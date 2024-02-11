from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

start = time.time()
difference = 0
upgrades = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory', 'buyGrandma', 'buyCursor']
store = {}

while difference < 300:
    if round(difference, 2) % 5 == 0:
        current_money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
        for upgrade in upgrades:
            store[upgrade] = int(driver.find_element(By.XPATH, value=f'//*[@id="{upgrade}"]/b').text.split('-')[1].strip().replace(",", ""))
        for item in store:
            if store[item] <= current_money:
                item_to_buy = driver.find_element(By.ID, value=item)
                item_to_buy.click()
                break
    cookie.click()
    end = time.time()
    difference = end - start

cps = driver.find_element(By.ID, value='cps').text
print(cps)