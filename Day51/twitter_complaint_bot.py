from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from pathlib import Path
import os
import time

load_dotenv(dotenv_path=Path("./Day51/.env"))

PROMISED_DOWN = 150 # Promised minimum download speed per Mbps
PROMISED_UP = 10 # Promised minimum upload speed per Mbps

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:

    def __init__(self, options):
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        
        time.sleep(3)
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()
        
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text


    def tweet_at_provider(self, internet_provider_handle):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        
        time.sleep(3)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(os.environ.get("TWITTER_USERNAME"), Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        password.send_keys(os.environ.get("TWITTER_PASSWORD"), Keys.ENTER)

        time.sleep(5)
        message = f"Hey {internet_provider_handle}, why is my internet speed DOWN: {self.down} Mbps/ UP: {self.up} Mbps, when I pay for DOWN: {PROMISED_DOWN} Mbps / UP: {PROMISED_UP} Mbps?"
        message_box = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')
        message_box.send_keys(message)

        time.sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                          '/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()



bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider('Internet Provider')