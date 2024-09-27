import json
import requests
from twilio.rest import Client

stock_url = "https://www.alphavantage.co/query"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "5min",
    "datatype": "json",
    "apikey": "B1T2WN4BSQB9320T",
}

stock_data = requests.get(stock_url, params=stock_parameters)

stock_data = stock_data.json()

with open("stock_data.json", "w") as file:
    json.dump(stock_data, file, indent=4)

stock_data = [
    float(i[1].get("4. close"))
    for i in list(stock_data.get("Time Series (Daily)").items())[:2]
]

is_up = "🔺" if (stock_data[0] - stock_data[1]) else "🔻"

price = round(((stock_data[0] - stock_data[1]) * 100) / stock_data[0], 2)


print(stock_data)
print(price)

if price > 10 or price < -10:
    news_url = "https://newsapi.org/v2/everything"

    news_parameters = {
        "q": "Tesla",
        "symbol": "T",
        "language": "en",
        "sortBy": "publishedAt",
        "apikey": "0623578070a647dd80f05f545af41c1f",
    }

    news_data = requests.get(news_url, params=news_parameters)

    news_data = news_data.json()

    with open("news_data.json", "w") as file:
        json.dump(news_data, file, indent=4)

    news_data = news_data.get("articles")[0]
    t = news_data.get("title")
    d = news_data.get("description")

    print(news_data)

    twilio_account_sid = "AC07a81f1226651d58932b3890f2aa5e65"
    twilio_auth_token = "606344a8e18280136fc06755e7489eec"

    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body=f"{is_up} {round(price,2)}\n{t}\n{d}",
        from_="+12017206236",
        to="+917247477955",
    )

    print(message.status)