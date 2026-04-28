import os
from pprint import pprint

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


class DataManager:
    def __init__(self):
        self.user = os.getenv("sheety_user_name")
        self.password = os.getenv("sheety_password")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.endpoint_url = os.getenv("sheety_url")
        self.flight_data = {}

    def get_data(self):
        response = requests.get(url=self.endpoint_url, auth=self.authorization)
        data = response.json()
        pprint(data)

        self.lowest_price = data["prices"]

        return self.lowest_price

    def update_data(self):
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
                auth=self.authorization,
            )

            print(f"\n\n\n{response.text}\n\n\n")
