import os
import datetime
import threading
from tkinter import Tk, Button, Label
import pywhatkit as kit
from questions import open_response
from sites import open_site
from speech import say
from chatbot import chat, chat_history
from gptai import ai
from programs import open_program
from micinput import takeCommand


class BharatAI:
    def __init__(self):
        # Initialize the application
        self.root = Tk()
        self.root.title("Bharat AI Assistant")
        self.root.geometry("400x400")
        self.root.attributes("-topmost", True)  # Stay on top of other windows
        self.root.configure(bg="#222")

        # State Variables
        self.text_visible = True  # Tracks output visibility
        self.active = True  # Tracks if the assistant is active

        # UI Components
        self.mic_btn = Button(
            self.root,
            text="🎤",
            font=("Arial", 30),
            command=self.activate_microphone,
            bg="#333",
            fg="#fff",
            activebackground="#444",
            activeforeground="#0f0"
        )
        self.mic_btn.pack(pady=50)

        self.hamburger_btn = Button(
            self.root,
            text="☰",
            font=("Arial", 20),
            command=self.show_folders,
            bg="#333",
            fg="#fff",
            activebackground="#444",
            activeforeground="#ff0"
        )
        self.hamburger_btn.pack(side="top", anchor="w", padx=10)

        self.eye_btn = Button(
            self.root,
            text="👁️",
            font=("Arial", 20),
            command=self.toggle_text_visibility,
            bg="#333",
            fg="#fff",
            activebackground="#444",
            activeforeground="#f00"
        )
        self.eye_btn.pack(side="top", anchor="e", padx=10)

        self.output_label = Label(
            self.root,
            text="",
            font=("Arial", 14),
            fg="#fff",
            bg="#222",
            wraplength=380,
            justify="left"
        )
        self.output_label.pack(pady=20)

        # Start background thread for wake-word detection
        self.wake_word_thread = threading.Thread(target=self.listen_for_wake_word, daemon=True)
        self.wake_word_thread.start()

    def activate_microphone(self):
        """Handles microphone activation and processes commands."""
        self.mic_btn.config(text="🎤...")  # Indicate listening
        say("Listening...")
        query = takeCommand()

        if query:
            self.process_query(query)

        self.mic_btn.config(text="✔️")  # Indicate completion

    def listen_for_wake_word(self):
        """Continuously listens for wake words in the background."""
        while self.active:
            try:
                query = takeCommand().lower()  # Continuously listen for commands
                if "bharat" in query or "hey bharat" in query:
                    self.activate_microphone()
            except Exception as e:
                print(f"Error in wake-word detection: {e}")

    def process_query(self, query):
        """Processes the user's query and routes to appropriate functions."""
        try:
            if "time" in query:
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                response = f"The time is {hour} hours and {minute} minutes."
                say(response)
                self.update_output(response)

            elif "date" in query:
                date = datetime.datetime.now().strftime("%d %B %Y")
                response = f"Today's date is {date}."
                say(response)
                self.update_output(response)

            elif "day" in query:
                day = datetime.datetime.now().strftime("%A")
                response = f"Today is {day}."
                say(response)
                self.update_output(response)

            elif "shutdown" in query:
                say("Shutting down the system.")
                kit.shutdown()

            elif "cancel shutdown" in query:
                say("Cancelling shutdown.")
                kit.cancel_shutdown()

            elif "screenshot" in query:
                screenshot_path = f"Screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                if not os.path.exists("Screenshots"):
                    os.mkdir("Screenshots")
                kit.take_screenshot(screenshot_path)
                response = f"Screenshot saved at {screenshot_path}."
                say(response)
                self.update_output(response)

            elif "ai" in query:
                response = ai(prompt=query)
                say(response)
                self.update_output(response)

            elif "reset chat" in query:
                global chat_history
                chat_history = ""
                response = "Chat history reset."
                say(response)
                self.update_output(response)

            elif "show chat history" in query:
                response = f"Chat History:\n{chat_history}"
                say("Showing chat history.")
                self.update_output(response)

            elif "quit" in query:
                say("Goodbye! Have a great day.")
                self.active = False  # Stop wake-word detection
                self.root.quit()

            else:
                say("Processing your request.")
                chat_response = chat(query)
                self.update_output(chat_response)

            open_site(query)
            open_program(query)
            open_response(query)

        except Exception as e:
            error_message = f"An error occurred: {e}"
            self.update_output(error_message)
            say(error_message)

    def update_output(self, text):
        """Updates the output label with given text."""
        self.output_label.config(text=text)

    def toggle_text_visibility(self):
        """Toggles the visibility of the output label."""
        if self.text_visible:
            self.output_label.pack_forget()
        else:
            self.output_label.pack()
        self.text_visible = not self.text_visible

    def show_folders(self):
        """Displays folders created by Bharat AI."""
        folders = "\n".join(os.listdir("."))
        self.update_output(f"Folders:\n{folders}")

    def run(self):
        """Runs the Bharat AI application."""
        self.root.mainloop()


if __name__ == "__main__":
    print("running bharat ai")
    app = BharatAI()
    app.run()
