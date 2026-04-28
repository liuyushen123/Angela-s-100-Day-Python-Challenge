import bs4
import requests

response = requests.get("https://op.gg/lol/champions?position=jungle")
opgg_web_page = response.text


soup = bs4.BeautifulSoup(opgg_web_page, "html.parser")

champion_names = soup.find_all(class_="flex-1 truncate text-xs max-[420px]:sr-only")
champion_win_rate = soup.find_all(class_="text-xs text-gray-600")

champions = soup.select("tr")
data = []

for champ in champions:
    name_tag = champ.select_one(".flex-1.truncate")
    stats_tags = champ.select(".text-xs.text-gray-600")

    if name_tag and len(stats_tags) >= 2:
        name = name_tag.get_text(strip=True)
        win_rate = stats_tags[0].get_text(strip=True)
        pick_rate = stats_tags[1].get_text(strip=True)

        data.append({"name": name, "win_rate": win_rate, "pick_rate": pick_rate})

for champ in data:
    print(
        f"{champ['name']} - Win Rate: {champ['win_rate']}, Pick Rate: {champ['pick_rate']}"
    )
