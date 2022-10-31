from requests import get, put
from json import dump

URL = "https://api.tequila.kiwi.com/locations/query"


class Location:
    def __init__(self, name_list, apikey="HCXPvXreO03zkkAEuK67L88jVGqA3mKP"):
        self.iata = []

        for i in name_list:
            header = {"apikey": apikey}
            parameters = {"term": i.get("city"), "limit": 1}

            data = get(url=URL, params=parameters, headers=header)
            data.raise_for_status()

            formatted_data = {
                "city": data.json().get("locations")[0].get("name"),
                "code": data.json().get("locations")[0].get("code"),
            }

            self.iata.append(formatted_data)

    def fix(self):
        pass


x = [
    {"city": "Sydney", "iataCode": "", "lowestPrice": 5510000, "id": 5},
    {"city": "San Francisco", "iataCode": "", "lowestPrice": 2600000, "id": 9},
]

oc = Location(x)

with open("New_Shit__/Angela_Yu__/Day_39 #Flight_search/help.json", "w") as file:
    dump(oc.iata, file, indent=4)
