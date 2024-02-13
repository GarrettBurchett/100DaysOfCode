from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
from pathlib import Path
import os
import time


load_dotenv(dotenv_path=Path("./Day52/.env"))

SIMILAR_ACCOUNT = "chefsteps" # Account you want to get followers from.

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(3)
        cookie_warning = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        if cookie_warning:
            cookie_warning[0].click()

        username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password, Keys.ENTER)

        time.sleep(4)
        save_login_prompt = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3)
        notifications_prompt = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        if notifications_prompt:
            notifications_prompt.click()


    def find_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}/followers")

        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Cancel")]')
                cancel_button.click()

bot = InstaFollower()
bot.login(username=os.environ.get("INSTAGRAM_USERNAME"), password=os.environ.get("INSTAGRAM_PASSWORD"))
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()