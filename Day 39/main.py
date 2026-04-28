from data_manager import DataManager
from dotenv import load_dotenv
from flight_searcher import FlightSearchManager

load_dotenv()

my_flight = DataManager()
my_flight_searcher = FlightSearchManager()
my_data = my_flight.get_data()
print(f"\n\n\n{my_data}\n\n\n")
for row in my_data:
    row["iataCode"] = my_flight_searcher.get_destination_code(row["airportName"])
    row["lowestPrice"], departure_date = my_flight_searcher.get_lowest_price(
        row["iataCode"]
    )
    row["departure_date"] = departure_date
my_flight.flight_data = my_data
print(my_flight.flight_data)
my_flight.update_data()
