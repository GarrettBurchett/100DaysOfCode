import requests
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv
import os
from pathlib import Path
import smtplib

load_dotenv(dotenv_path=Path("./Day47/.env"))

MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")

URL = "https://www.amazon.com/Marvels-Spider-Man-Miles-Morales-Ultimate-Playstation/dp/B08QFWWJ8K/ref=sr_1_1?keywords=spiderman"

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}

target_price = 45
response = requests.get(URL, headers=HEADER)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")

price = soup.select_one(".a-offscreen").getText()
current_price = float(price.split("$")[1])
print(current_price)

product = soup.find(id="productTitle").getText().strip()

if current_price <= target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{product} is now ${current_price}.\n{URL}".encode('utf-8')
        )