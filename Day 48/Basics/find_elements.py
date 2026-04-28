from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

seaarch_bar = driver.find_element(By.NAME, value="q")
submit_button = driver.find_element(By.ID, value="submit")

documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a"
)
print(documentation_link)


driver.quit()
