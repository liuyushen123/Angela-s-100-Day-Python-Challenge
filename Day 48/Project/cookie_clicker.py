import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

URL = "https://ozh.github.io/cookieclicker/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


time.sleep(3)

try:
    language_menu = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
    print("Found language button, clicking...")
    language_menu.click()
    time.sleep(3)
except NoSuchElementException:
    print("Language selection not found")
finally:
    time.sleep(3)


cookie = driver.find_element(By.ID, value="bigCookie")
best_price = -1
timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        prodcuts = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked")

        for product in prodcuts:
            price_text = product.find_element(By.CLASS_NAME, "price").text
            price_number = int(price_text.replace(",", ""))
            print(price_number)
            if best_price < price_number:
                best_product = product.get_attribute("ID")
                best_price = price_number
            print(best_product)

        driver.find_element(By.ID, value=best_product).click()

        timeout = time.time() + 5
