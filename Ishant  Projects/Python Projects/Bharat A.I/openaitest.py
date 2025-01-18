import os
import datetime
import requests
from transformers import pipeline
import pywhatkit as kit
from questions import open_response
from sites import open_site
from speech import say
from chatbot import chat, chat_history
from gptai import ai
from programs import open_program
from micinput import takeCommand

# Load lightweight NLP model (DistilBERT)
nlp = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")


def get_weather():
    """Fetch and return the current weather condition using Open-Meteo."""
    try:
        # Get the current location using IP
        location_response = requests.get("http://ip-api.com/json/").json()
        latitude = location_response.get("lat")
        longitude = location_response.get("lon")
        city = location_response.get("city", "Unknown location")
        country = location_response.get("country", "Unknown country")
        
        if not latitude or not longitude:
            say("Sorry, I couldn't determine your current location.")
            return
        
        # Fetch weather data from Open-Meteo
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url).json()
        
        if "current_weather" not in weather_response:
            say("Sorry, I couldn't fetch the weather at the moment.")
            return

        # Extract weather details
        weather_data = weather_response["current_weather"]
        temperature = weather_data["temperature"]
        weather_description = weather_data.get("weathercode", "Clear")  # Adjust for simplicity

        say(f"The current weather in {city}, {country} is {weather_description} with a temperature of {temperature} degrees Celsius.")
    except Exception as e:
        say("I couldn't fetch the weather due to an error.")
        print(f"Error fetching weather: {e}")


def handle_time_commands(query):
    """Handle time-related commands like time, date, and day."""
    if "time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        say(f"Sir, the time is {hour} hours and {minute} minutes.")
    elif "date" in query:
        dt = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%B")
        year = datetime.datetime.now().strftime("%Y")
        say(f"Today's date is {dt} {month} {year}.")
    elif "day" in query:
        day = datetime.datetime.now().strftime("%A")
        say(f"Today is {day}.")


def handle_screenshot():
    """Take and save a screenshot in the 'Screenshots' directory."""
    try:
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
            say("Created a folder named 'Screenshots' for saving your screenshots.")
        
        screenshot_path = f"Screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        kit.take_screenshot(screenshot_path)
        say("Screenshot captured and saved.")
    except Exception as e:
        say("Failed to take a screenshot.")
        print(f"Screenshot Error: {e}")


def handle_query_with_nlp(query):
    """Process query using NLP for better intent understanding."""
    # Define possible tasks
    candidate_labels = [
        "weather",
        "play music",
        "time",
        "date",
        "day",
        "shutdown",
        "cancel shutdown",
        "take screenshot",
        "chat",
        "reset chat history",
        "show chat history",
        "open site",
        "ai",
        "quit",
    ]
    
    # Classify the query
    nlp_result = nlp(query, candidate_labels)
    intent = nlp_result["labels"][0]
    confidence = nlp_result["scores"][0]  # Confidence score for accuracy checks
    
    if confidence < 0.70:
        say("Sorry, I couldn't understand your request clearly. Could you please repeat?")
        return

    # Map intents to actions
    if intent == "weather":
        get_weather()
    elif intent == "play music":
        say("Playing music. Please specify your preference next time.")
    elif intent in ["time", "date", "day"]:
        handle_time_commands(query)
    elif intent == "shutdown":
        try:
            say("Shutting down the system, sir.")
            kit.shutdown()
        except Exception as e:
            say("An error occurred while shutting down.")
            print(f"Error: {e}")
    elif intent == "cancel shutdown":
        try:
            say("Cancelling the shutdown, sir.")
            kit.cancel_shutdown()
        except Exception as e:
            say("Unable to cancel the shutdown.")
            print(f"Error: {e}")
    elif intent == "take screenshot":
        handle_screenshot()
    elif intent == "ai":
        ai(prompt=query)
    elif intent == "reset chat history":
        say("Resetting chat history.")
        global chat_history
        chat_history = ""
    elif intent == "show chat history":
        say("Showing chat history.")
        print(chat_history)
    elif intent == "open site":
        open_site(query)
    elif intent == "questions":
        open_response(query)
    elif intent == "open program":
        open_program(query)
    elif intent == "chat":
        say("Let's chat. Say 'exit chat' to quit.")
        while True:
            sub_query = takeCommand().lower()
            if any(cmd in sub_query for cmd in ["exit chat", "quit chat", "cancel chat", "quit"]):
                break
            chat(query=sub_query)
    elif intent == "quit":
        say("Goodbye! Have a great day.")
        exit(0)  # Exit application


def main():
    """Main loop for Bharat AI."""
    print("Welcome to Bharat AI")
    say("Welcome to Bharat AI.")

    while True:
        print("Listening...")
        q = takeCommand()
        query = q.lower()
        
        # Process the query with advanced NLP
        handle_query_with_nlp(query)


if __name__ == '__main__':
    main()
