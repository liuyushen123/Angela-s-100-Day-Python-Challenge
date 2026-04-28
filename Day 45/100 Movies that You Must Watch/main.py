import bs4
import requests

EMPIR_URL_ENDPOINT = (
    "https://www.empireonline.com/movies/features/best-movies-of-all-time-us/"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(EMPIR_URL_ENDPOINT, headers=headers)
contents = response.text

soup = bs4.BeautifulSoup(contents, "html.parser")

all_movies = soup.find_all(name="span", class_="content_content__i0P3p")
movies = []

for movie in all_movies:
    h2 = movie.select_one("h2")

    if h2:
        text = h2.get_text(strip=True)

        if ")" in text:
            rank, title = text.split(")", 1)
            if rank.isdigit():
                movies.append((int(rank), title.strip()))

movies.sort()

with open("movies.txt", "w") as file:
    for rank, title in movies:
        file.write(f"{rank}. {title}\n")
