from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path("./Day53/.env"))

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

links = soup.select('.StyledPropertyCardDataArea-anchor')
print(f"Links length: {len(links)}")
prices = soup.select('.PropertyCardWrapper__StyledPriceLine')
print(f"Prices length: {len(prices)}")
addresses = soup.find_all('address')
print(f"Addresses length: {len(addresses)}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.environ.get("FORMS_URL")) # Forms link from Google Forms
driver.maximize_window()

for link, price, address in zip(links, prices, addresses):
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    if address.get_text().find('|') != -1:
        address_field.send_keys(address.get_text().split('|')[1].strip())
    else:
        text = address.get_text().split(',')[1:]
        address_field.send_keys(''.join(text).strip())

    time.sleep(2)
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price.get_text()[:6])

    time.sleep(2)
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(link.get('href'))

    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    time.sleep(2)
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()