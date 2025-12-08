import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")

username_field = driver.find_element("xpath", "//input[@placeholder= 'Username']")
username_field.send_keys("standard_user")

time.sleep(1)

password_field = driver.find_element("xpath", "//input[@placeholder='Password']")
password_field.send_keys("secret_sauce")

time.sleep(3)

login_button = driver.find_element("xpath", "//input[@type='submit']")
login_button.click()

time.sleep(6)

assert driver.current_url == "https://www.saucedemo.com/inventory.html", print("Mistake")
