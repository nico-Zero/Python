import requests
from twilio.rest import Client


url = "https://ai-weather-by-meteosource.p.rapidapi.com/hourly"
twilio_account_sid = "AC07a81f1226651d58932b3890f2aa5e65"
twilio_auth_token = "606344a8e18280136fc06755e7489eec"


# parameters = {"lat": "22.352600", "lon": "82.545403", "timezone": "GMT"}
parameters = {"lat": "12.971599", "lon": "77.594566", "timezone": "GMT"}

headers = {
    "X-RapidAPI-Key": "bbaf8bc7dcmsh888f9b9b549d0b1p1642cdjsnfc4e5de2d813",
    "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=parameters)
response = response.json()

response = response.get("hourly").get("data")[5:29]

rain = False

for i in response:
    day = i.get("precipitation").get("type").lower()
    time = i.get("date").split("T")[1]
    if day == "rain":
        rain = True

if rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="Fuck. It will RAIN today!☔😠. Just Remember to bring a Umbrella",
        from_="+12017206236",
        to="+917247477955",
    )
