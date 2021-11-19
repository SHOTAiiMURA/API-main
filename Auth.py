import spotipy
import spotipy.util as util

scope = "playlist-modify-private playlist-modify-public"
token = util.prompt_for_user_token(
    'v4y6oq2f0hhoeynqx68xsxrvo',
    scope,
    client_id='79565d5166ad491fae2a051f73e2650b',
    client_secret='d9dc05c83d8f44cdb76f04b546e813ea', redirect_uri='http://localhost:8888')

spotify = spotipy.Spotify(auth=token)
print('ok')

# spotify.user_playlist_create('v4y6oq2f0hhoeynqx68xsxrvo', "Spotify API Test")

#
# playlists = spotify.user_playlists('v4y6oq2f0hhoeynqx68xsxrvo')
# for item in playlists["items"]:
#     playlist_id = item["id"]
#     print("Name {0}, id {1}".format(item["name"], item["id"]))
#
# # `MGMT`のアーティスト検索を実行
# target = 'YOASOBI'
# result = spotify.search(q='artist:' + target, type='artist', limit=10)
# for item in result['artists']['items']:
#     # 名前が完全一致するアーティストを採用
#     if item['name'].lower() == target.lower():
#         spotify.user_follow_artists([item['id']])
#         print('アーティスト`{}`[id={}]をフォローしました'.format(item['name'], item['id']))

# playlists = sp.user_playlists('v4y6oq2f0hhoeynqx68xsxrvo')
# for item in playlists["items"]:
#     print(item["id"])
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
#
# print(sp.current_user_playlists())

# # Get playlist id here
# playlist_name = "Spotify API Test"
# user_name = 'v4y6oq2f0hhoeynqx68xsxrvo'
#
# playlists = spotify.user_playlists(user_name)
# for item in playlists["items"]:
#     if item["name"] ==playlist_name:
#         playlist_id = item["id"]
#
# # Search for artist
# name = 'YOASOBI'
# results = spotify.search(q='artist:' + name, type='artist')
# # Get artist id here
# artist_id = results['artists']['items'][0]["id"]
#
# # Get top tracks of specified artist
# tracks = spotify.artist_top_tracks(artist_id)["tracks"]
# playlist_id = playlists["items"][0]["id"]
#
# # Make song list
# songs = []
# for i in range(len(spotify.artist_top_tracks(artist_id)["tracks"])):
#     print("{0} :  {1}, id : {2}".format(tracks[i]["name"] ,tracks[i]["artists"][0]["name"], tracks[i]["uri"]))
#     # Add song to list
#     songs.append(tracks[i]["uri"])
# print(songs)
#
# # Add song list to playlist
# spotify.playlist_add_items(playlist_id, songs)

playlist = spotify.new_releases(country="JP")
for items in playlist["albums"]["items"]:
    print("Artist : {0}, Song : {1}, Release_Date :{2}".format(items["artists"][0]["name"], items["name"], items["release_date"]))
print(playlist)