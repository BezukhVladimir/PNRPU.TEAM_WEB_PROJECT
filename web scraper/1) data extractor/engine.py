from bs4 import BeautifulSoup
import requests

r = requests.get('https://perm.kinoafisha.info/cinema/') #url - ссылка
html = r.text
f = open('info.html', 'w+', encoding="utf-8")
f.write(html)
soup = BeautifulSoup(f, "lxml")

f.close()