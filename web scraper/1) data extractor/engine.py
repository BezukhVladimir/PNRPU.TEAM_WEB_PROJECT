from bs4 import BeautifulSoup
import requests

https = 'https://'
kinoafisha = '.kinoafisha.info/cinema/'
cities = ["perm"]

url = https + cities[0] + kinoafisha
response = requests.get(url)

html = response.text

#file = open('info.html', 'w', encoding="utf-8")
#file.write(html)
with open("info.html",encoding="utf-8") as file:
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


#file.close()
