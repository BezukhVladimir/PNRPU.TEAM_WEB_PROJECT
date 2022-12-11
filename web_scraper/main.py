#import sys
import data_extractor.extractor as extractor

#sys.path.append("..\\..\\..\\PNRPU_TEAM_WEB_PROJECT")

current_city = "perm"

extractor.extract_cinemas(current_city)
current_cinemas = extractor.get_cinemas(current_city)
extractor.extract_cinemas_schedules(current_city, current_cinemas)

for cinema in current_cinemas:
    films_sessions = extractor.get_films_sessions(current_city, cinema)

    for film_sessions in films_sessions:
        print(film_sessions.film.name,
              film_sessions.film.year,
              film_sessions.film.country,
              film_sessions.film.tags)

        for session in film_sessions.sessions:
            print(session.start_time,
                  session.ticket_price)
