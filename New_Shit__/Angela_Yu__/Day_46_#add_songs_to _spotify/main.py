import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from functools import reduce
from json import dump


def remove_space(string):
    for i in string:
        if i == " " or i == "\n" or i == "\t":
            string = string[1:]
        else:
            break
    for i in string[::-1]:
        if i == " " or i == "\n" or i == "\t":
            string = string[:-1]
        else:
            break
    return string


Url = "https://www.billboard.com/charts/hot-100/"
date = input("Enter a date in Y-M-D:- ") or ""
if date:
    date = date + "/"

Url = Url + date

data = requests.get(url=Url)
data.raise_for_status()
data = data.text

soup = BeautifulSoup(data, "html.parser")
clas = "lrv-u-width-100p"

li = soup.find_all(name="li", class_=clas)


with open("music.html", "w") as file:
    file.write(reduce(lambda x, y: str(x) + str(y), li))

h3 = [
    tag.select(selector="ul li h3")[0]
    for tag in li
    if len(tag.select(selector="ul li h3")) != 0
]

unfiltered_song_names = [tag.getText() for tag in h3]
filtered_song_names = [remove_space(i) for i in unfiltered_song_names]
song_names = [
    str(position) + ". " + i for position, i in enumerate(filtered_song_names, start=1)
]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="9ef8421f3cb1480da4f01bc7888a06d4",
        client_secret="e1f94fccac2545ba88fe00e1e80d4d31",
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_list = []
for name in filtered_song_names:
    try:
        data = sp.search(q=f"track:{name} year:{year}", type="track")
        song_list.append(data["tracks"]["items"][0])
        print(name, "Done...")
    except Exception:
        continue
song_uris = [i["uri"] for i in song_list]

with open("song-data.json", "w") as f:
    dump(song_list, f)

user_data = sp.user(user_id)
print(user_data)

user_playlist = sp.user_playlist_create(
    user=user_id, name=f"Songs of {year}", public=False
)

putting_song_to_playlists = sp.user_playlist_add_tracks(
    user=user_id, playlist_id=user_playlist["id"], tracks=song_uris
)

print(putting_song_to_playlists)
