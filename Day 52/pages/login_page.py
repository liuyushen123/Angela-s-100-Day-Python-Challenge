import logging

import config
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    def login(self, username, password):
        logger.info("Navigating to login page...")
        self.driver.get(f"{config.BASE_URL}/login")

        self.send_keys_to_element(config.USERNAME_FIELD, username)
        self.send_keys_to_element(config.PASSWORD_FIELD, password)
        self.click_element(config.LOGIN_BUTTON)

        try:
            self.wait.until(EC.presence_of_element_located(config.NAAN_PAGE))
            logger.info("Successfully Logged In")
        except TimeoutException:
            logger.error("Login verification failed: Dashboard element not found.")
            self.save_screenshot("login_verification_failure")
            raise ConnectionError("Login failed: Could not reach dashboard.")
