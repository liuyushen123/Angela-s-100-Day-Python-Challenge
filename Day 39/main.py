from data_manager import DataManager
from dotenv import load_dotenv
from pprint import pprint
from flight_searcher import FlightSearchManager

load_dotenv()

my_flight = DataManager()
my_flight_searcher = FlightSearchManager()
my_data = my_flight.get_data()


pprint(my_data)
for row in my_data:
    code = my_flight_searcher.get_destination_code(row["airportName"])
    row["iataCode"] = code

    if code is None:
        row["lowestPrice"] = None
        row["departure_date"] = None
        continue

    row["lowestPrice"], row["departure_date"] = my_flight_searcher.get_lowest_price(
        code
    )


my_flight.flight_data = my_data
my_flight.update_data()
