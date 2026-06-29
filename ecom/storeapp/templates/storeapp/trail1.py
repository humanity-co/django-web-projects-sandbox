import tkinter as tk
from tkinter import ttk, messagebox, font
import json
import uuid
from datetime import datetime, timedelta
import random
import os
from PIL import Image, ImageTk

class HospitalKioskSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Kiosk System")
        self.root.geometry("1024x768")
        self.root.configure(bg="#f0f0f0")
        
        # Set up fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=14)
        self.text_font = font.Font(family="Helvetica", size=12)
        
        # Define color scheme
        self.primary_color = "#007bff"  # Blue
        self.secondary_color = "#6c757d"  # Gray
        self.success_color = "#28a745"  # Green
        self.danger_color = "#dc3545"  # Red
        self.light_color = "#f8f9fa"  # Light gray
        
        # Initialize data structures
        self.initialize_data()
        
        # Language support
        self.languages = {
            "English": {
                "welcome": "Welcome to Hospital Kiosk",
                "select_language": "Select your preferred language",
                "new_patient": "New Patient",
                "existing_patient": "Existing Patient",
                "emergency": "Emergency",
                "back": "Back",
                "next": "Next",
                "confirm": "Confirm",
                "cancel": "Cancel",
                "select_pain_area": "Select area(s) where you feel pain",
                "pain_intensity": "Select pain intensity",
                "mild": "Mild",
                "moderate": "Moderate",
                "severe": "Severe",
                "pain_type": "Select pain type",
                "sharp": "Sharp",
                "dull": "Dull",
                "throbbing": "Throbbing",
                "select_doctor": "Select a doctor",
                "schedule_appointment": "Schedule Appointment",
                "personal_details": "Enter Personal Details",
                "name": "Name",
                "age": "Age",
                "gender": "Gender",
                "contact": "Contact Number",
                "email": "Email",
                "address": "Address",
                "appointment_confirmed": "Appointment Confirmed",
                "appointment_details": "Appointment Details",
                "confirmation_number": "Confirmation Number",
                "print": "Print",
                "email_confirmation": "Email Confirmation",
                "thank_you": "Thank you for using our service",
                "accessibility": "Accessibility Options",
                "increase_font": "Increase Font Size",
                "decrease_font": "Decrease Font Size",
                "high_contrast": "High Contrast Mode",
                "audio_guide": "Audio Guide",
                "front_view": "Front View",
                "back_view": "Back View",
                "head": "Head",
                "chest": "Chest",
                "abdomen": "Abdomen",
                "arms": "Arms",
                "legs": "Legs",
                "follow_up": "Follow-up Visit",
                "view_history": "View Visit History",
                "request_refill": "Request Prescription Refill",
                "nearby_facilities": "Nearby Facilities",
                "pharmacy": "Pharmacy",
                "emergency_room": "Emergency Room",
                "laboratory": "Laboratory",
                "general_practitioner": "General Practitioner",
                "cardiologist": "Cardiologist",
                "neurologist": "Neurologist",
                "orthopedist": "Orthopedist",
                "dermatologist": "Dermatologist",
                "select_time": "Select Time Slot",
                "morning": "Morning",
                "afternoon": "Afternoon",
                "evening": "Evening"
            },
            "Hindi": {
                "welcome": "अस्पताल किओस्क में आपका स्वागत है",
                "select_language": "अपनी पसंदीदा भाषा चुनें",
                "new_patient": "नया रोगी",
                "existing_patient": "मौजूदा रोगी",
                "emergency": "आपातकालीन",
                "back": "वापस",
                "next": "आगे",
                "confirm": "पुष्टि करें",
                "cancel": "रद्द करें",
                "select_pain_area": "वह क्षेत्र चुनें जहां आपको दर्द महसूस होता है",
                "pain_intensity": "दर्द की तीव्रता का चयन करें",
                "mild": "हल्का",
                "moderate": "मध्यम",
                "severe": "गंभीर",
                "pain_type": "दर्द के प्रकार का चयन करें",
                "sharp": "तेज",
                "dull": "मंद",
                "throbbing": "धड़कता हुआ",
                "select_doctor": "एक डॉक्टर चुनें",
                "schedule_appointment": "अपॉइंटमेंट शेड्यूल करें",
                "personal_details": "व्यक्तिगत विवरण दर्ज करें",
                "name": "नाम",
                "age": "आयु",
                "gender": "लिंग",
                "contact": "संपर्क नंबर",
                "email": "ईमेल",
                "address": "पता",
                "appointment_confirmed": "अपॉइंटमेंट की पुष्टि हो गई है",
                "appointment_details": "अपॉइंटमेंट विवरण",
                "confirmation_number": "पुष्टिकरण संख्या",
                "print": "प्रिंट",
                "email_confirmation": "ईमेल पुष्टिकरण",
                "thank_you": "हमारी सेवा का उपयोग करने के लिए धन्यवाद",
                "accessibility": "पहुंच विकल्प",
                "increase_font": "फॉन्ट आकार बढ़ाएं",
                "decrease_font": "फॉन्ट आकार घटाएं",
                "high_contrast": "हाई कंट्रास्ट मोड",
                "audio_guide": "ऑडियो गाइड",
                "front_view": "सामने का दृश्य",
                "back_view": "पीछे का दृश्य",
                "head": "सिर",
                "chest": "छाती",
                "abdomen": "पेट",
                "arms": "बाहें",
                "legs": "पैर",
                "follow_up": "फॉलो-अप विजिट",
                "view_history": "विजिट हिस्ट्री देखें",
                "request_refill": "प्रिस्क्रिप्शन रिफिल का अनुरोध करें",
                "nearby_facilities": "आस-पास की सुविधाएं",
                "pharmacy": "फार्मेसी",
                "emergency_room": "आपातकालीन कक्ष",
                "laboratory": "प्रयोगशाला",
                "general_practitioner": "जनरल प्रैक्टिशनर",
                "cardiologist": "हृदय रोग विशेषज्ञ",
                "neurologist": "न्यूरोलॉजिस्ट",
                "orthopedist": "हड्डी रोग विशेषज्ञ",
                "dermatologist": "त्वचा विशेषज्ञ",
                "select_time": "समय स्लॉट चुनें",
                "morning": "सुबह",
                "afternoon": "दोपहर",
                "evening": "शाम"
            },
            "Marathi": {
                "welcome": "हॉस्पिटल कियॉस्कमध्ये आपले स्वागत आहे",
                "select_language": "आपली पसंतीची भाषा निवडा",
                "new_patient": "नवीन रुग्ण",
                "existing_patient": "विद्यमान रुग्ण",
                "emergency": "आपत्कालीन",
                "back": "मागे",
                "next": "पुढे",
                "confirm": "पुष्टी करा",
                "cancel": "रद्द करा",
                "select_pain_area": "जिथे आपल्याला वेदना जाणवतात ते क्षेत्र निवडा",
                "pain_intensity": "वेदनेची तीव्रता निवडा",
                "mild": "सौम्य",
                "moderate": "मध्यम",
                "severe": "तीव्र",
                "pain_type": "वेदनेचा प्रकार निवडा",
                "sharp": "तीक्ष्ण",
                "dull": "मंद",
                "throbbing": "ठुसठुसणारी",
                "select_doctor": "डॉक्टर निवडा",
                "schedule_appointment": "अपॉइंटमेंट शेड्यूल करा",
                "personal_details": "वैयक्तिक तपशील प्रविष्ट करा",
                "name": "नाव",
                "age": "वय",
                "gender": "लिंग",
                "contact": "संपर्क क्रमांक",
                "email": "ईमेल",
                "address": "पत्ता",
                "appointment_confirmed": "अपॉइंटमेंट पुष्टी झाली",
                "appointment_details": "अपॉइंटमेंट तपशील",
                "confirmation_number": "पुष्टीकरण क्रमांक",
                "print": "प्रिंट",
                "email_confirmation": "ईमेल पुष्टीकरण",
                "thank_you": "आमच्या सेवेचा वापर केल्याबद्दल धन्यवाद",
                "accessibility": "प्रवेशयोग्यता पर्याय",
                "increase_font": "फॉन्ट आकार वाढवा",
                "decrease_font": "फॉन्ट आकार कमी करा",
                "high_contrast": "उच्च कॉन्ट्रास्ट मोड",
                "audio_guide": "ऑडिओ गाइड",
                "front_view": "समोरचा दृश्य",
                "back_view": "मागचा दृश्य",
                "head": "डोके",
                "chest": "छाती",
                "abdomen": "पोट",
                "arms": "हात",
                "legs": "पाय",
                "follow_up": "फॉलो-अप भेट",
                "view_history": "भेटीचा इतिहास पहा",
                "request_refill": "प्रिस्क्रिप्शन रिफिल साठी विनंती करा",
                "nearby_facilities": "जवळपासच्या सुविधा",
                "pharmacy": "फार्मसी",
                "emergency_room": "आपत्कालीन कक्ष",
                "laboratory": "प्रयोगशाळा",
                "general_practitioner": "जनरल प्रॅक्टिशनर",
                "cardiologist": "हृदयरोग तज्ञ",
                "neurologist": "न्यूरोलॉजिस्ट",
                "orthopedist": "हाडांचे तज्ञ",
                "dermatologist": "त्वचा तज्ञ",
                "select_time": "वेळ स्लॉट निवडा",
                "morning": "सकाळ",
                "afternoon": "दुपार",
                "evening": "संध्याकाळ"
            }
        }
        
        # Current language (default is English)
        self.current_language = "English"
        
        # Patient data
        self.current_patient = {
            "is_new": True,
            "personal_details": {},
            "pain_areas": [],
            "pain_intensity": {},
            "pain_type": {},
            "selected_doctor": None,
            "appointment_time": None,
            "confirmation_number": None
        }
        
        # Initialize accessibility settings
        self.accessibility = {
            "font_size_multiplier": 1.0,
            "high_contrast": False,
            "audio_guide": False
        }
        
        # Create main container frame
        self.main_container = tk.Frame(self.root, bg="#f0f0f0")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header frame
        self.header_frame = tk.Frame(self.main_container, bg="#f0f0f0")
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Create content frame
        self.content_frame = tk.Frame(self.main_container, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create footer frame
        self.footer_frame = tk.Frame(self.main_container, bg="#f0f0f0")
        self.footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Add accessibility buttons to footer
        self.create_accessibility_buttons()
        
        # Start with language selection screen
        self.show_language_selection()
    
    def initialize_data(self):
        # Initialize doctors data
        self.doctors = {
            "General Practitioner": [
                {"id": "GP001", "name": "Dr. John Smith", "specialization": "General Practitioner", "availability": ["09:00", "10:00", "11:00", "14:00", "15:00"], "rating": 4.8},
                {"id": "GP002", "name": "Dr. Sarah Johnson", "specialization": "General Practitioner", "availability": ["09:30", "10:30", "11:30", "14:30", "15:30"], "rating": 4.7}
            ],
            "Cardiologist": [
                {"id": "CD001", "name": "Dr. Michael Chen", "specialization": "Cardiologist", "availability": ["10:00", "11:00", "14:00", "15:00", "16:00"], "rating": 4.9},
                {"id": "CD002", "name": "Dr. Emma Wilson", "specialization": "Cardiologist", "availability": ["09:00", "11:30", "13:30", "15:30"], "rating": 4.8}
            ],
            "Neurologist": [
                {"id": "NR001", "name": "Dr. Robert Brown", "specialization": "Neurologist", "availability": ["09:00", "10:30", "13:00", "14:30", "16:00"], "rating": 4.7},
                {"id": "NR002", "name": "Dr. Lisa Wong", "specialization": "Neurologist", "availability": ["08:30", "10:00", "13:30", "15:00", "16:30"], "rating": 4.9}
            ],
            "Orthopedist": [
                {"id": "OR001", "name": "Dr. James Davis", "specialization": "Orthopedist", "availability": ["08:00", "09:30", "11:00", "14:00", "16:00"], "rating": 4.6},
                {"id": "OR002", "name": "Dr. Maria Rodriguez", "specialization": "Orthopedist", "availability": ["09:00", "10:30", "13:00", "15:30"], "rating": 4.8}
            ],
            "Dermatologist": [
                {"id": "DM001", "name": "Dr. David Lee", "specialization": "Dermatologist", "availability": ["08:30", "10:00", "11:30", "14:00", "15:30"], "rating": 4.7},
                {"id": "DM002", "name": "Dr. Jessica Park", "specialization": "Dermatologist", "availability": ["09:00", "11:00", "13:30", "16:00"], "rating": 4.8}
            ]
        }
        
        # Initialize existing patients data (simplified for demo)
        self.existing_patients = {
            "P12345": {
                "name": "John Doe",
                "age": 45,
                "gender": "Male",
                "contact": "9876543210",
                "email": "john.doe@example.com",
                "address": "123 Main St, Anytown",
                "visit_history": [
                    {"date": "2023-01-15", "doctor": "Dr. Michael Chen", "diagnosis": "Hypertension", "prescription": "Amlodipine 5mg"},
                    {"date": "2023-03-10", "doctor": "Dr. Michael Chen", "diagnosis": "Follow-up", "prescription": "Continue Amlodipine 5mg"}
                ]
            },
            "P67890": {
                "name": "Jane Smith",
                "age": 35,
                "gender": "Female",
                "contact": "9876543211",
                "email": "jane.smith@example.com",
                "address": "456 Elm St, Anytown",
                "visit_history": [
                    {"date": "2023-02-20", "doctor": "Dr. Lisa Wong", "diagnosis": "Migraine", "prescription": "Sumatriptan 50mg"},
                    {"date": "2023-04-05", "doctor": "Dr. Lisa Wong", "diagnosis": "Follow-up", "prescription": "Sumatriptan 50mg as needed"}
                ]
            }
        }
        
        # Body parts mapping to specializations (simplified)
        self.body_part_to_specialization = {
            "head": ["Neurologist", "General Practitioner"],
            "chest": ["Cardiologist", "General Practitioner"],
            "abdomen": ["General Practitioner"],
            "arms": ["Orthopedist", "General Practitioner"],
            "legs": ["Orthopedist", "General Practitioner"]
        }
    
    def get_text(self, key):
        """Get text in current language"""
        return self.languages[self.current_language].get(key, key)
    
    def clear_frame(self, frame):
        """Clear all widgets from a frame"""
        for widget in frame.winfo_children():
            widget.destroy()
    
    def create_styled_button(self, parent, text, command, width=15, height=2, font=None):
        """Create a styled button with hover effect"""
        if font is None:
            font = self.button_font
            
        button = tk.Button(
            parent,
            text=text,
            font=font,
            bg=self.primary_color,
            fg="white",
            activebackground="#0069d9",
            activeforeground="white",
            relief=tk.FLAT,
            borderwidth=0,
            padx=10,
            pady=5,
            command=command
        )
        
        # Add hover effect
        button.bind("<Enter>", lambda e: button.config(background="#0069d9"))
        button.bind("<Leave>", lambda e: button.config(background=self.primary_color))
        
        return button
    
    def create_header(self, title_text):
        """Create header with title and back button if needed"""
        self.clear_frame(self.header_frame)
        
        # Add back button if not on language selection
        if title_text != self.get_text("select_language"):
            back_button = self.create_styled_button(
                self.header_frame,
                self.get_text("back"),
                self.go_back,
                width=8,
                height=1
            )
            back_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Add title
        title_label = tk.Label(
            self.header_frame,
            text=title_text,
            font=self.title_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(side=tk.LEFT, padx=10)
        
        # Add emergency button
        emergency_button = self.create_styled_button(
            self.header_frame,
            self.get_text("emergency"),
            self.show_emergency_screen,
            width=10,
            height=1
        )
        emergency_button.config(bg=self.danger_color)
        emergency_button.bind("<Enter>", lambda e: emergency_button.config(background="#c82333"))
        emergency_button.bind("<Leave>", lambda e: emergency_button.config(background=self.danger_color))
        emergency_button.pack(side=tk.RIGHT, padx=(10, 0))
    
    def create_accessibility_buttons(self):
        """Create accessibility buttons in footer"""
        self.clear_frame(self.footer_frame)
        
        # Create a frame for accessibility buttons
        accessibility_frame = tk.Frame(self.footer_frame, bg="#f0f0f0")
        accessibility_frame.pack(side=tk.RIGHT)
        
        # Increase font size button
        increase_font_button = self.create_styled_button(
            accessibility_frame,
            "A+",
            self.increase_font_size,
            width=3,
            height=1
        )
        increase_font_button.pack(side=tk.LEFT, padx=5)
        
        # Decrease font size button
        decrease_font_button = self.create_styled_button(
            accessibility_frame,
            "A-",
            self.decrease_font_size,
            width=3,
            height=1
        )
        decrease_font_button.pack(side=tk.LEFT, padx=5)
        
        # High contrast button
        high_contrast_button = self.create_styled_button(
            accessibility_frame,
            "HC",
            self.toggle_high_contrast,
            width=3,
            height=1
        )
        high_contrast_button.pack(side=tk.LEFT, padx=5)
        
        # Audio guide button
        audio_button = self.create_styled_button(
            accessibility_frame,
            "🔊",
            self.toggle_audio_guide,
            width=3,
            height=1
        )
        audio_button.pack(side=tk.LEFT, padx=5)
    
    def increase_font_size(self):
        """Increase font size for accessibility"""
        if self.accessibility["font_size_multiplier"] < 1.5:
            self.accessibility["font_size_multiplier"] += 0.1
            self.update_fonts()
    
    def decrease_font_size(self):
        """Decrease font size for accessibility"""
        if self.accessibility["font_size_multiplier"] > 0.8:
            self.accessibility["font_size_multiplier"] -= 0.1
            self.update_fonts()
    
    def update_fonts(self):
        """Update all fonts based on the current multiplier"""
        multiplier = self.accessibility["font_size_multiplier"]
        
        self.title_font.configure(size=int(24 * multiplier))
        self.header_font.configure(size=int(18 * multiplier))
        self.button_font.configure(size=int(14 * multiplier))
        self.text_font.configure(size=int(12 * multiplier))
        
        # Refresh current screen
        self.refresh_current_screen()
    
    def toggle_high_contrast(self):
        """Toggle high contrast mode for accessibility"""
        self.accessibility["high_contrast"] = not self.accessibility["high_contrast"]
        
        if self.accessibility["high_contrast"]:
            self.root.configure(bg="black")
            self.main_container.configure(bg="black")
            self.header_frame.configure(bg="black")
            self.content_frame.configure(bg="black")
            self.footer_frame.configure(bg="black")
            
            # Update text colors for high contrast
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.configure(bg="black", fg="white")
        else:
            self.root.configure(bg="#f0f0f0")
            self.main_container.configure(bg="#f0f0f0")
            self.header_frame.configure(bg="#f0f0f0")
            self.content_frame.configure(bg="#f0f0f0")
            self.footer_frame.configure(bg="#f0f0f0")
            
            # Reset text colors
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.configure(bg="#f0f0f0", fg="#333333")
        
        # Refresh current screen
        self.refresh_current_screen()
    
    def toggle_audio_guide(self):
        """Toggle audio guide for accessibility"""
        self.accessibility["audio_guide"] = not self.accessibility["audio_guide"]
        
        # For a real implementation, this would trigger text-to-speech
        # Here we'll just show a message
        if self.accessibility["audio_guide"]:
            messagebox.showinfo("Audio Guide", "Audio guide is now enabled. Voice instructions will be provided.")
        else:
            messagebox.showinfo("Audio Guide", "Audio guide is now disabled.")
    
    def go_back(self):
        """Go back to previous screen"""
        # Navigation history would be implemented here
        # For simplicity, we'll just go back to the main menu
        self.show_patient_type_selection()
    
    def refresh_current_screen(self):
        """Refresh the current screen (for accessibility changes)"""
        # This would be implemented with a proper screen history
        # For simplicity, we'll just go back to language selection
        self.show_language_selection()
    
    def show_language_selection(self):
        """Show language selection screen"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("select_language"))
        
        # Create a frame for language buttons
        language_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        language_frame.pack(expand=True)
        
        # Create language buttons
        for language in self.languages.keys():
            button = self.create_styled_button(
                language_frame,
                language,
                lambda lang=language: self.set_language(lang),
                width=20,
                height=3
            )
            button.pack(pady=10)
    
    def set_language(self, language):
        """Set the current language and proceed to patient type selection"""
        self.current_language = language
        self.show_patient_type_selection()
    
    def show_patient_type_selection(self):
        """Show new/existing patient selection screen"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("welcome"))
        
        # Create a frame for patient type buttons
        patient_type_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        patient_type_frame.pack(expand=True)
        
        # Create patient type buttons
        new_patient_button = self.create_styled_button(
            patient_type_frame,
            self.get_text("new_patient"),
            lambda: self.set_patient_type(True),
            width=20,
            height=3
        )
        new_patient_button.pack(pady=10)
        
        existing_patient_button = self.create_styled_button(
            patient_type_frame,
            self.get_text("existing_patient"),
            lambda: self.set_patient_type(False),
            width=20,
            height=3
        )
        existing_patient_button.pack(pady=10)
    
    def set_patient_type(self, is_new):
        """Set patient type and proceed to appropriate screen"""
        self.current_patient["is_new"] = is_new
        
        if is_new:
            self.show_personal_details()
        else:
            self.show_patient_id_entry()
    
    def show_personal_details(self):
        """Show personal details entry form for new patients"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("personal_details"))
        
        # Create a frame for form
        form_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        form_frame.pack(expand=True, fill=tk.BOTH, padx=50)
        
        # Create form fields
        fields = [
            ("name", self.get_text("name")),
            ("age", self.get_text("age")),
            ("gender", self.get_text("gender")),
            ("contact", self.get_text("contact")),
            ("email", self.get_text("email")),
            ("address", self.get_text("address"))
        ]
        
        self.form_entries = {}
        
        for i, (field, label) in enumerate(fields):
            # Create label
            label = tk.Label(form_frame, text=label, font=self.text_font, bg="#f0f0f0", anchor="w")
            label.grid(row=i, column=0, sticky="w", pady=5, padx=5)
            
            # Create entry
            entry = tk.Entry(form_frame, font=self.text_font, width=30)
            entry.grid(row=i, column=1, sticky="ew", pady=5, padx=5)
            
            self.form_entries[field] = entry
        
        # Add gender dropdown (replace entry)
        gender_options = ["Male", "Female", "Other"]
        gender_var = tk.StringVar(form_frame)
        gender_var.set(gender_options[0])
        gender_dropdown = ttk.Combobox(form_frame, textvariable=gender_var, values=gender_options, font=self.text_font, state="readonly")
        gender_dropdown.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
        self.form_entries["gender"] = gender_dropdown

        # Add a button frame
        button_frame = tk.Frame(form_frame, bg="#f0f0f0")
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        # Add next button
        next_button = self.create_styled_button(
            button_frame,
            self.get_text("next"),
            self.save_personal_details,
            width=15,
            height=2
        )
        next_button.pack()
    
    def save_personal_details(self):
        """Save personal details and proceed to body diagram"""
        # Validate form
        for field, entry in self.form_entries.items():
            if isinstance(entry, ttk.Combobox):
                value = entry.get()
            else:
                value = entry.get().strip()
            
            if not value:
                messagebox.showerror("Error", f"{field.capitalize()} is required")
                return
            
            self.current_patient["personal_details"][field] = value
        
        # Generate patient ID for new patients
        if self.current_patient["is_new"]:
            patient_id = f"P{random.randint(10000, 99999)}"
            while patient_id in self.existing_patients:
                patient_id = f"P{random.randint(10000, 99999)}"
            
            self.current_patient["personal_details"]["patient_id"] = patient_id
        
        # Proceed to body diagram
        self.show_body_diagram()
    
    def show_patient_id_entry(self):
        """Show patient ID entry for existing patients"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("existing_patient"))
        
        # Create a frame for ID entry
        id_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        id_frame.pack(expand=True)
        
        # Add instructions
        instructions = tk.Label(
            id_frame,
            text="Please enter your Patient ID:",
            font=self.header_font,
            bg="#f0f0f0"
        )
        instructions.pack(pady=10)
        
        # Add ID entry
        self.patient_id_entry = tk.Entry(id_frame, font=self.text_font, width=20)
        self.patient_id_entry.pack(pady=10)
        
        # Add login button
        login_button = self.create_styled_button(
            id_frame,
            "Login",
            self.verify_patient_id,
            width=15,
            height=2
        )
        login_button.pack(pady=10)
        
        # For demo purposes, add some sample patient IDs
        sample_ids = tk.Label(
            id_frame,
            text="Sample IDs: P12345, P67890",
            font=self.text_font,
            bg="#f0f0f0",
            fg="#666666"
        )
        sample_ids.pack(pady=5)
    
    def verify_patient_id(self):
        """Verify patient ID and proceed to patient options"""
        patient_id = self.patient_id_entry.get().strip()
        
        if patient_id in self.existing_patients:
            # Load patient data
            self.current_patient["personal_details"] = self.existing_patients[patient_id].copy()
            self.current_patient["personal_details"]["patient_id"] = patient_id
            
            # Show existing patient options
            self.show_existing_patient_options()
        else:
            messagebox.showerror("Error", "Invalid Patient ID. Please try again.")
    
    def show_existing_patient_options(self):
        """Show options for existing patients"""
        self.clear_frame(self.content_frame)
        self.create_header(f"Welcome, {self.current_patient['personal_details']['name']}")
        
        # Create a frame for options
        options_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        options_frame.pack(expand=True)
        
        # Add option buttons
        options = [
            (self.get_text("follow_up"), self.show_body_diagram),
            (self.get_text("view_history"), self.show_visit_history),
            (self.get_text("request_refill"), self.show_prescription_refill)
        ]
        
        for option_text, option_command in options:
            button = self.create_styled_button(
                options_frame,
                option_text,
                option_command,
                width=25,
                height=2
            )
            button.pack(pady=10)
    
    def show_visit_history(self):
        """Show visit history for existing patients"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("view_history"))
        
        # Create a frame for history
        history_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        history_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Add history table
        columns = ["Date", "Doctor", "Diagnosis", "Prescription"]
        
        # Create headers
        for i, col in enumerate(columns):
            header = tk.Label(
                history_frame,
                text=col,
                font=self.header_font,
                bg="#e0e0e0",
                relief=tk.RAISED,
                padx=10,
                pady=5,
                width=15
            )
            header.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)
        
        # Add visit data
        visit_history = self.existing_patients[self.current_patient["personal_details"]["patient_id"]]["visit_history"]
        
        for i, visit in enumerate(visit_history, 1):
            for j, col in enumerate(columns):
                key = col.lower()
                value = visit.get(key, "")
                
                cell = tk.Label(
                    history_frame,
                    text=value,
                    font=self.text_font,
                    bg="#f9f9f9",
                    relief=tk.RIDGE,
                    padx=10,
                    pady=5,
                    width=15
                )
                cell.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        
        # Add back to options button
        back_button = self.create_styled_button(
            history_frame,
            self.get_text("back"),
            self.show_existing_patient_options,
            width=15,
            height=2
        )
        back_button.grid(row=len(visit_history) + 1, column=0, columnspan=len(columns), pady=20)
    
    def show_prescription_refill(self):
        """Show prescription refill request screen"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("request_refill"))
        
        # Create a frame for refill options
        refill_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        refill_frame.pack(expand=True)
        
        # Get prescriptions from visit history
        visit_history = self.existing_patients[self.current_patient["personal_details"]["patient_id"]]["visit_history"]
        prescriptions = [visit.get("prescription", "") for visit in visit_history if visit.get("prescription")]
        
        # Add label
        instructions = tk.Label(
            refill_frame,
            text="Select prescription to refill:",
            font=self.header_font,
            bg="#f0f0f0"
        )
        instructions.pack(pady=10)
        
        # Add prescription options
        self.refill_var = tk.StringVar(refill_frame)
        
        for i, prescription in enumerate(prescriptions):
            radio = tk.Radiobutton(
                refill_frame,
                text=prescription,
                variable=self.refill_var,
                value=prescription,
                font=self.text_font,
                bg="#f0f0f0"
            )
            radio.pack(anchor="w", pady=5)
            
            # Select first option by default
            if i == 0:
                self.refill_var.set(prescription)
        
        # Add request button
        request_button = self.create_styled_button(
            refill_frame,
            "Request Refill",
            self.process_refill_request,
            width=15,
            height=2
        )
        request_button.pack(pady=20)
    
    def process_refill_request(self):
        """Process prescription refill request"""
        prescription = self.refill_var.get()
        
        if prescription:
            # In a real system, this would submit the request to the hospital database
            messagebox.showinfo("Success", f"Refill request submitted for: {prescription}\n\nYou will be notified when it's ready for pickup.")
            self.show_existing_patient_options()
        else:
            messagebox.showerror("Error", "Please select a prescription to refill.")
    
    def show_body_diagram(self):
        """Show interactive body diagram for pain selection"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("select_pain_area"))
        
        # Create main content frame
        diagram_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        diagram_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Create view selection frame
        view_frame = tk.Frame(diagram_frame, bg="#f0f0f0")
        view_frame.pack(pady=10)
        
        # View selection buttons
        self.view_var = tk.StringVar(value="front")
        
        front_button = tk.Radiobutton(
            view_frame,
            text=self.get_text("front_view"),
            variable=self.view_var,
            value="front",
            command=self.update_body_view,
            font=self.text_font,
            bg="#f0f0f0"
        )
        front_button.pack(side=tk.LEFT, padx=10)
        
        back_button = tk.Radiobutton(
            view_frame,
            text=self.get_text("back_view"),
            variable=self.view_var,
            value="back",
            command=self.update_body_view,
            font=self.text_font,
            bg="#f0f0f0"
        )
        back_button.pack(side=tk.LEFT, padx=10)
        
        # Create body diagram frame
        self.body_frame = tk.Frame(diagram_frame, bg="#f0f0f0")
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        
        # Create body part selection
        self.update_body_view()
        
        # Create selected areas display
        selected_frame = tk.Frame(diagram_frame, bg="#f0f0f0")
        selected_frame.pack(pady=10, fill=tk.X)
        
        selected_label = tk.Label(
            selected_frame,
            text="Selected areas:",
            font=self.text_font,
            bg="#f0f0f0"
        )
        selected_label.pack(side=tk.LEFT, padx=5)
        
        self.selected_areas_label = tk.Label(
            selected_frame,
            text="None",
            font=self.text_font,
            bg="#f0f0f0",
            fg=self.primary_color
        )
        self.selected_areas_label.pack(side=tk.LEFT)
        
        # Add next button
        next_button = self.create_styled_button(
            diagram_frame,
            self.get_text("next"),
            self.proceed_to_pain_details,
            width=15,
            height=2
        )
        next_button.pack(pady=10)
        
        # Initialize pain areas
        self.current_patient["pain_areas"] = []
    
    def update_body_view(self):
        """Update body diagram based on selected view"""
        self.clear_frame(self.body_frame)
        
        view = self.view_var.get()
        
        # In a real system, we would use actual body diagrams
        # For this demo, we'll use a simple representation with buttons
        
        # Create a canvas for the body diagram
        canvas_width = 300
        canvas_height = 500
        
        canvas = tk.Canvas(
            self.body_frame,
            width=canvas_width,
            height=canvas_height,
            bg="white",
            highlightthickness=1,
            highlightbackground="#cccccc"
        )
        canvas.pack(pady=10)
        
        # Draw a simple body outline
        if view == "front":
            # Head
            head = canvas.create_oval(120, 30, 180, 90, fill="#f0f0f0", outline="black", width=2, tags="head")
            
            # Torso
            torso = canvas.create_rectangle(110, 90, 190, 250, fill="#f0f0f0", outline="black", width=2)
            chest = canvas.create_rectangle(110, 90, 190, 170, fill="#f0f0f0", outline="black", width=2, tags="chest")
            abdomen = canvas.create_rectangle(110, 170, 190, 250, fill="#f0f0f0", outline="black", width=2, tags="abdomen")
            
            # Arms
            left_arm = canvas.create_rectangle(70, 100, 110, 220, fill="#f0f0f0", outline="black", width=2, tags="arms")
            right_arm = canvas.create_rectangle(190, 100, 230, 220, fill="#f0f0f0", outline="black", width=2, tags="arms")
            
            # Legs
            left_leg = canvas.create_rectangle(110, 250, 145, 450, fill="#f0f0f0", outline="black", width=2, tags="legs")
            right_leg = canvas.create_rectangle(155, 250, 190, 450, fill="#f0f0f0", outline="black", width=2, tags="legs")
            
            # Add labels
            canvas.create_text(150, 60, text=self.get_text("head"), font=self.text_font)
            canvas.create_text(150, 130, text=self.get_text("chest"), font=self.text_font)
            canvas.create_text(150, 210, text=self.get_text("abdomen"), font=self.text_font)
            canvas.create_text(70, 160, text=self.get_text("arms"), font=self.text_font)
            canvas.create_text(230, 160, text=self.get_text("arms"), font=self.text_font)
            canvas.create_text(127, 350, text=self.get_text("legs"), font=self.text_font)
            canvas.create_text(173, 350, text=self.get_text("legs"), font=self.text_font)
        else:  # back view
            # Head
            head = canvas.create_oval(120, 30, 180, 90, fill="#f0f0f0", outline="black", width=2, tags="head")
            
            # Torso
            torso = canvas.create_rectangle(110, 90, 190, 250, fill="#f0f0f0", outline="black", width=2)
            back_upper = canvas.create_rectangle(110, 90, 190, 170, fill="#f0f0f0", outline="black", width=2, tags="chest")
            back_lower = canvas.create_rectangle(110, 170, 190, 250, fill="#f0f0f0", outline="black", width=2, tags="abdomen")
            
            # Arms
            left_arm = canvas.create_rectangle(70, 100, 110, 220, fill="#f0f0f0", outline="black", width=2, tags="arms")
            right_arm = canvas.create_rectangle(190, 100, 230, 220, fill="#f0f0f0", outline="black", width=2, tags="arms")
            
            # Legs
            left_leg = canvas.create_rectangle(110, 250, 145, 450, fill="#f0f0f0", outline="black", width=2, tags="legs")
            right_leg = canvas.create_rectangle(155, 250, 190, 450, fill="#f0f0f0", outline="black", width=2, tags="legs")
            
            # Add labels
            canvas.create_text(150, 60, text=self.get_text("head"), font=self.text_font)
            canvas.create_text(150, 130, text=self.get_text("chest") + " (Back)", font=self.text_font)
            canvas.create_text(150, 210, text=self.get_text("abdomen") + " (Back)", font=self.text_font)
            canvas.create_text(70, 160, text=self.get_text("arms"), font=self.text_font)
            canvas.create_text(230, 160, text=self.get_text("arms"), font=self.text_font)
            canvas.create_text(127, 350, text=self.get_text("legs"), font=self.text_font)
            canvas.create_text(173, 350, text=self.get_text("legs"), font=self.text_font)
        
        # Bind click events to body parts
        for part in ["head", "chest", "abdomen", "arms", "legs"]:
            canvas.tag_bind(part, "<Button-1>", lambda event, part=part: self.toggle_pain_area(part))
    
    def toggle_pain_area(self, part):
        """Toggle pain area selection"""
        if part in self.current_patient["pain_areas"]:
            self.current_patient["pain_areas"].remove(part)
        else:
            self.current_patient["pain_areas"].append(part)
        
        # Update selected areas display
        if self.current_patient["pain_areas"]:
            parts_text = ", ".join(self.get_text(part) for part in self.current_patient["pain_areas"])
            self.selected_areas_label.config(text=parts_text)
        else:
            self.selected_areas_label.config(text="None")
    
    def proceed_to_pain_details(self):
        """Proceed to pain details screen if areas are selected"""
        if not self.current_patient["pain_areas"]:
            messagebox.showerror("Error", "Please select at least one pain area.")
            return
        
        self.show_pain_details()
    
    def show_pain_details(self):
        """Show pain details screen for selected areas"""
        self.clear_frame(self.content_frame)
        self.create_header("Pain Details")
        
        # Create main content frame
        details_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        details_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Initialize pain details if not exists
        if "pain_intensity" not in self.current_patient:
            self.current_patient["pain_intensity"] = {}
        
        if "pain_type" not in self.current_patient:
            self.current_patient["pain_type"] = {}
        
        # Create a notebook for each pain area
        notebook = ttk.Notebook(details_frame)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        for area in self.current_patient["pain_areas"]:
            # Create a frame for this area
            area_frame = tk.Frame(notebook, bg="#f0f0f0", padx=20, pady=20)
            
            # Add to notebook
            notebook.add(area_frame, text=self.get_text(area))
            
            # Pain intensity
            intensity_label = tk.Label(
                area_frame,
                text=self.get_text("pain_intensity"),
                font=self.header_font,
                bg="#f0f0f0"
            )
            intensity_label.pack(anchor="w", pady=(10, 5))
            
            # Intensity options
            intensity_frame = tk.Frame(area_frame, bg="#f0f0f0")
            intensity_frame.pack(fill=tk.X, pady=5)
            
            intensity_var = tk.StringVar(value=self.current_patient["pain_intensity"].get(area, ""))
            
            for intensity in ["mild", "moderate", "severe"]:
                radio = tk.Radiobutton(
                    intensity_frame,
                    text=self.get_text(intensity),
                    variable=intensity_var,
                    value=intensity,
                    font=self.text_font,
                    bg="#f0f0f0",
                    command=lambda area=area, var=intensity_var: self.set_pain_intensity(area, var.get())
                )
                radio.pack(side=tk.LEFT, padx=10)
            
            # Pain type
            type_label = tk.Label(
                area_frame,
                text=self.get_text("pain_type"),
                font=self.header_font,
                bg="#f0f0f0"
            )
            type_label.pack(anchor="w", pady=(20, 5))
            
            # Type options
            type_frame = tk.Frame(area_frame, bg="#f0f0f0")
            type_frame.pack(fill=tk.X, pady=5)
            
            type_var = tk.StringVar(value=self.current_patient["pain_type"].get(area, ""))
            
            for pain_type in ["sharp", "dull", "throbbing"]:
                radio = tk.Radiobutton(
                    type_frame,
                    text=self.get_text(pain_type),
                    variable=type_var,
                    value=pain_type,
                    font=self.text_font,
                    bg="#f0f0f0",
                    command=lambda area=area, var=type_var: self.set_pain_type(area, var.get())
                )
                radio.pack(side=tk.LEFT, padx=10)
        
        # Add next button
        next_button = self.create_styled_button(
            details_frame,
            self.get_text("next"),
            self.proceed_to_doctor_selection,
            width=15,
            height=2
        )
        next_button.pack(pady=20)
    
    def set_pain_intensity(self, area, intensity):
        """Set pain intensity for a specific area"""
        self.current_patient["pain_intensity"][area] = intensity
    
    def set_pain_type(self, area, pain_type):
        """Set pain type for a specific area"""
        self.current_patient["pain_type"][area] = pain_type
    
    def proceed_to_doctor_selection(self):
        """Proceed to doctor selection if all pain details are provided"""
        # Check if all pain areas have intensity and type
        for area in self.current_patient["pain_areas"]:
            if area not in self.current_patient["pain_intensity"] or not self.current_patient["pain_intensity"][area]:
                messagebox.showerror("Error", f"Please select pain intensity for {self.get_text(area)}")
                return
            
            if area not in self.current_patient["pain_type"] or not self.current_patient["pain_type"][area]:
                messagebox.showerror("Error", f"Please select pain type for {self.get_text(area)}")
                return
        
        self.show_doctor_selection()
    
    def show_doctor_selection(self):
        """Show doctor selection screen"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("select_doctor"))
        
        # Create main content frame
        doctor_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        doctor_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Determine relevant specializations based on pain areas
        specializations = set()
        for area in self.current_patient["pain_areas"]:
            specializations.update(self.body_part_to_specialization.get(area, []))
        
        # Create a notebook for specializations
        notebook = ttk.Notebook(doctor_frame)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Add tabs for each specialization
        for specialization in specializations:
            # Create a frame for this specialization
            spec_frame = tk.Frame(notebook, bg="#f0f0f0", padx=20, pady=20)
            
            # Add to notebook
            notebook.add(spec_frame, text=self.get_text(specialization.lower().replace(" ", "_")))
            
            # Add doctors for this specialization
            for doctor in self.doctors.get(specialization, []):
                doctor_button = tk.Frame(
                    spec_frame,
                    bg="#ffffff",
                    relief=tk.RAISED,
                    borderwidth=1,
                    padx=10,
                    pady=10
                )
                doctor_button.pack(fill=tk.X, pady=5)
                
                # Top row: Name and Rating
                top_row = tk.Frame(doctor_button, bg="#ffffff")
                top_row.pack(fill=tk.X)
                
                name_label = tk.Label(
                    top_row,
                    text=doctor["name"],
                    font=self.header_font,
                    bg="#ffffff"
                )
                name_label.pack(side=tk.LEFT)
                
                rating_label = tk.Label(
                    top_row,
                    text=f"★ {doctor['rating']}",
                    font=self.text_font,
                    fg="#ff9900",
                    bg="#ffffff"
                )
                rating_label.pack(side=tk.RIGHT)
                
                # Bottom row: Specialization and Select button
                bottom_row = tk.Frame(doctor_button, bg="#ffffff")
                bottom_row.pack(fill=tk.X, pady=(5, 0))
                
                spec_label = tk.Label(
                    bottom_row,
                    text=doctor["specialization"],
                    font=self.text_font,
                    fg="#666666",
                    bg="#ffffff"
                )
                spec_label.pack(side=tk.LEFT)
                
                select_button = self.create_styled_button(
                    bottom_row,
                    "Select",
                    lambda d=doctor: self.select_doctor(d),
                    width=8,
                    height=1
                )
                select_button.pack(side=tk.RIGHT)
        
        # If the patient is existing, suggest previous doctors
        if not self.current_patient["is_new"]:
            # Get patient's visit history
            patient_id = self.current_patient["personal_details"]["patient_id"]
            visit_history = self.existing_patients.get(patient_id, {}).get("visit_history", [])
            
            if visit_history:
                # Create a frame for previous doctors
                prev_frame = tk.Frame(notebook, bg="#f0f0f0", padx=20, pady=20)
                notebook.add(prev_frame, text="Previous Doctors")
                
                # Add label
                label = tk.Label(
                    prev_frame,
                    text="Your previous doctors:",
                    font=self.header_font,
                    bg="#f0f0f0"
                )
                label.pack(anchor="w", pady=(0, 10))
                
                # Get unique doctors from visit history
                prev_doctors = set(visit["doctor"] for visit in visit_history)
                
                # Add previous doctors
                for doctor_name in prev_doctors:
                    # Find doctor in our database
                    doctor_obj = None
                    for spec, doctors in self.doctors.items():
                        for d in doctors:
                            if d["name"] == doctor_name:
                                doctor_obj = d
                                break
                    
                    if not doctor_obj:
                        continue
                    
                    # Create a button for this doctor
                    doctor_button = tk.Frame(
                        prev_frame,
                        bg="#e6f7ff",  # Highlight previous doctors
                        relief=tk.RAISED,
                        borderwidth=1,
                        padx=10,
                        pady=10
                    )
                    doctor_button.pack(fill=tk.X, pady=5)
                    
                    # Top row: Name and Rating
                    top_row = tk.Frame(doctor_button, bg="#e6f7ff")
                    top_row.pack(fill=tk.X)
                    
                    name_label = tk.Label(
                        top_row,
                        text=doctor_obj["name"],
                        font=self.header_font,
                        bg="#e6f7ff"
                    )
                    name_label.pack(side=tk.LEFT)
                    
                    rating_label = tk.Label(
                        top_row,
                        text=f"★ {doctor_obj['rating']}",
                        font=self.text_font,
                        fg="#ff9900",
                        bg="#e6f7ff"
                    )
                    rating_label.pack(side=tk.RIGHT)
                    
                    # Bottom row: Specialization and Select button
                    bottom_row = tk.Frame(doctor_button, bg="#e6f7ff")
                    bottom_row.pack(fill=tk.X, pady=(5, 0))
                    
                    spec_label = tk.Label(
                        bottom_row,
                        text=doctor_obj["specialization"],
                        font=self.text_font,
                        fg="#666666",
                        bg="#e6f7ff"
                    )
                    spec_label.pack(side=tk.LEFT)
                    
                    select_button = self.create_styled_button(
                        bottom_row,
                        "Select",
                        lambda d=doctor_obj: self.select_doctor(d),
                        width=8,
                        height=1
                    )
                    select_button.pack(side=tk.RIGHT)
    
    def select_doctor(self, doctor):
        """Select a doctor and proceed to appointment scheduling"""
        self.current_patient["selected_doctor"] = doctor
        self.show_appointment_scheduling()
    
    def show_appointment_scheduling(self):
        """Show appointment scheduling screen"""
        self.clear_frame(self.content_frame)
        self.create_header(self.get_text("schedule_appointment"))
        
        # Create main content frame
        schedule_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        schedule_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Add doctor info
        doctor = self.current_patient["selected_doctor"]
        
        doctor_info = tk.Frame(schedule_frame, bg="#ffffff", padx=15, pady=15, relief=tk.RAISED, borderwidth=1)
        doctor_info.pack(fill=tk.X, pady=10)
        
        doctor_name = tk.Label(
            doctor_info,
            text=doctor["name"],
            font=self.header_font,
            bg="#ffffff"
        )
        doctor_name.pack(anchor="w")