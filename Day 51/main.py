import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = "32923146@nebraska.edu"
PASSWORD = "MC5na1qNlRgnoe2B"
PROMISED_DOWN = 1000
PROMISED_UP = 1000
URL = "https://app.100daysofpython.dev/services/y"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        self.url = "https://www.speedtest.net/"
        self.wait = WebDriverWait(self.driver, 60)

    def get_internet_speed(self):
        self.driver.get(self.url)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
        ).click()

        time.sleep(60)

        print("Getting ready to pull the data")

        time.sleep(3)

        self.down = float(
            self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "download-speed"))
            ).text
        )

        self.up = float(
            self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed"))
            ).text
        )

        print(f"Down: {self.down}")
        print(f"Up: {self.up}")
        time.sleep(3)

    def tweet_at_provider(self):
        tweet_compose = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/nav/button"
        )
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            tweet = f"Hey my internet provider, I’m seeing {self.down} down / {self.up} up, but I pay for {PROMISED_DOWN}/{PROMISED_UP}. Can you help?"
        else:
            tweet = f"Hey my internet provider, my speed is great! Hitting {self.down} down / {self.up} up as promised. Thanks!"
        tweet_compose.send_keys(tweet)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="modal-post-btn"]')
        tweet_button.click()

        time.sleep(2)

        input()

        self.driver.quit()

    # Navigating page
    def run_automation(self):
        try:
            # Navigation
            self.driver.get(URL)
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), 'Log in')]")
                )
            ).click()

            # Login
            email_input = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//input[contains(@placeholder, "Email")]')
                )
            )
            email_input.send_keys(EMAIL)

            self.driver.find_element(
                By.XPATH, '//input[contains(@placeholder, "Password")]'
            ).send_keys(PASSWORD)

            self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Log in')]"
            ).click()
            print("Login complete.")

        except Exception as e:
            print(f"An error occurred: {e}")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.run_automation()
bot.tweet_at_provider()
