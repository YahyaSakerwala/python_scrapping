import requests
from bs4 import BeautifulSoup
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('executable_path=C:\\Users\\3463\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get("https://apnews.com/search?q=positive+outlook&s=0")

# Use WebDriverWait to wait for the elements to be present on the page

elements = WebDriverWait(driver, 20).until(

    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Link"))

)

list = []
listNewsJson = []

# Iterate over the elements and print href links

for element in elements:

    href_link = element.get_attribute("href")

    if href_link not in list:

        list.append(href_link)

driver.quit()

for link in list:

    if link is not None:

        #print(link)
        response = requests.get(link)
        htmlContent = response.content
        soup = BeautifulSoup(htmlContent, "html.parser")

        # Extracting specific metadata
        og_title = soup.find('meta', property='og:title')
        og_url = soup.find('meta', property='og:url')
        og_description = soup.find('meta', property='og:description')
        published_time = soup.find('meta', property='article:published_time')
        modified_time_meta = soup.find('meta', property='article:modified_time')
        category = soup.find('meta', property='article:section')
        author = soup.find('meta', property='og:site_name')

        # Create a dictionary to store the metadata
        metadata = {}

        # Add metadata to the dictionary
        if og_title:
            metadata["title"] = og_title['content']

        if og_url:
            metadata["url"] = og_url['content']

        if category:
            metadata["category"] = category['content']

        if author:
            metadata["author"] = author['content']

        if og_description:
            metadata["content"] = og_description['content']

        if published_time:
            metadata["published_time"] = published_time['content']

        if modified_time_meta:
            metadata["modified_time"] = modified_time_meta['content']

        # Convert the dictionary to a JSON object
        json_metadata = json.dumps(metadata, indent=2)
        listNewsJson.append(json_metadata)

# Close the browser window
print(listNewsJson)