import requests
from twilio.rest import Client


url = "https://ai-weather-by-meteosource.p.rapidapi.com/hourly"
twilio_account_sid = "AC1ac2feb2140b9b5a239f841410dd3b5b"
twilio_auth_token = "6385a7c47d814d2472b51af3c42125d2"


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


client = Client(twilio_account_sid, twilio_auth_token)
message = client.messages.create(
    body="Fuck. It will RAIN today!☔😠. Just Remember to bring a Umbrella",
    from_="+18623621471",
    to="+917247477955",
)
print("done")
