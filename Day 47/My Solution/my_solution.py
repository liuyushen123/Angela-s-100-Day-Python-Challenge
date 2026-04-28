import requests
from bs4 import BeautifulSoup

live_url = "https://www.amazon.com/Bookmarks-Bookmark-Painting-Writers-Children/dp/B0D1FTTT8L/ref=sr_1_8?crid=35VEEUX3F5GZ9&dib=eyJ2IjoiMSJ9.GrcHKjpTIbQmvJrJeXR5Daer-tCoZuaqbOpqN2-1ItzVxdbWikL1Bxn3DxPKnT1oftna4PJeG43ntdAon3gJKtTLSGirkybEGhsfNaUp4OeJ8dLn--Bk7Sokkt1FZbnhfUNlgBr9BfsIQa3BbfAVUFJHXVzqD5_IiAAgpMenXRnpbMZEH6Rw5iHzxRdy_Vw3OrrfSjkvCoOop0Pno_no2lmB1JsKnJc28-kOn7c-bqTTnyvNZf9-z6XjrHZ4HOUdLnm3dTp0uWsAeCYruMv0m1mPpA123palSm1KC61XWj4.0IWMqSP9uTUJ7kyO8nDKxwJ2kVll14Q7PcNzb_ET7eM&dib_tag=se&keywords=bookmarks&qid=1776362471&sprefix=%2Caps%2C111&sr=8-8&th=1"

practice_url = "https://appbrewery.github.io/instant_pot/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}


response = requests.get(url=live_url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

price = soup.select("span.a-price-whole")

if price:
    print(price)
else:
    print("Amazon is too good")
