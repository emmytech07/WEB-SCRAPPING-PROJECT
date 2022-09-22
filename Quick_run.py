from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)

# find element by name 
Name_search = driver.find_element(By.CSS_SELECTOR, value="input[name='q']")
Name_search.clear
Name_search.send_keys("checking")
Name_search.send_keys(Keys.RETURN)
