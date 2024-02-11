# Challenge: Use selenium to print the total number of articles from the Wikipedia homepage to the console.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_of_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a[title="Special:Statistics"]')
# print(num_of_articles.text)
# ^^^ENDS CHALLENGE^^^. Below is all new learning code for interacting with webpages

# num_of_articles.click() # Tells Selenium to click the hyperlink.

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
driver.maximize_window()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER) # Types the word "Python" into the search bar and press Enter. The Keys class has lots of standard values for keyboard keys.
 