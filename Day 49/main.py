import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

base_dir = os.path.dirname(os.path.abspath(__file__))
user_data_dir = os.path.join(base_dir, "selenium_profile")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 10)


def register_account(name, email, password):
    if not name or not email or not password:
        print("Missing input")
        return

    # Join button
    join_btn = wait.until(
        ec.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3"))
    )
    join_btn.click()

    # Switch to register
    register_btn = wait.until(
        ec.element_to_be_clickable((By.CLASS_NAME, "Login_toggleButton___tVY8"))
    )
    register_btn.click()

    # Inputs
    name_input = wait.until(ec.presence_of_element_located((By.ID, "name-input")))
    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    password_input = wait.until(
        ec.presence_of_element_located((By.ID, "password-input"))
    )

    name_input.send_keys(name)
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Submit
    register = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
    register.click()


def login(email="liuyushen123@gmail.com", password="liuyushen"):
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    password_input = wait.until(
        ec.presence_of_element_located((By.ID, "password-input"))
    )
    email_input.clear()
    email_input.send_keys(email)

    password_input.clear()
    password_input.send_keys(password)

    hit_login = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
    hit_login.click()


login()
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

all_cards = wait.until(
    ec.presence_of_all_elements_located((By.CLASS_NAME, "Schedule_dayGroup__y79__"))
)

booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []

for day_card in all_cards:
    day_header = day_card.find_element(By.TAG_NAME, "h2").text

    if "Thu" in day_header or "Fri" in day_header:
        class_cards = day_card.find_elements(
            By.CSS_SELECTOR,
            value=".ClassCard_card__KpCx5 .ClassCard_cardContent__WGvPp",
        )

        for class_card in class_cards:
            class_name_element = class_card.find_element(By.TAG_NAME, value="h3").text
            class_time_element = class_card.find_element(
                By.CLASS_NAME, value="ClassCard_classDetail__Z8Z8f"
            ).text.split(" ")
            class_book_btn = class_card.find_element(By.XPATH, "..").find_element(
                By.TAG_NAME, value="button"
            )
            class_info = f"{class_name_element} on {day_header}"

            if class_book_btn.text == "Booked":
                already_booked_count += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif class_book_btn.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif class_book_btn.text == "Book Class":
                class_book_btn.click()
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")
                class_book_btn.click()
                time.sleep(0.5)
            elif class_book_btn.text == "Join Waitlist":
                class_book_btn.click()
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                class_book_btn.click()
                time.sleep(0.5)
            print(class_name_element)

print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(
    f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}"
)

# Print detailed class list
print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")


total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0


all_my_bookings = driver.find_elements(
    By.CSS_SELECTOR, value=".MyBookings_section__oBwNg"
)


for my_sections in all_my_bookings:
    try:
        my_sections_array = my_sections.find_elements(
            By.CLASS_NAME, value="MyBookings_bookingCard__VRdrR"
        )

        for my_cards in my_sections_array:
            class_name = my_cards.find_element(By.TAG_NAME, "h3").text
            print(class_name)
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        print("Can't not find this element!")
        continue

print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
