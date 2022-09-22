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
containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text()
    subtitle = container.find_element(by="xpath", value='./a/p').text()

    link = container.find_element(by='xpath', value='./a').get_attribute("href")