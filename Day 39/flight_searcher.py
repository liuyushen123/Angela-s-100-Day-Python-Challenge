import datetime as dt
import os

import pandas
import requests
from dotenv import load_dotenv
from utils.get_env import get_required_env_var

load_dotenv()


class FlightSearchManager:
    def __init__(self):
        self.airport_info = pandas.DataFrame(pandas.read_csv("iata-icao.csv"))
        self.serpi_url = "https://serpapi.com/search.json"
        self.departure_id = "OMA"
        self.sugested_departure_time = (
            dt.datetime.now() + dt.timedelta(days=92)
        ).strftime("%Y-%m-%d")
        self.serp_api_key = get_required_env_var("serp_api_key")

    def get_destination_code(self, airport_name):
        matches = self.airport_info.loc[
            self.airport_info["airport"] == airport_name, "iata"
        ]

        if matches.empty:
            print(f"No IATA code found for airport: {airport_name}")
            return None

        return matches.iloc[0]

    def get_lowest_price(self, airport_code):
        params = {
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": airport_code,
            "currency": "USD",
            "type": "2",
            "outbound_date": self.sugested_departure_time,
            "api_key": self.serp_api_key,
        }

        print(
            f"Searching flights for route {self.departure_id}/{airport_code} on {self.sugested_departure_time}"
        )

        response = requests.get(self.serpi_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        flights = data.get("best_flights", []) + data.get("other_flights", [])
        prices = [f["price"] for f in flights if "price" in f]

        if not prices:
            print(
                f"No flights found for route {self.departure_id}/{airport_code} "
                f"date: {self.sugested_departure_time}"
            )
            return None, self.sugested_departure_time

        return min(prices), self.sugested_departure_time


if __name__ == "__main__":
    fsm = FlightSearchManager()
    print(fsm.get_lowest_price("SFO"))
