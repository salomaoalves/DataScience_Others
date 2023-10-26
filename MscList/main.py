import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import config

# # Variables
CLIENT_ID = config.client_id
CLIENT_SECRET = config.client_secret
SCOPE = config.scope
USER = config.username
REDIRECT_URI = config.redirect_uri

def connect(scope=''):

    # Authentication
    with_user = True
    try:
        if not with_user:
            sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, 
                                                                                        client_secret=CLIENT_SECRET))
        else:
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri=REDIRECT_URI,
                                                            scope=scope))
    except:
        print('Unable to connect with Spotify')
    return sp

def get_uri(link):
    '''
        @link: str, a open/spotify link'''
    playlist_URI = link.split("/")[-1].split("?")[0]
    return playlist_URI

def playlist_info(playlist_link):
    sp = connect(scope = 'playlist-read-private')
    playlist_URI = get_uri(playlist_link)
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        #URI
        track_uri = track["track"]["uri"]
        print(track_uri)

        #Track name
        track_name = track["track"]["name"]
        print(track_name)
        
        #Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        print(artist_uri)
        artist_info = sp.artist(artist_uri)
        print(artist_info)
        
        #Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        print(artist_name)
        artist_pop = artist_info["popularity"]
        print(artist_pop)
        artist_genres = artist_info["genres"]
        print(artist_genres)
        
        #Album
        album = track["track"]["album"]["name"]
        print(album)
        
        #Popularity of the track
        track_pop = track["track"]["popularity"]
        print(track_pop)

playlist_link = "https://open.spotify.com/playlist/4bJUhMPraAFAKpZjnHtJw3"
#playlist_info(playlist_link)



# # sp = connect()
# # results = sp.current_user_saved_tracks()
# # for idx, item in enumerate(results['items']):
# #     #track = item['track']
# #     print(item)
# #     #print(idx, track['artists'][0]['name'], " – ", track['name'])
# #     input()
# # playlists = sp.user_playlists('spotify')
# # while playlists:
# #     for i, playlist in enumerate(playlists['items']):
# #         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
# #     if playlists['next']:
# #         playlists = sp.next(playlists)
# #     else:
# #         playlists = None

def get_playlist_info():
    sp = connect(scope = 'playlist-read-private')
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        desc = item['description']
        size = item['tracks']['total']
        name = item['name']
        url = item['external_urls']['spotify']


ranges = ['short_term', 'medium_term', 'long_term']

sp = connect(scope = 'user-top-read')
for sp_range in ['long_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=50)

    for i, item in enumerate(results['items']):
        print(i, item['name'])
    input()