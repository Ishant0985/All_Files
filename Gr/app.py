import pywhatkit as kit
import schedule
import time

def send_whatsapp_message(phone_number, message):
    """
    Sends a WhatsApp message using PyWhatKit.
    """
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=40)
    print(f"Message sent to {phone_number}: {message}")

# Schedule the message
print("Scheduling Task")
schedule.every().day.at("06:58").do(send_whatsapp_message, "+916307953956", "Hello, How are you? How was your picnic?")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(2)