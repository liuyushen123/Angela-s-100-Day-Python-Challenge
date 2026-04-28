import time
from datetime import datetime

import requests

MY_LAT = 40.815369
MY_LONG = -96.711885

param = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=param)
sun_response.raise_for_status()
data = sun_response.json()

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_response = iss_response.json()

iss_latitude = float(iss_response["iss_position"]["latitude"])
iss_longitude = float(iss_response["iss_position"]["longitude"])

now = datetime.now()
current_hour = now.hour


def is_night():
    param = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=param)
    response.raise_for_status()
    data = response.json()

    sunrise = datetime.fromisoformat(data["results"]["sunrise"]).astimezone()
    sunset = datetime.fromisoformat(data["results"]["sunset"]).astimezone()
    now = datetime.now().astimezone()

    return now >= sunset or now <= sunrise


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    return (
        MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5
    )


while True:
    if is_iss_overhead():
        print("ISS is overhead!")

        if is_night():
            print("Visible right now 🌙")
        else:
            print("Not visible (daytime) ☀️")
    else:
        print("ISS is not near your location")

    time.sleep(10)
