from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()

driver.maximize_window()

#navigate to the url
driver.get("https://www.google.com/")
