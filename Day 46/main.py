import requests
from bs4 import BeautifulSoup
import os


URL = "https://www.billboard.com/charts/hot-100/"

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888/callback"


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")



billboard_response = requests.get(url=f"{URL}{date}/")
print(f"{URL}{date}/")

billboard_webpage =billboard_response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')

dummy_variable = soup.select(selector='div ul li ul li h3')
song_names = []
artiste_names = []
for h3 in soup.select(selector='div ul li ul li h3'):
    song_names.append(h3.getText().strip('\t\n'))

for h3 in soup.select(selector='div ul li ul li span'):
    artiste_names.append(h3.getText().strip('\t\n'))


print(song_names)
print(artiste_names)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

year = date.split("-")[0]


song_uris = []
for song in song_names:
    result = sp.search(q=f"track: {song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} cant be found on Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)