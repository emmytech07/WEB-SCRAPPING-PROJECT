# https://www.thesun.co.uk/sport/football/


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
# path = "/Users/hp/Downloads/"

# service = Service(executable_path=path)
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="/Users/hp/Downloads/")

driver.get(website)