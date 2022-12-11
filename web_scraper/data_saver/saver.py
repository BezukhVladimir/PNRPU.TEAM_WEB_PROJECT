import csv


def update_cinemas(cinemas):
    with open('data_saver/tables/cinemas.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for cinema in cinemas:
            writer.writerow([cinema.name, cinema.address])


def update_films_sessions(cinema_name, films_sessions):
    with open(f'data_saver/tables/{cinema_name}_films_sessions.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for film_sessions in films_sessions:
            writer.writerow([film_sessions.film.name,
                            film_sessions.film.year,
                            film_sessions.film.country,
                            film_sessions.film.tags])

            temp = []
            for session in film_sessions.sessions:
                temp.append(session.start_time)
                temp.append(session.ticket_price)
            writer.writerow(temp)
