# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from json import dump

sheety_api = (
    "https://api.sheety.co/396fe2deb7f4f387c77a206b624a1c7e/flightPriceChecker/sheet1"
)

data = FlightData(sheety_api).flight_data

with open("New_Shit__/Angela_Yu__/Day_39 #/data.json", "w") as file:
    dump(data, file, indent=4)

filtered_data = DataManager(data)

flight_min_price = {i["city"]: i["lowestPrice"] for i in filtered_data.filtered_data}

flight_search = [
    FlightSearch("RPR", i["iataCode"], "05/11/2022", "5/11/2022").result
    for i in filtered_data.filtered_data
]

with open("New_Shit__/Angela_Yu__/Day_39 #/flight_data.json", "w") as file:
    dump(flight_search, file, indent=4)


# print(*flight_search, sep="\n")

filtered_flight_search_data = {
    i["data"][0]["cityTo"]: {
        "cityFrom": i["data"][0]["cityFrom"],
        "cityTo": i["data"][0]["cityTo"],
        "countryFrom": i["data"][0]["countryFrom"]["name"],
        "countryTo": i["data"][0]["countryTo"]["name"],
        "price": i["data"][0]["price"],
    }
    for i in flight_search
}

final_data = filtered_data.ok_price(filtered_flight_search_data)

print(final_data)

notification = NotificationManager()
message_status = notification.send_message(final_data)

print(message_status)
