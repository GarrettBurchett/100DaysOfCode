from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from pathlib import Path
import os
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv(dotenv_path=Path("./Day50/.env"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
driver.maximize_window()

time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="c1606223767"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(3)
facebook_login = driver.find_element(By.XPATH, '//*[@id="c1827564203"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()

time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(os.environ.get("FACEBOOK_USERNAME"))
password.send_keys(os.environ.get("FACEBOOK_PASSWORD"), Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

allow_location_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(5)
notification_button = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notification_button.click()

time.sleep(5)
cookies = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div[2]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()