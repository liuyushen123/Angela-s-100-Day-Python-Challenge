from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 67)

    # ---       (Helper Functions)   ---
    def send_keys_to_element(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))

            element.clear()

            element.send_keys(text)
        except TimeoutException:
            print(f"Error: Timed out waiting for input field {locator}")
            self.driver.save_screenshot("input_timeout.png")
        except Exception as e:
            print(f"An unexpected error occurred while sending keys: {e}")

    def click_element(self, locator):

        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

        except TimeoutException:
            print("Error: The page loaded too slowly or elements were not found.")
            self.driver.save_screenshot("login_timeout_error.png")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
