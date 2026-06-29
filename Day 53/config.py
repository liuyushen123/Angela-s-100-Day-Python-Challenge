from selenium.webdriver.common.by import By

DATA_ENTRY_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdQLnoS8VBtw6Oz47CWEXIE_4qY65UDryue9TpjJk7nnntUHA/viewform"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

ADDRESS_INPUT = (
    By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
)

PRICE_INPUT = (
    By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
)

LINK_INPUT = (
    By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
)

BUTTON = (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
