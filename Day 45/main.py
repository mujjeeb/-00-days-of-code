import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

import requests

response = requests.get(url=URL)

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, 'html.parser')

movies_tag = soup.find_all(name='h3', class_="title")

movies_to_watch = []
for movie in movies_tag:
    films = movie.getText()
    movies_to_watch.append(films)

# movies_to_watch = [(movie.getText().split()[0]) for movie in soup.find_all(name='h3', class_="title")]

movies_to_watch.reverse()

with open('movies.txt', 'w') as f:
    for movie in movies_to_watch:
        f.write(f"{movie}\n")

