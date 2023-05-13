import json
import requests
from datetime import datetime


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": "6ffaad54",
    "x-app-key": "987eb1ebd928dad614d711de0123828e",
}

parameters = {
    "query": str(input("Enter your exercises:- ")),
}

refined_data = requests.post(url=nutritionix_endpoint, json=parameters, headers=header)

refined_data = refined_data.json()
with open(
    "exercise_data.json",
    "w",
) as f:
    json.dump(refined_data, f, indent=4)

refined_data = refined_data.get("exercises")

print(*refined_data, sep="\n")

# ---------------------------------------------------------------------------------------------

today = datetime.now()
DATE = today.strftime("%Y-%m-%d")
TIME = today.strftime("%H:%M:%S")

sheety_api_endpoint = (
    "https://api.sheety.co/396fe2deb7f4f387c77a206b624a1c7e/pythonExercise/sheet1"
)

header = {"Content-Type": "application/json"}

for i in refined_data:
    parameter = {
        "sheet1": {
            "date": DATE,
            "time": TIME,
            "exercise": i.get("name"),
            "duration": i.get("duration_min"),
            "calories": i.get("nf_calories"),
        }
    }

    data = requests.post(url=sheety_api_endpoint, json=parameter, headers=header)

    print(data.json())
