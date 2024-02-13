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





chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.environ.get("FORMS_URL")) # Forms link from Google Forms
driver.maximize_window()