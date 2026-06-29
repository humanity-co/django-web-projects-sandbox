import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands and OpenCV
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Prompt user to enter the image file path
image_path = input("Please enter the path to the image you want to zoom in and out: ")

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image. Please check the file path.")
    exit()

# Get the image dimensions (height and width)
height, width, _ = image.shape

# Create an initial zoom factor
zoom_factor = 1.0
previous_distance = 0

def calculate_distance(thumb_tip, index_tip):
    """Calculate Euclidean distance between the thumb and index finger tips."""
    return math.sqrt((thumb_tip[0] - index_tip[0]) ** 2 + (thumb_tip[1] - index_tip[1]) ** 2)

while True:
    # Start video capture
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to RGB (MediaPipe works with RGB images)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # If hands are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Get the positions of the thumb and index finger tips
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Get the screen coordinates of the landmarks
            thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
            index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)
            
            # Calculate the distance between the thumb and index finger
            current_distance = calculate_distance((thumb_x, thumb_y), (index_x, index_y))
            
            # If we have a previous distance, calculate the zoom based on the change in distance
            if previous_distance > 0:
                zoom_factor += (current_distance - previous_distance) * 0.01
            
            # Update previous distance
            previous_distance = current_distance
            
            # Limit zoom factor to avoid extreme zoom-in or zoom-out
            zoom_factor = max(0.5, min(zoom_factor, 2.0))
            
            # Resize the image based on the zoom factor
            zoomed_image = cv2.resize(image, (0, 0), fx=zoom_factor, fy=zoom_factor)
            
            # Display the zoomed image on the frame
            height, width, _ = zoomed_image.shape
            x_offset = (frame.shape[1] - width) // 2
            y_offset = (frame.shape[0] - height) // 2
            frame[y_offset:y_offset + height, x_offset:x_offset + width] = zoomed_image

            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Display the final frame with zoomed image
    cv2.imshow('Pinch-to-Zoom', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
