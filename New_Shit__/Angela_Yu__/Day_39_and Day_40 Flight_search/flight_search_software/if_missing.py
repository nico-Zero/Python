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
                "id": str(i["id"]),
                "city": data.json().get("locations")[0].get("name"),
                "code": data.json().get("locations")[0].get("code"),
            }

            self.iata.append(formatted_data)

    def fix(self, api_url):
        if self.iata:
            print("Found missing data")
            for i in self.iata:
                print("Fixing row data id: ", i["id"])
                parameters = {"sheet1": {"iataCode": i["code"]}}

                x = put(
                    url=api_url + "/" + i["id"],
                    json=parameters,
                )
                x.raise_for_status()
                print(i["id"], "Fixed")

            flight_data = get(url=api_url)
            flight_data.raise_for_status()
            flight_data = flight_data.json()
            flight_data = list(flight_data.values())[0]

            return flight_data
        else:
            print("No missing data")
            return None
