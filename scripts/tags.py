import requests
from bs4 import BeautifulSoup

with open("scripts/sample.html", "r")as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
#print(soup.title.string, type(soup.title.string))
#print(soup.div)

#print(soup.find_all("div")[0])

for link in soup.find_all("a"):
    print(link.get_text())
    print(link.get("href"))

s = soup.find(id = "link3")
print(s)

print(soup.select("div.italic"))
print(soup.select("span#italic"))