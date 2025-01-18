from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess

class AI_Assistant(App):
    def build(self):
        self.engine = pyttsx3.init()
        
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="AI Assistant", font_size=24)
        layout.add_widget(self.label)
        
        self.text_input = TextInput(font_size=18, size_hint_y=None, height=150)
        layout.add_widget(self.text_input)
        
        self.listen_button = Button(text="Listen", font_size=18, on_press=self.listen)
        layout.add_widget(self.listen_button)
        
        self.commands = {
            "open google": self.open_google,
            "turn on the light": self.turn_on_light,
            "turn off the light": self.turn_off_light,
            "login": self.login,
            "open": self.open_application,
            "settings": self.open_settings,
            "make a call": self.make_call
        }
        
        return layout
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self, instance):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            self.text_input.text += f"You said: {command}\n"
            self.execute_command(command)
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that.")
        except sr.RequestError:
            self.speak("Could not request results; check your network connection.")
    
    def execute_command(self, command):
        for key in self.commands:
            if key in command:
                self.commands[key](command)
                return
        self.speak("Sorry, I don't know how to do that.")
    
    def open_google(self, command=None):
        self.speak("Opening Google")
        webbrowser.open("http://www.google.com")
    
    def turn_on_light(self, command=None):
        # Placeholder for actual smart home light control
        self.speak("Turning on the light")
    
    def turn_off_light(self, command=None):
        # Placeholder for actual smart home light control
        self.speak("Turning off the light")
    
    def login(self, command=None):
        self.speak("Logging in")
        # Placeholder for actual login logic
    
    def open_application(self, command):
        app_name = command.replace('open', '').strip()
        self.speak(f"Opening {app_name}")
        try:
            if os.name == 'posix':
                subprocess.call(['open', '-a', app_name])
            elif os.name == 'nt':
                os.system(f'start {app_name}')
            else:
                self.speak("Unsupported operating system")
        except Exception as e:
            self.speak(f"Could not open {app_name}. Please try again.")
    
    def open_settings(self, command=None):
        self.speak("Opening settings")
        try:
            if os.name == 'posix':
                os.system("open /System/Library/PreferencePanes")
            elif os.name == 'nt':
                os.system("start ms-settings:")
            else:
                self.speak("Unsupported operating system")
        except Exception as e:
            self.speak("Could not open settings. Please try again.")
    
    def make_call(self, command):
        self.speak("Making a call")
        phone_number = command.replace('make a call to', '').strip()
        # Placeholder for actual calling logic; this requires a phone service API or similar
        # Example using pywhatkit for WhatsApp calls
        # import pywhatkit as kit
        # kit.sendwhatmsg_instantly(phone_number, "Hi", wait_time=10)
        self.speak(f"Calling {phone_number} is not implemented in this example")

if __name__ == "__main__":
    AI_Assistant().run()
