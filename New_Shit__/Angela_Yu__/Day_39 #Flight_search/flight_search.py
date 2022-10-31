from requests import get

URL = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(
        self,
        fly_from,
        fly_to,
        date_from,
        date_to,
        apikey="HCXPvXreO03zkkAEuK67L88jVGqA3mKP",
    ):
        self.header = {"apikey": apikey}
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "curr":"IDR",
            "limit":1
        }
        self.result = get(url=URL, headers=self.header, params=self.parameters)
        self.result.raise_for_status()
        self.result = self.result.json()
