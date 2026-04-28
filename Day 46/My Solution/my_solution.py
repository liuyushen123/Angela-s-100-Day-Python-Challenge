import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.billboard.com/charts/hot-100/")
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li ul li h3")

for i, song in enumerate(songs):
    song = song.get_text().strip()
    print(f"The Number {i + 1}: {song}\n")
