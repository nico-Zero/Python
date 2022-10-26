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

filtered_data = DataManager(data).filtered_data

# print(filtered_data)

flight_search = FlightSearch(filtered_data[0]["iataCode"], "05/11/2022", "20/11/2022").result

print(flight_search)

with open("New_Shit__/Angela_Yu__/Day_39 #/flight_data.json", "w") as file:
    dump(flight_search, file, indent=4)
