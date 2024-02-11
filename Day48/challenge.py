# Challenge: Use Selenium to fill in the form at the URL and click "Sign Up"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Doe")

email = driver.find_element(By.NAME, value="email")
email.send_keys("johndoe@example.com")

button = driver.find_element(By.TAG_NAME, value="button")
button.click()

# Alternative solution
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("John", Keys.TAB, "Doe", Keys.TAB, "johndoe@example.com", Keys.TAB, Keys.ENTER)