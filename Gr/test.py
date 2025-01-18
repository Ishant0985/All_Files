import os
import time
from datetime import datetime
from appium import webdriver
import subprocess
from urllib.parse import quote


def get_device_details():
    """Fetch connected device details using ADB."""
    # Get device name
    device_name = subprocess.getoutput("adb devices").splitlines()[1].split("\t")[0]

    # Get platform version
    platform_version = subprocess.getoutput("adb shell getprop ro.build.version.release").strip()

    return {
        "platformName": "Android",
        "platformVersion": platform_version,
        "deviceName": device_name
    }


def get_current_app_details():
    """Get the current app package and activity using ADB."""
    current_app = subprocess.getoutput("adb shell dumpsys window | grep mCurrentFocus")
    # Extract package and activity
    if "mCurrentFocus" in current_app:
        package_activity = current_app.split()[-1].strip("}").split("/")
        app_package = package_activity[0]
        app_activity = package_activity[1]
        return app_package, app_activity
    else:
        raise Exception("Unable to fetch app package and activity. Is WhatsApp running?")


def send_whatsapp_message_android(day, month, year, hour, minute, second, message, phone_number, max_retries=5):
    """
    Schedules and sends a WhatsApp message on an Android device using Appium.

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

            # Check if it's time to send the message
            if (current_datetime.day == day and current_datetime.month == month and
                    current_datetime.year == year and current_datetime.hour == hour and
                    current_datetime.minute == minute):
                
                # Encode the message for the WhatsApp URL
                encoded_message = quote(message)
                whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

                # Use adb to open WhatsApp with the URL
                print(f"Opening WhatsApp with message for {phone_number}...")
                adb_open_command = f"adb shell am start -a android.intent.action.VIEW -d '{whatsapp_url}'"
                os.system(adb_open_command)

                # Wait for WhatsApp to load
                time.sleep(5)

                # Initialize Appium driver for further actions
                device_details = get_device_details()
                desired_capabilities = {
                    "platformName": device_details["platformName"],
                    "platformVersion": device_details["platformVersion"],
                    "deviceName": device_details["deviceName"],
                    "appPackage": "com.whatsapp",  # WhatsApp package
                    "appActivity": "com.whatsapp.HomeActivity",
                    "noReset": True
                }

                driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
                driver.implicitly_wait(10)

                # Locate the "Send" button
                send_button = driver.find_element_by_accessibility_id("Send")

                # Click the "Send" button
                print("Clicking the Send button...")
                send_button.click()

                print("Message sent successfully!")
                driver.quit()
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


# Example Usage:
send_whatsapp_message_android(
    day=26, month=11, year=2024, hour=15, minute=30, second=0,
    message="Hello, this is a test message!", 
    phone_number="+1234567890"
)
