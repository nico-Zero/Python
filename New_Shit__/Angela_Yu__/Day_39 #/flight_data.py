from requests import get


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, api_endpoint):
        self.flight_data = get(url=api_endpoint)
        self.flight_data.raise_for_status()
        self.flight_data = self.flight_data.json()
