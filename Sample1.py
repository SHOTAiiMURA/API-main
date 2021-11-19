import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '79565d5166ad491fae2a051f73e2650b'
client_secret = 'd9dc05c83d8f44cdb76f04b546e813ea'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'rihanna'
result = spotify.search(q='artist:' + name, type='artist')
print(result)

for i in result['artists']['items']:
    print("{0} popularity: {1}".format(i['name'], i['popularity']))

result = spotify.artist_related_artists(result['artists']['items'][0]['id'])
for artist in result['artists']:
    artist_name = artist['name']
    popularity = artist['popularity']
    unique_id = artist['id']
    print("{0} - popularity: {1}, id: {2}".format(artist_name, popularity, unique_id))


playlists = spotify.user_playlists('v4y6oq2f0hhoeynqx68xsxrvo')
for item in playlists["items"]:
    playlist_id = item["id"]

#
# name = 'YOASOBI'
#
# results = spotify.search(q='artist:' + name, type='artist')
# artist_id = results['artists']['items'][0]["id"]
#
# tracks = spotify.artist_top_tracks(artist_id)["tracks"]
# for item in tracks:
#     for subItem in item:
#         print(subItem)
#
# for i in range(len(spotify.artist_top_tracks(artist_id)["tracks"])):
#     print(tracks[i])
#     print("{0} :  {1}, id : {2}".format(tracks[i]["name"] ,tracks[i]["artists"][0]["name"], tracks[i]["uri"]))
#
# # for item in results['artists']['items'][0]["id"]:
# #     print(item)
# items = results['artists']['items']
# # if len(items) > 0:
# #     artist = items[0]
# #     spotify.artist_top_tracks(artist)
# #     print(artist['name'], artist['images'][0]['url'])
#
