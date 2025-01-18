import speech_recognition as sr
import os
import webbrowser
import openai # type: ignore
import datetime
import pyttsx3
import logging
import pywhatkit as kit

# Load your OpenAI API key
from config import apikey

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)

# Logger setup
logging.basicConfig(filename="bharat_ai.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Global Variables
name = "Ishant"
chat_history = ""

# Function to speak text
def say(text):
    """Convert text to speech."""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logging.error(f"Error in say function: {e}")

# Function to handle ChatGPT interactions
def chat(query):
    global chat_history
    openai.api_key = apikey
    chat_history += f"{name}: {query}\nBharat: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chat_history,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        message = response["choices"][0]["text"].strip()
        say(message)
        chat_history += f"{message}\n"
        return message
    except Exception as e:
        logging.error(f"Error during ChatGPT API call: {e}")
        say("I am sorry, there was an error connecting to the AI service.")
        return "Error connecting to AI service."

# Function to generate AI response and save to a file
def ai(prompt):
    openai.api_key = apikey
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = response["choices"][0]["text"].strip()
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        filename = f"Openai/{prompt[:50].replace(' ', '_')}.txt"
        with open(filename, "w") as file:
            file.write(f"Prompt: {prompt}\n\n{text}")
        say("The response has been saved.")
    except Exception as e:
        logging.error(f"Error in AI function: {e}")
        say("I am sorry, there was an error completing the task.")

# Function to recognize voice input using Google Web Speech API
def take_command():
    """Recognize voice input using Google Web Speech API."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        query = recognizer.recognize_google(audio)  # Using Google Web Speech API
        print(f"User said: {query}")
        logging.info(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        say("Sorry, I didn't understand that. Please repeat.")
        logging.warning("Speech recognition could not understand the audio.")
        return ""
    except sr.RequestError as error:
        logging.error(f"Speech recognition service error: {error}")
        say("Speech recognition service is unavailable.")
        return ""
    except Exception as error:
        logging.error(f"Unexpected error in take_command: {error}")
        say("An error occurred while processing your voice. Please try again.")
        return ""

# Main Functionality
if __name__ == '__main__':
    say("Welcome to Bharat A.I.")
    while True:
        query = take_command()
        if not query:
            continue

        # Predefined sites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["github", "https://www.github.com"],
            ["instagram", "https://www.instagram.com"],
            ["x", "https://www.x.com"],
            ["twitter", "https://www.twitter.com"],
            ["facebook", "https://www.facebook.com"]
        ]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
                break

        # Play music or YouTube videos
        if "play" in query:
            song = query.replace("play", "").strip()
            say(f"Playing {song} on YouTube.")
            kit.playonyt(song)

        # Time Query
        elif "the time" in query:
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M")
            say(f"The time is {time_str}")

        # Chat mode
        elif "let's chat" in query or "start chat" in query:
            say("Sure, let's start chatting.")
            chat(query)

        # Exit command
        elif "quit" in query or "exit" in query:
            say("Goodbye! Have a great day.")
            break

        # AI and Chat
        elif "using artificial intelligence" in query:
            ai(query)

        elif "reset chat" in query:
            chat_history = ""
            say("Chat history has been reset.")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            say("Shutting down the system.")

        elif "cancel shutdown" in query:
            os.system("shutdown /a")
            say("Shutdown canceled.")

        else:
            say("I am not sure how to handle that. Please try something else.")
