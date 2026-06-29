import time

from config import DATA_ENTRY_FORM_URL
from driver_setup import create_driver
from pages.form_page import FormPage
from pages.zillow_page import ZillowPage

driver = create_driver()

zillow_bot = ZillowPage()
properties = zillow_bot.get_properties()

form_bot = FormPage(driver)
print(len(properties))

for index, property in enumerate(properties):
    driver.get(DATA_ENTRY_FORM_URL)
    print(f"Processing property {index + 1}/{len(properties)}...")
    try:
        form_bot.submit_property(
            property["address"], property["price"], property["link"]
        )
    except Exception as e:
        print(f"Failed to submit property {index + 1}, skipping. Error: {e}")
        continue
    finally:
        time.sleep(2)
