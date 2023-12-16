import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime


url="https://apnews.com/search?q=positive+outlook#nt=navsearch"     
response = requests.get(url)
html_doc = response.text
soup = BeautifulSoup(html_doc,'html.parser')

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    items = soup.select("div.PageList-items-item")

    json_data_list = []

    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            title_element = item.find("div", class_="PagePromo-title")
            title = title_element.get_text(strip=True) if title_element else ""
            description_element = item.find("div", class_="PagePromo-description")
            description = description_element.get_text(strip=True) if description_element else ""

            # Find the date element
            byline_element = item.find("div", class_="PagePromo-byline")
            date_element = byline_element.find("div", class_="PagePromo-date") if byline_element else None
            # Find the bsp-timestamp element within the byline element
            timestamp_element = date_element.find("bsp-timestamp") if date_element else None
            epochdate_str = timestamp_element.get("data-timestamp") if timestamp_element else ""
            if epochdate_str:
                epochdate = int(epochdate_str) // 1000  # Convert milliseconds to seconds
                dt_object = datetime.fromtimestamp(epochdate)
                human_readable_datetime = dt_object.strftime('%Y-%m-%d %H:%M:%S')

                if title:
                    json_data = {"title": title, "description": description, "date": human_readable_datetime}
                    json_data_list.append(json_data)

        json_response = json.dumps(json_data_list, indent=2)
        f.write(json_response)

    return json_response

fetchAndSaveToFile(url, "data/apnewsdata.html")