from bs4 import BeautifulSoup
import requests
import re
import os

from lib.cinema import Cinema
from lib.film import Film
from lib.film_session import FilmSession
from lib.film_sessions import FilmSessions
from lib.file_checks import does_file_not_exist_or_is_empty
from lib.soup import get_soup


def extract_cinemas(city):
    url = "https://" + city + ".kinoafisha.info/cinema/"
    file_path = 'data_extractor/cities/' + city + '/cinemas.html'
    name_div_class_with_necessary_information = "cinemaList cinemaList-details outer-mobile"

    if does_file_not_exist_or_is_empty(file_path):
        response = requests.get(url)
        raw_html = response.text
        soup = BeautifulSoup(raw_html, "lxml")
        html = str(soup.find(class_=name_div_class_with_necessary_information))
        file = open(file_path, "w", encoding="utf-8")
        file.write(html)
        file.close()


def get_cinemas(city):
    file_path = "data_extractor/cities/" + city + "/cinemas.html"
    soup = get_soup(file_path)

    all_cinemas_hrefs = soup.find_all(class_="cinemaList_ref")
    all_cinemas_names = soup.find_all(class_="cinemaList_name")
    all_cinemas_addresses = soup.find_all(class_="cinemaList_addr")

    cinemas = []

    for i in range(0, len(all_cinemas_hrefs)):
        address = all_cinemas_addresses[i].text
        address = re.sub(' ', ' ', address)
        cinemas.append(Cinema(all_cinemas_hrefs[i].get("href"),
                              all_cinemas_names[i].text,
                              address))

    return cinemas


def extract_cinemas_schedules(city, cinemas):
    for cinema in cinemas:
        req = requests.get(url=(cinema.href + "schedule/"))
        src = req.text
        current_cinema = f"data_extractor/cities/{city}/cinemas_schedules/{cinema.name}.html"

        if does_file_not_exist_or_is_empty(current_cinema):
            print(os.getcwd())
            with open(f"data_extractor/cities/{city}/cinemas_schedules/{cinema.name}.html", "w",
                      encoding="utf-8") as file:
                file.write(src)


def get_films_sessions(city, cinema):
    films_sessions = []
    current_schedule = f"data_extractor/cities/{city}/cinemas_schedules/{cinema.name}.html"
    soup = get_soup(current_schedule)

    all_films_names = soup.find_all(class_="showtimesMovie_name")
    all_films_details = soup.find_all(class_="showtimesMovie_details")
    all_films_tags = soup.find_all(class_="showtimesMovie_categories")
    all_films_sessions = soup.find_all(class_="showtimes_sessions")

    for i in range(0, len(all_films_names)):
        details = all_films_details[i].text
        year = details[:4]
        country = details[6:]
        film = Film(all_films_names[i].text,
                    year,
                    country,
                    all_films_tags[i].text)
        film_sessions = []

        sessions = all_films_sessions[i]
        times_and_prices = re.sub("^|\n|от|₽", '', sessions.text)

        i = 0
        default_ticket_price = "300"

        while i < len(times_and_prices):
            temp_start_time = times_and_prices[i:i + 5]
            i += 5

            if i < len(times_and_prices) and times_and_prices[i] == ' ':
                i += 1
                temp_ticket_price = ""

                while i < len(times_and_prices) and times_and_prices[i] != ' ':
                    temp_ticket_price += times_and_prices[i]
                    i += 1

                i += 1
                film_sessions.append(
                    FilmSession(
                        temp_start_time,
                        temp_ticket_price))
            else:
                film_sessions.append(
                    FilmSession(
                        temp_start_time,
                        default_ticket_price))

        films_sessions.append(FilmSessions(
            film, film_sessions)
        )

    return films_sessions
