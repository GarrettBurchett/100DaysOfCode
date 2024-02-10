from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Keep Chrome browser open after program finishes
chrome_options = Options()# webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_3?keywords=instant%2Bpot&sr=8-3&th=1") # Opens the webpage for the specified url
driver.get("https://www.python.org/")

# dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is ${dollars}.{cents}")

search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a') # Find the element w/ inspect, right click and select Copy XPath
print(bug_link.text)

# driver.close() # Closes a single tab (active tab)
driver.quit() # Quits the entire browser