import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="tr", class_="athing submission")
my_json = []

for article_tags in articles:
    dictionary = {}
    current_id = article_tags["id"]

    dictionary["page_link"] = article_tags.select_one(".titleline a").get("href")
    dictionary["title"] = article_tags.select_one(".titleline a").get_text(strip=True)
    dictionary["score"] = int(
        soup.find(class_="score", id=f"score_{current_id}").string.split(" ")[0]
    )

    my_json.append(dictionary)

sorted_data = sorted(my_json, key=lambda x: x["score"], reverse=True)

print()
for item in sorted_data:
    print(item["score"], "-", item["title"])
    print()
print(my_json)
