import datetime as dt
import os

import pandas
import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearchManager:
    def __init__(self):
        self.airport_info = pandas.DataFrame(pandas.read_csv("iata-icao.csv"))
        self.serpi_url = "https://serpapi.com/search.json"
        self.departure_id = "OMA"
        self.sugested_departure_time = (
            dt.datetime.now() + dt.timedelta(days=92)
        ).strftime("%Y-%m-%d")
        self.serp_api_key = os.getenv("serp_api_key")

    def get_destination_code(self, airport_code):
        return self.airport_info[self.airport_info["airport"] == airport_code][
            "iata"
        ].values[0]

    def get_lowest_price(self, airport_code):
        print(f"\n\n\n{self.sugested_departure_time}\n\n\n")
        params = {
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": airport_code,
            "currency": "USD",
            "type": "2",
            "outbound_date": self.sugested_departure_time,
            "api_key": self.serp_api_key,
        }

        response = requests.get(self.serpi_url, params=params, timeout=10)

        print(f"\n\n\n{response.text}\n\n\n")
        data = response.json()
        cheapest = float("inf")

        if "best_flights" not in data:
            print(
                f"No flights found for route {self.departure_id}/{airport_code} date: {self.sugested_departure_time}"
            )
            return -1

        for flight in data["best_flights"]:
            if flight["price"] < cheapest:
                cheapest = flight["price"]
        return cheapest, self.sugested_departure_time
