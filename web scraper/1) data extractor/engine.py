import os.path

from bs4 import BeautifulSoup
import requests

url = "https://perm.kinoafisha.info/cinema/"

if not os.path.isfile("./info.html"):
    response = requests.get(url)
    html = response.text
    file = open("info.html", "w", encoding="utf-8")
    file.write(html)
    file.close()

with open("info.html", encoding="utf-8") as file:
    file = file.read()

soup = BeautifulSoup(file, "lxml")

all_cinemas_hrefs = soup.find_all(class_="cinemaList_ref")
all_cinemas_names = soup.find_all(class_="cinemaList_name")
all_cinemas_addresses = soup.find_all(class_="cinemaList_addr")

for item in all_cinemas_hrefs:
	item_href = item.get("href")
	print(item_href)
for item in all_cinemas_names:
	item_name = item.text
	print(item_name)
for item in all_cinemas_addresses:
	item_address = item.text
	print(item_address)
