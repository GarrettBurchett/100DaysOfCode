import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client

dotenv_path = Path("./Day36/.env")
load_dotenv(dotenv_path=dotenv_path)

alphavantage_API_Key = os.environ.get("ALPHA_VANTAGE_API_KEY")
news_API_key = os.environ.get("NEWS_API_KEY")
twilio_account = os.environ.get("TWILIO_ACCOUNT")
auth_token = os.environ.get("AUTH_TOKEN")

STOCK_NAME = "TSLA" # Pick any stock you would like.
COMPANY_NAME = "Tesla Inc" # Company name of the stock chosen

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': alphavantage_API_Key
}

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': news_API_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

price_data = [v for v in stock_data["Time Series (Daily)"].values()]
day_before_close = float(price_data[0]['4. close'])
yesterday_close = float(price_data[1]['4. close'])

difference = yesterday_close - day_before_close
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent_diff = difference / yesterday_close

if percent_diff >= 0.05 or percent_diff <= -0.05:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    news_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in news_response.json()['articles'][:3]]

    client = Client(twilio_account, auth_token)

    for article in news_articles:
        message = client.messages.create(
        from_=os.environ.get("TWILIO_PHONE"),
        body=f"{STOCK_NAME}: {up_down}{percent_diff:.2%}\n{article}",
        to=os.environ.get("MY_PHONE")
        )