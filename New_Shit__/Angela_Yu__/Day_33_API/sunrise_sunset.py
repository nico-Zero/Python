from time import sleep
import requests
from datetime import datetime

MY_LAT: float = 22.359449
MY_LNG: float = 82.750061
parameter: dict = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}


def vision(your_location, object_location):
    if (
        your_location[0] - 5 < object_location[0] < your_location[0] + 5
        and your_location[1] - 5 < object_location[1] < your_location[1] + 5
    ):
        return True
    else:
        return False


while True:
    sun_data = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    sun_data.raise_for_status()
    sun_data = sun_data.json()

    # sunrise and sunset hours
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    iss_location = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_location.raise_for_status()
    iss_location = iss_location.json()["iss_position"]

    # iss_location in latitude and longitude
    iss_lat = float(iss_location["latitude"])
    iss_lng = float(iss_location["longitude"])

    # today hour
    today_hour = datetime.now().hour

    if sunrise_hour > today_hour > sunset_hour:
        if vision((MY_LAT, MY_LNG), (iss_lat, iss_lng)):
            print("look Up")
            sleep(60)
            continue

    print("ISS location are:-\niss_lat: ", iss_lat, "\n", "iss_lng: ", iss_lng, sep="")
    print("No ISS Today😿!!!")

    break
