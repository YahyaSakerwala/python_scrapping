# import requests

# def fetchAndSaveToFile(url, path):
#     r = requests.get(url)
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(r.text)

# url = "https://timesofindia.indiatimes.com/city/mumbai"

# fetchAndSaveToFile(url, "data/times.html")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://apnews.com/')
# sleep(10)
# page = driver.page_source
# soup = BeautifulSoup(page, "html.parser")

# button_decline = '//*[@id="bx-close-inside-2407156"]/svg'
# element_to_decline = driver.find_element(By.XPATH, button_decline)
# element_to_decline.click()

# sports = driver.find_element(By.XPATH, "/html/body/div[2]/bsp-header/div[1]/div[2]/bsp-nav/ul/li[4]/div/div/a")
# sports.click()

# button_xpath = "/html/body/div[2]/bsp-header/div[1]/div[3]/bsp-search-overlay/button/svg[1]/use"
# element_to_click = driver.find_element(By.XPATH, button_xpath)

# element_to_click.click()

try:
    # Wait for the popup to be present
    popup_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bx-close-inside-2407151"))
    )

    # Click the close button to dismiss the popup
    popup_element.click()

    print("Closed the popup.")
except Exception as e:
    print(f"Error: {e}")


try:
    element_to_click = driver.find_element(By.CSS_SELECTOR, '.MainNavigationItem-text a.AnClick-MainNav')
    
    # Simulate a mouse click on the element
    element_to_click.click()
    
    print("Clicked on Sports link.")
except Exception as e:
    print(f"Error: {e}")




