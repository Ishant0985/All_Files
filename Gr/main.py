import subprocess
import sys
import os

# Function to install a module if it's not already installed
def install_and_import(package):
    try:
        __import__(package)  # Try importing the package
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])  # Install the package
        print(f"{package} has been installed successfully.")
    finally:
        globals()[package] = __import__(package)  # Import the module dynamically after installation

# Check and install required modules
required_modules = ["pywhatkit",]
for module in required_modules:
    install_and_import(module)

# Import pywhatkit after ensuring installation and datetime
import time
from datetime import datetime
import pywhatkit as kit


def send_whatsapp_message(day, month, year, hour, minute, second, message, phone_number, max_retries=5):
    """
    Schedules and sends a WhatsApp message using pywhatkit.

    Args:
        day (int): Day for the scheduled message.
        month (int): Month for the scheduled message.
        year (int): Year for the scheduled message.
        hour (int): Hour (24-hour format) for the scheduled message.
        minute (int): Minute for the scheduled message.
        second (int): Second (ignored for scheduling).
        message (str): The message to send.
        phone_number (str): The recipient's phone number in "+<country_code><number>" format.
        max_retries (int): Maximum retries in case of failures.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Get the current time
            current_datetime = datetime.now()
            
            # Extract current date and time
            h = current_datetime.hour
            m = current_datetime.minute
            s = current_datetime.second
            d = current_datetime.day
            mon = current_datetime.month
            y = current_datetime.year

            # Check if it's time to send the message
            if (d == day and mon == month and y == year and h == hour and m == minute):

                # Add a small buffer time for sending the message
                send_m = (minute + 2) % 60  # Add 2 minutes buffer
                send_h = hour + ((minute + 2) // 60)  # Increment hour if minute overflows
                send_h %= 24  # Ensure hour stays within 0-23

                print(f"Scheduling message to {phone_number} at {send_h}:{send_m}...")
                kit.sendwhatmsg(phone_number, message, send_h, send_m, wait_time=30)  # Wait time for loading
                print("Message sent successfully!")
                return True
            else:
                print("Waiting for the scheduled time...")
                time.sleep(10)  # Check every 10 seconds
        except Exception as e:
            retry_count += 1
            print(f"Error encountered: {e}. Retrying... ({retry_count}/{max_retries})")
            time.sleep(10)  # Wait before retrying

    print("Failed to send the message after maximum retries.")
    return False


# Example usage
# if __name__ == "__main__":
#     # Replace with actual details
#     send_whatsapp_message(24, 11, 2024, 11, 21, 0, 
#                           "Hello! This is a scheduled message.", 
#                           "+919450862805")
