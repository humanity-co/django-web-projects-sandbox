import tkinter as tk
from tkinter import messagebox

# Sample function to handle language selection
def change_language(language):
    if language == "English":
        label.config(text="Select body part to report pain:")
        btn1.config(text="Head")
        btn2.config(text="Chest")
        btn3.config(text="Leg")
        # Add more button text changes here for other body parts
    elif language == "Marathi":
        label.config(text="दुखण्याच्या शरीराच्या भागाची निवड करा:")
        btn1.config(text="तोंड")
        btn2.config(text="छाती")
        btn3.config(text="पाय")
        # Add more button text changes here for Marathi
    elif language == "Hindi":
        label.config(text="दर्द रिपोर्ट करने के लिए शरीर का हिस्सा चुनें:")
        btn1.config(text="सिर")
        btn2.config(text="छाती")
        btn3.config(text="पैर")
        # Add more button text changes here for Hindi

# Basic function to handle body part selection
def body_part_selected(part):
    messagebox.showinfo("Pain Report", f"You selected: {part}.\nPlease continue with the next steps.")

# Main window setup
window = tk.Tk()
window.title("Hospital Kiosk - Patient Assistance")
window.geometry("500x400")

# Language selection dropdown
language_var = tk.StringVar(value="English")
language_menu = tk.OptionMenu(window, language_var, "English", "Marathi", "Hindi", command=change_language)
language_menu.pack(pady=10)

# Instruction label
label = tk.Label(window, text="Select body part to report pain:")
label.pack(pady=20)

# Buttons for body part selection (front and back could be implemented with different buttons or images)
btn1 = tk.Button(window, text="Head", command=lambda: body_part_selected("Head"))
btn1.pack(pady=10)

btn2 = tk.Button(window, text="Chest", command=lambda: body_part_selected("Chest"))
btn2.pack(pady=10)

btn3 = tk.Button(window, text="Leg", command=lambda: body_part_selected("Leg"))
btn3.pack(pady=10)

# Optional: Adding more buttons for other body parts and functionalities
# ...

# Run the application
window.mainloop()
