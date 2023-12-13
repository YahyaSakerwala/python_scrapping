from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.reuters.com/world/')
sleep(10)

search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div/div[1]/div[3]/a').click()