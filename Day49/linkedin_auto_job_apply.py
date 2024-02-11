from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(dotenv_path=Path("./Day49/.env"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
           "&keywords=python%20developer"
           "&location=Houston%2C%20Texas%2C%20United%20States"
           "&redirect=false&position=1&pageNum=0"
           )
driver.maximize_window()

time.sleep(3)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email = driver.find_element(By.ID, "username")
email.send_keys(os.environ.get("LINKEDIN_USERNAME"))
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("LINKEDIN_PASSWORD"))
password.send_keys(Keys.ENTER)

time.sleep(5)
all_job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_job_listings:
    listing.click()
    time.sleep(2)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    time.sleep(3)
