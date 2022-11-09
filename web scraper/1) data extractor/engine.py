from bs4 import BeautifulSoup
import requests

from cinema import Cinema
from lib.file_checks import does_file_not_exist_or_is_empty

url_to_cinemas_in_perm = "https://perm.kinoafisha.info/cinema/"
name_div_class_with_necessary_information = "cinemaList cinemaList-details outer-mobile"
perm_cinemas_list = "perm_cinemas_list.html"

if does_file_not_exist_or_is_empty(perm_cinemas_list):
    response = requests.get(url_to_cinemas_in_perm)
    raw_html = response.text
    soup = BeautifulSoup(raw_html, "lxml")
    html = str(soup.find(class_=name_div_class_with_necessary_information))
    file = open(perm_cinemas_list, "w", encoding="utf-8")
    file.write(html)
    file.close()

with open(perm_cinemas_list, encoding="utf-8") as current_cinemas_list:
    current_cinemas_list = current_cinemas_list.read()

soup = BeautifulSoup(current_cinemas_list, "lxml")

all_cinemas_hrefs = soup.find_all(class_="cinemaList_ref")
all_cinemas_names = soup.find_all(class_="cinemaList_name")
all_cinemas_addresses = soup.find_all(class_="cinemaList_addr")
cinemas = []

for i in range(0, len(all_cinemas_hrefs)):
    cinemas.append(Cinema(all_cinemas_hrefs[i].get("href"),
                          all_cinemas_names[i].text,
                          all_cinemas_addresses[i].text))

for cinema in cinemas:
    print(cinema.href)
    print(cinema.name)
    print(cinema.addresses)
    print()
