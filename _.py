import requests

url = "https://sms77io.p.rapidapi.com/sms"

payload = "to=%2B917247477955&p=JT5qe4eP6u7Z88wX0UUhtMaWsTTKGZEGk9ldruv36wClh6aqnVqyg9Eew0KJwmwwYM6KmMQE21LwJJ3k5PStA2UjhQ&text=Dear%20customer.%20We%20want%20to%20say%20thanks%20for%20your%20trust.%20Use%20code%20MINUS10%20for%2010%20%25%20discount%20on%20your%20next%20order!&json=1"
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "bbaf8bc7dcmsh888f9b9b549d0b1p1642cdjsnfc4e5de2d813",
    "X-RapidAPI-Host": "sms77io.p.rapidapi.com",
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
