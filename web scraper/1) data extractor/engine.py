from bs4 import BeautifulSoup
import requests
import json
import os.path
import sys
import os

from cinema import Cinema
sys.path.append("..\\..\\..\\PNRPU_TEAM_WEB_PROJECT")
from lib.file_checks import does_file_not_exist_or_is_empty
from lib.film import Film
from lib.shows import Shows
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

films = []
shows = []
timess = []
count = 0

for cinema in cinemas:
	req = requests.get(url=(cinema.href+"schedule/"))
	src = req.text
	current_cinema = f"data/{count}_{cinema.name}.html"

	if does_file_not_exist_or_is_empty(current_cinema):
		with open(f"data/{count}_{cinema.name}.html","w",encoding="utf-8") as file:
			file.write(src)
			
	soup = BeautifulSoup(src, "lxml")

	all_films_names = soup.find_all(class_="showtimesMovie_name")
	#all_films_names = soup.find_all(class_="showtimesMovie_info")
	all_films_tags = soup.find_all(class_="showtimesMovie_categories")
	all_films_details = soup.find_all(class_="showtimesMovie_details")
	all_films_times = soup.find_all(class_="showtimes_sessions")
	
	for item in all_films_names:
		item_name=item.text
		#print(item_name)
	for item in all_films_tags:
		item_tags=item.text
		#print(item_tags)
	for item in all_films_details:
		item_details=item.text
		det = item_details.split()
		
		#print(item_details)
		print(det)
	item_times = []
	for item in all_films_times:
		item_times = item.text
		for obj in item_times:
			obj.replace('\n', "")
			#obj.strip()
		item_times = item_times.replace('\n', " ")
		arr = item_times.split()
		for item in arr:
			if item=="от" or item=="₽":
				arr.remove(item)
		item_times = arr
		print(item_times)
	for i in range(0, len(all_films_names)):
		films.append(Film(cinema.name,
    		all_films_names[i].text,
            all_films_tags[i].text,
            all_films_details[i].text))
	count += 1

for film in films:
    print(film.cinema)
    print(film.name)
    print(film.tags)
    print(film.details)
for show in shows:
    print(show.time)
    print(show.price)
