import os
from pprint import pprint

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from utils.get_env import get_required_env_var

load_dotenv()


class DataManager:
    def __init__(self):
        self.user = get_required_env_var("sheety_user_name")
        self.password = get_required_env_var("sheety_password")
        self.endpoint_url = get_required_env_var("sheety_url")
        self.flight_data = []

    def get_data(self) -> list:
        if self.endpoint_url:
            response = requests.get(
                url=self.endpoint_url, auth=HTTPBasicAuth(self.user, self.password)
            )
            data = response.json()
            pprint(data)

            self.lowest_price = data["prices"]

        return self.lowest_price

    def update_data(self) -> None:
        for city in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    "lowestPrice": city["lowestPrice"],
                }
            }
            response = requests.put(
                url=f"{self.endpoint_url}/{city['id']}",
                json=new_data,
                auth=HTTPBasicAuth(self.user, self.password),
            )

            print(f"\n\n\n{response.text}\n\n\n")

    def __repr__(self):
        return f"DataManager(flight_data={self.flight_data})"


if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_data()
