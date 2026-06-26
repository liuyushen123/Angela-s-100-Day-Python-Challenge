import logging

import config
from driver_setup import create_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("Day 52/logs/naan_bot.log"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("WDM").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

driver = create_driver()
login_bot = LoginPage(driver)
homepage_bot = HomePage(driver)


try:
    login_bot.login("liuyushen123@gmail.com", "tPqc3x_yLi5QbmGQ")
    response = input("Would you like to follow(y) or unfollow(n)? (y/n)").lower()
    action = (
        homepage_bot.follow_followers
        if response == "y"
        else homepage_bot.unfollow_followers
    )

    for account in config.SIMILAR_ACCOUNTS:
        logger.info(f"Processing {account}")
        homepage_bot.navigate_to_target(account)
        action()
except Exception:
    logger.exception("An unexpected error occurred")

except KeyboardInterrupt:
    logger.info("Program interrupted by user.")

finally:
    logger.info("Closing browser...")
    driver.quit()
