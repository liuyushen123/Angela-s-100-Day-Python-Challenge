class FlightData:
    def __init__(
        self, price, origin_airport, destination_airport, out_date, return_date
    ):
        """
        Constructor for initializing a new flight data instance with specific travel details.

        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(flight, out_date, return_date, origin, destination):

    if flight is None or "best_flights" not in flight:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    lowest_price = min(f["price"] for f in flight["best_flights"])
    return FlightData(lowest_price, origin, destination, out_date, return_date)
