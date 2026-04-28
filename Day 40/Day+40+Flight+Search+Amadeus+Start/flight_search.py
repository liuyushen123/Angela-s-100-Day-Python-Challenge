import os

import pandas
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class FlightSearch:
    def __init__(self):
        """
        Initialize an instance of the FlightSearch class.

        This constructor performs the following tasks:
        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.

        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token method.
        """
        self._api_key = os.environ["SERP_API_KEY"]
        self.data = pandas.DataFrame(pandas.read_csv("iata-icao.csv"))
        self.serp_url = "https://serpapi.com/search.json"
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.

    def get_destination_code(self, airport_name):

        try:
            code = self.data[self.data["airport"] == airport_name]
        except IndexError:
            print(f"IndexError: No airport code found for {airport_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {airport_name}.")
            return "Not Found"
        print(code)
        return code

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "currency": "USD",
            "type": "1",
            "outbound_date": from_time,
            "return_date": to_time,
            "api_key": self._api_key,
        }

        response = requests.get(url=self.serp_url, params=query, timeout=30)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print(
                "There was a problem with the flight search.\n"
                "For details on status codes, check the API documentation:\n"
                "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                "-reference"
            )
            print("Response body:", response.text)
            return None

        return response.json()
