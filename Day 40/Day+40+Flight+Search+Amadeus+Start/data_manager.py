import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/9ec77ccb1f24490364afb4e3c6666ba0/flightDeals/prices"
)

SHEETY_USERS_ENDPOINT = (
    "https://api.sheety.co/9ec77ccb1f24490364afb4e3c6666ba0/flightDeals/users"
)


class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()

        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)

        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization,
            )
            print(response.text)

    def get_users(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=self._authorization)
        data = response.json()

        self.sheety_user_list = data

        return self.sheety_user_list


if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_users()

    print(data_manager.sheety_user_list)
