from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def start_bot(username, password, url):
    """
    Automates login for a given website using Selenium.

    :param username: Login username
    :param password: Login password
    :param url: URL of the login page
    """
    if not all([username, password, url]):
        print("Error: Missing required parameters. Please provide username, password, and URL.")
        return

    try:
        # Use webdriver_manager to automatically handle ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open the login page
        driver.get(url)

        # Locate and fill the username field
        username_field = driver.find_element(By.NAME, "username")  # Update "username" to the actual field name
        username_field.send_keys(username)

        # Locate and fill the password field
        password_field = driver.find_element(By.NAME, "password")  # Update "password" to the actual field name
        password_field.send_keys(password)

        # Locate and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".login-button")  # Update ".login-button" with the actual CSS selector
        login_button.click()

        print("Login attempted. Check browser for the result.")
        time.sleep(5)  # Wait to observe the result

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

# Driver Code
if __name__ == "__main__":
    # Replace with your login details and website information
    USERNAME = "your_username"
    PASSWORD = "your_password"
    URL = "https://example.com/login"

    # Call the function
    start_bot(USERNAME, PASSWORD, URL)
