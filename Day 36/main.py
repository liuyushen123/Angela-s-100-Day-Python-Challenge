import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("ALPHA_ADVANTAGE_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


############################## Helper Function ##############################
def percentage_news(percentage):
    if percentage > 0:
        up_down = "🔺"
    elif percentage < 0:
        up_down = "🔻"
    else:
        return f"{STOCK}: 0.00%"
    return f"{STOCK}: {up_down}{abs(percentage):.2f}%"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
print(stock_response.json())
stock_response = stock_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_response.items()]

yestarday_closing_price = float(data_list[0]["4. close"])
day_before_yestarday_closing_price = float(data_list[1]["4. close"])

difference = yestarday_closing_price - day_before_yestarday_closing_price

difference_percentage = (difference / day_before_yestarday_closing_price) * 100

formatted_percentage = percentage_news(difference_percentage)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

today = dt.datetime.today().strftime("%Y-%m-%d")
new_params = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
}
news_response = requests.get(NEWS_ENDPOINT, new_params)
news_response.raise_for_status()
news_response = news_response.json()
articles = news_response["articles"]
three_article = articles[:3]
formatted_articles = [
    f"{formatted_percentage}\nHeadline: {article['title']}\nBrief: {article['description']}"
    for article in three_article
]

for msg in formatted_articles:
    print(msg)
    print("_" * 50)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
