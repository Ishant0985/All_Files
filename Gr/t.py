from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed

# Target WhatsApp URL
phone_number = "+916307953956"
message = "Hello, how are you?"
url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"

# Open WhatsApp Web with the prefilled message
driver.get(url)
print("Trying to send message")
# Wait for WhatsApp Web to load
time.sleep(10)  # Adjust this as per your internet speed

# Click the Send button
try:
    
    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()
    print("Message sent successfully!")
except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
