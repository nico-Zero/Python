# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from if_missing import Location
from json import dump

sheety_api = (
    "https://api.sheety.co/396fe2deb7f4f387c77a206b624a1c7e/flightPriceChecker/sheet1"
)

##-------------------------------------------------------------------------------------------------- GATHERING DATA

data = FlightData(sheety_api).flight_data

with open("data.json", "w") as file:
    dump(data, file, indent=4)
##---------------------------------------------------------------------------------------------------FILTERING DATA
data_filter = DataManager(data)

##---------------------------------------------------------------------------------------------------FINDING MISSING DATA AND FIXING IT
rows = data_filter.rows
missing_data = Location(rows)

with open("help.json", "w") as file:
    dump(missing_data.iata, file, indent=4)
filtered_data = missing_data.fix(sheety_api) or data_filter.filtered_data

##--------------------------------------------------------------------------------------------------SEARCHING FLIGHTS
flight_min_price = {i["city"]: i["lowestPrice"] for i in filtered_data}

flight_search = [
    FlightSearch("RPR", i["iataCode"], "15/11/2022", "15/11/2022").result
    for i in filtered_data
]

with open("flight_data.json", "w") as file:
    dump(flight_search, file, indent=4)

filtered_flight_searched_data = {
    i.get("data")[0]["cityTo"]: {
        "cityFrom": i.get("data")[0]["cityFrom"],
        "cityTo": i.get("data")[0]["cityTo"],
        "countryFrom": i.get("data")[0]["countryFrom"]["name"],
        "countryTo": i.get("data")[0]["countryTo"]["name"],
        "price": i.get("data")[0]["price"],
    }
    for i in flight_search
}

final_data = data_filter.ok_price(filtered_flight_searched_data)

# ---------------------------------------------------------------------------------------------------SENDING NOTIFICATIONS
notification = NotificationManager()
message_status = notification.send_message(final_data)

print(*message_status, sep="\n")
