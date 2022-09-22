# https://www.thesun.co.uk/sport/football/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "C:\chromedriver"

service = Service(executable_path=path)