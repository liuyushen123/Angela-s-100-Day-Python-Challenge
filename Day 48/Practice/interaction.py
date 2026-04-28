from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num = driver.find_element(By.CSS_SELECTOR, value=".mp-box #articlecount li a")

print(f"There are {num.text} active editors!")

driver.quit()
