import logging
import random
import time

import config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    def navigate_to_target(self, target_account):
        logging.info(f"Navigating to {target_account}...")
        self.driver.get(f"{config.BASE_URL}/u/{target_account}/followers")

    def scroll_popup(self, popup):
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", popup
        )

    def get_popup_height(self):
        return self.driver.execute_script(
            "return document.querySelector('.followers-scroll').scrollHeight"
        )

    def follow_followers(self):
        while True:
            last_height = self.get_popup_height()

            rows = self.driver.find_elements(By.CLASS_NAME, "naan-follower-row")

            for row in rows:
                try:
                    button = row.find_element(By.CLASS_NAME, "naan-follow-btn")
                    meta = row.find_element(By.CLASS_NAME, "naan-meta").text
                    sub = row.find_element(By.CLASS_NAME, "naan-sub").text

                    if button.is_displayed() and button.text == "Follow":
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block: 'center'});",
                            button,
                        )
                        logger.info(
                            f"Clicked Follow button for Meta: {meta} and Sub: {sub}."
                        )
                        button.click()
                        time.sleep(random.uniform(2, 4))

                except Exception as e:
                    logger.exception(f"Failed to click Follow button: {e}")

            popup = self.driver.find_element(*config.MODAL)
            self.scroll_popup(popup)
            time.sleep(2)

            new_height = self.get_popup_height()

            if new_height == last_height:
                logger.info("Reached the end of the followers list.")
                break

    def unfollow_followers(self):
        while True:
            last_height = self.get_popup_height()

            rows = self.driver.find_elements(By.CLASS_NAME, "naan-follower-row")

            for row in rows:
                try:
                    button = row.find_element(By.CLASS_NAME, "naan-follow-btn")
                    meta = row.find_element(By.CLASS_NAME, "naan-meta").text
                    sub = row.find_element(By.CLASS_NAME, "naan-sub").text

                    if button.is_displayed() and button.text == "Following":
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block: 'center'});",
                            button,
                        )
                        logger.info(f"Unfollowing user: {meta} - {sub}")
                        button.click()
                        self.wait.until(
                            EC.element_to_be_clickable(config.UNFOLLOW_CONFIRM_BUTTON)
                        ).click()

                        time.sleep(random.uniform(2, 4))

                except Exception as e:
                    logger.exception(f"Failed to unfollow user {meta}: {e}")

            popup = self.driver.find_element(*config.MODAL)
            self.scroll_popup(popup)
            time.sleep(2)

            new_height = self.get_popup_height()

            if new_height == last_height:
                logger.info("Reached the end of the followers list.")
                break
