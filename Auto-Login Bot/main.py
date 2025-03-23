from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

def setup_logger():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def start_bot(username, password, url):
    """
    Automates login for a given website using Selenium with improved error handling and dynamic waits.

    :param username: Login username
    :param password: Login password
    :param url: URL of the login page
    """
    if not all([username, password, url]):
        logging.error("Missing required parameters. Please provide username, password, and URL.")
        return

    try:
        setup_logger()
        
        options = Options()
        # Uncomment for debugging (runs with UI)
        # options.add_argument("--headless")  
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        
        logging.info("Opening login page...")
        driver.get(url)
        
        wait = WebDriverWait(driver, 10)
        
        # Locate and fill the username field
        try:
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))  # Check correct attribute
            username_field.send_keys(username)
        except Exception:
            logging.error("Username field not found!")
            return
        
        # Locate and fill the password field
        try:
            password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))  # Check correct attribute
            password_field.send_keys(password)
        except Exception:
            logging.error("Password field not found!")
            return

        # Locate and click the login button
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-button")))  # Check correct selector
            login_button.click()
        except Exception:
            logging.error("Login button not found or not clickable!")
            return
        
        logging.info("Login attempted successfully.")
        
        # Optional: Check for successful login indicator
        time.sleep(3)  # Adjust time as needed

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        logging.info("Browser closed.")

# Driver Code
if __name__ == "__main__":
    USERNAME = "your_username"
    PASSWORD = "your_password"
    URL = "https://https://example.com//login"
    
    start_bot(USERNAME, PASSWORD, URL)
