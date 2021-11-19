import sys

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
client_id = '79565d5166ad491fae2a051f73e2650b'
client_secret = 'd9dc05c83d8f44cdb76f04b546e813ea'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])
#
#
#
# results = spotify.artist_top_tracks(lz_uri)
#
# for track in results['tracks'][:10]:
#     print('track    : ' + track['id'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()
#



name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist["followers"]["total"])
    print(artist['name'], artist['images'][0]['url'])

for item in items:
    print("Name : {0}, Popularity : {1}".format(item["name"], item["popularity"]))

# playlists = spotify.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = spotify.next(playlists)
#     else:
#         playlists = None