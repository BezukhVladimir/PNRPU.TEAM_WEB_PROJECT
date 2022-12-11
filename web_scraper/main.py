#import sys
import data_extractor.extractor as extractor
import data_saver.saver as saver

#sys.path.append("..\\..\\..\\PNRPU_TEAM_WEB_PROJECT")

current_city = "perm"

extractor.extract_cinemas(current_city)
current_cinemas = extractor.get_cinemas(current_city)
saver.update_cinemas(current_cinemas)

extractor.extract_cinemas_schedules(current_city, current_cinemas)
for cinema in current_cinemas:
    films_sessions = extractor.get_films_sessions(current_city, cinema)
    saver.update_films_sessions(cinema.name, films_sessions)
