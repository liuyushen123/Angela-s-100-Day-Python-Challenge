import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = "liuyushen123@gmail.com"
PASSWORD = "67iLoveBoobs69"

URL = "https://sachaavogel.github.io/mock-tinder/"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url=URL)

login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/button"))
)
login_btn.click()

facebook_login_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login-screen"]/div/div/div/div/span/div/button')
    )
)
facebook_login_btn.click()

main_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]

driver.switch_to.window(facebook_window)

email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
password_input = wait.until(EC.presence_of_element_located((By.ID, "pass")))


email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "login_button")))

submit_btn.click()

driver.switch_to.window(main_window)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loc-step"]/button'))).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/button"))
).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cookie-banner"]/div/button'))
).click()

for i in range(10):
    match_popups = driver.find_elements(By.XPATH, '//*[@id="match-popup"]/a')
    if match_popups and match_popups[0].is_displayed():
        print("发现匹配窗口，点击关闭...")
        wait.until(EC.element_to_be_clickable(match_popups[0])).click()

    else:
        try:
            like_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="content"]/div[3]/div/div/div/div/button')
                )
            )
            like_btn.click()
            print(f"执行了第 {i + 1} 次点赞")
            time.sleep(0.5)
        except Exception as e:
            print(f"点赞按钮暂未出现或不可用: {e}")


time.sleep(3)
driver.quit()
