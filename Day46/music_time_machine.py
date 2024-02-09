from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv(dotenv_path=Path("./Day46/.env"))

timeframe = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{timeframe}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in songs]

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"), client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"), 
                                               scope=scope, redirect_uri="http://example.com", cache_path='./Day46/token.txt'))

user_id = sp.current_user()['id']

song_uris = []
for song in song_titles:
    song_search = sp.search(q=f"track:{song} year:{timeframe[:4]}", type="track")
    try:
        uri = song_search['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{timeframe} Billboard 100", public=False, description=f"Billboard Top 100 songs for week of {timeframe}")
playlist_id = playlist['id']
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uris)