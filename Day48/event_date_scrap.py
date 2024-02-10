from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_dict = {}
for index, item in enumerate(zip(dates, events)):
    event_dict[index] = {'time': item[0].get_attribute("datetime").split("T")[0], 'name': item[1].text}

print(event_dict)

driver.quit()