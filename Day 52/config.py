# config.py
from selenium.webdriver.common.by import By

# 使用元组，方便后续调用: driver.find_element(*USERNAME_FIELD)
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
USERNAME_FIELD = (
    By.XPATH,
    '//input[contains(@placeholder, "Phone number, username, or email")]',
)
PASSWORD_FIELD = (By.XPATH, '//input[contains(@placeholder, "Password")]')
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in')]")
NAAN_PAGE = (By.CLASS_NAME, "naan-page")
MODAL = (By.CSS_SELECTOR, ".followers-scroll")
SIMILAR_ACCOUNTS = ["chefsteps", "rordongamsay", "elaineducasse"]
UNFOLLOW_CONFIRM_BUTTON = (
    By.XPATH,
    "//button[contains(text(), 'Unfollow')]",
)
