from datetime import datetime

import requests

MY_LAT = 40.815369
MY_LONG = -96.711885

param = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=param)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

now = datetime.now()
current_hour = now.hour

print(sunrise, sunset, current_hour)
