import requests
from bs4 import BeautifulSoup
from config import ZILLOW_CLONE_URL


class ZillowPage:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        }
        self.response = requests.get(ZILLOW_CLONE_URL, headers=self.headers)
        self.response.raise_for_status()

        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_properties(self):
        properties = []

        for card in self.soup.select(".StyledPropertyCardDataWrapper"):
            properties.append(
                {
                    "link": self.extract_link(card),
                    "address": self.extract_address(card),
                    "price": self.extract_price(card),
                }
            )

        return properties

    def extract_link(self, card):
        return card.find("a")["href"]

    def extract_address(self, card):
        address = card.find("address").get_text(" ", strip=True)
        return address.replace(" | ", " ")

    def extract_price(self, card):
        price = card.find("span").get_text(strip=True)

        return int(
            price.replace("/mo", "")
            .replace("$", "")
            .replace(",", "")
            .replace("+", "")
            .split()[0]
        )
