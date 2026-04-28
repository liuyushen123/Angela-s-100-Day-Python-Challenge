from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://secure-retreat-92358.herokuapp.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="form button")


first_name_input.send_keys("Yuchen")
last_name_input.send_keys("Liu")
email_input.send_keys("liuyushen123@gmail.com")
button.click()
