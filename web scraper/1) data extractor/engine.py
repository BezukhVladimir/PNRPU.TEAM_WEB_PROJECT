from bs4 import BeautifulSoup
import requests

https = 'https://'
kinoafisha = '.kinoafisha.info/cinema/'
cities = ["perm"]

url = https + cities[0] + kinoafisha
response = requests.get(url)

html = response.text
file = open('info.html', 'w+', encoding="utf-8")
file.write(html)

soup = BeautifulSoup(file, "lxml")

file.close()
