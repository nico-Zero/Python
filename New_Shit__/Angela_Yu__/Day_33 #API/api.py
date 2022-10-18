# http://api.open-notify.org/iss-now.json
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    print("Error")
else:
    response = response.json()
    print(response)
