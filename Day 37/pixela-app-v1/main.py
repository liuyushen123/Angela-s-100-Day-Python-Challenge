import datetime as dt
import json
import os
import webbrowser

import requests
from dotenv import load_dotenv


class PixelaApp:
    def __init__(self):
        load_dotenv()
        self.today = dt.datetime.now().strftime("%Y%m%d")
        self.today_formatted = dt.datetime.now().strftime("%Y-%m-%d")
        self.token = os.getenv("PIXEL_TOKEN")
        self.user_name = os.getenv("USER_NAME")
        self.graph_id = "graph"
        self.base_url = "https://pixe.la/v1/users"
        self.graph_url = f"{self.base_url}/{self.user_name}/graphs/{self.graph_id}"
        self.headers = {"X-USER-TOKEN": self.token}
        self.menu_options = {
            "1": self.log_today,
            "2": self.update_pixel,
            "3": self.delete_pixel,
            "4": self.view_graph,
            "5": self.exit_app,
        }

    def view_graph(self):
        url = self.graph_url + ".html"
        webbrowser.open(url, new=2)

    def get_optional_data(self):

        study_notes = input("How was the studying today?: ")

        return {"notes": study_notes.title() if study_notes else "No notes today"}

    def pixel_exists(self, date):
        url = f"{self.graph_url}/{date}"

        try:
            response = requests.get(url=url, headers=self.headers, timeout=5)

            if response.status_code == 200:
                return True
            elif response.status_code == 404:
                return False
            else:
                response.raise_for_status()

        except requests.RequestException as e:
            print(f"Network error: {e}")
            return False

    def get_date(self):
        while True:
            date = input("Enter date (YYYYMMDD)")
            try:
                dt.datetime.strptime(date, "%Y%m%d")
                return date
            except ValueError:
                print("Please input in a format of YYYYMMDD")

    def log_today(self):
        print(f"\n--- 打卡今日 ({self.today_formatted}) ---")
        if self.pixel_exists(self.today):
            print("This pixel already exists! Try again tomorrow or use Update.")
            return

        params = {
            "date": self.today,
            "quantity": self.get_quantity(),
            "optionalData": json.dumps(self.get_optional_data()),
        }

        response = requests.post(
            url=self.graph_url, headers=self.headers, json=params, timeout=5
        )
        print(response.text)
        response.raise_for_status()

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("How many minutes have you coded today?: "))
                break
            except ValueError:
                print("Not a valid input ")
        return str(quantity)

    def update_pixel(self):
        date = self.get_date()
        url = f"{self.graph_url}/{date}"

        if not self.pixel_exists(date):
            print("Cannot update a pixel that does not exist.")
            return
        params = {
            "quantity": self.get_quantity(),
            "optionalData": json.dumps(self.get_optional_data()),
        }
        response = requests.put(url=url, headers=self.headers, json=params, timeout=5)
        print(response.text)
        response.raise_for_status()
        print(response.json())

    def exit_app(self):
        print("Goodbye!")
        exit()

    def delete_pixel(self):
        date = self.get_date()
        url = f"{self.graph_url}/{date}"

        if not self.pixel_exists(date):
            print("Cannot delete a pixel that does not exist.")
            return
        response = requests.delete(url=url, headers=self.headers, timeout=5)
        print(response.text)
        response.raise_for_status()
        print(response.json())

    def run(self):
        while True:
            print(f"\n=== Welcome! {self.user_name} ===")
            print("1. Log today")
            print("2. Update pixel")
            print("3. Delete pixel")
            print("4. View graph")
            print("5. Exit")

            choice = input("\nWhat's your choice: ").strip()

            action = self.menu_options.get(choice, lambda: print("\nInvalid input"))

            action()


yuchen_pixla = PixelaApp()

yuchen_pixla.run()
