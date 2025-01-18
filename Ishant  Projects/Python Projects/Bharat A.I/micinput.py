import speech_recognition as sr

from speech import say

def takeCommand():
    """Capture voice input and recognize it as text with improved settings for built-in microphones."""
    r = sr.Recognizer()

    # Dynamic energy threshold adjustment enabled
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=5)  # Longer duration for noisy environments
            print("Listening...")

            # Listen with a timeout and phrase time limit, but wait for pause in speech
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Longer phrase_time_limit to capture full sentences
            print("Recognizing...")

            # Attempt to recognize speech
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query

        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            say("No speech detected. Please try again.")

        except sr.UnknownValueError:
            print("Speech was unclear. Please speak more clearly.")
            say ("Speech was unclear. Please speak more clearly.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            say( "Sorry, there was a network error.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            say(f"An unexpected error occurred: {e}")    
