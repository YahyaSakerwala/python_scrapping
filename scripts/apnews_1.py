# import requests
# from bs4 import BeautifulSoup
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os

# def scrape_apnews_data():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('executable_path=C:\\Users\\3463\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()

#     driver.get("https://apnews.com/search?q=positive+outlook&s=0")

#     elements = WebDriverWait(driver, 20).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Link"))
#     )

#     link_list = []

#     for element in elements:
#         href_link = element.get_attribute("href")
#         if href_link not in link_list:
#             link_list.append(href_link)

#     driver.quit()

#     json_data_list = []

#     for link in link_list:
#         if link is not None:
#             response = requests.get(link)
#             html_content = response.content
#             soup = BeautifulSoup(html_content, "html.parser")

#             og_title = soup.find('meta', property='og:title')
#             og_url = soup.find('meta', property='og:url')
#             og_description = soup.find('meta', property='og:description')
#             published_time = soup.find('meta', property='article:published_time')
#             modified_time_meta = soup.find('meta', property='article:modified_time')
#             category = soup.find('meta', property='article:section')
#             author = soup.find('meta', property='og:site_name')

#             metadata = {}

#             if og_title:
#                 metadata["title"] = og_title['content']

#             if og_url:
#                 metadata["url"] = og_url['content']

#             if category:
#                 metadata["category"] = category['content']

#             if author:
#                 metadata["author"] = author['content']

#             if og_description:
#                 metadata["content"] = og_description['content']

#             if published_time:
#                 metadata["published_time"] = published_time['content']

#             if modified_time_meta:
#                 metadata["modified_time"] = modified_time_meta['content']

#             json_metadata = json.dumps(metadata, indent=2)
#             json_data_list.append(json_metadata)

#     with open(os.path.join('data', 'apnews_data.json'), 'w') as json_file:
#         json_file.write('\n'.join(json_data_list))

# if __name__ == "__main__":
#     scrape_apnews_data()



import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def scrape_apnews_data():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('executable_path=C:\\Users\\3463\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://apnews.com/search?q=positive+outlook&s=0")

    elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Link"))
    )

    link_list = []

    for element in elements:
        href_link = element.get_attribute("href")
        if href_link not in link_list:
            link_list.append(href_link)

    driver.quit()

    json_data_list = []

    for link in link_list:
        if link is not None:
            response = requests.get(link)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")

            og_title = soup.find('meta', property='og:title')
            og_url = soup.find('meta', property='og:url')
            og_description = soup.find('meta', property='og:description')
            published_time = soup.find('meta', property='article:published_time')
            modified_time_meta = soup.find('meta', property='article:modified_time')
            category = soup.find('meta', property='article:section')
            author = soup.find('meta', property='og:site_name')

            metadata = {}

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

            json_data_list.append(metadata)

    with open(os.path.join('data', 'apnews_data.json'), 'w') as json_file:
        json.dump(json_data_list, json_file, indent=2)

if __name__ == "__main__":
    scrape_apnews_data()
