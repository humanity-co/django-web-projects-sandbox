from flask import Flask, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)

# Speech Recognition function
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Sorry, the speech recognition service is down."

# Route for speech recognition
@app.route("/recognize_speech", methods=["GET"])
def recognize_speech():
    text = recognize_speech_from_microphone()
    return jsonify({"speech_text": text})

# Serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
