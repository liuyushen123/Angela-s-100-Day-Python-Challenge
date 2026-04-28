import requests

url = "https://serpapi.com/search.json"

params = {
    "engine": "google_flights",
    "departure_id": "OMA",
    "arrival_id": "SFO",
    "currency": "USD",
    "type": "2",
    "outbound_date": "2026-07-30",
    "api_key": "85b59bbf6b0b349d0c589a7a99694c1f889cd717cd7943bcb6d3ded8ec404a1c",
}
response = requests.get(url, params=params, timeout=10)
data = response.json()
print(response.text)
print(data)

for i in data["best_flights"]:
    print(i["price"])
