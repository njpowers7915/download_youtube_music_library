import requests
import json

#To Do's...add date range for date added to one of my playlists
#Convert to PHP

def get_user():
    user = input('Enter Channel ID: ').lower().replace(' ', '')
    if user in ['me', 'mine', 'nick', 'nickpowers']:
        user = 'UCGapcX9oYfWQ_mM6SRcXadw'
    return user

def api_request(id_type, endpoint, id, page_token=None):
    url = 'https://www.googleapis.com/youtube/v3/' + endpoint
    #global page_token
    response = requests.get(
        url,
        params={
            'key': 'AIzaSyChVZH1w2JTiYkdmO3vii28BT-geJ25nDs',
            'part': 'snippet',
            id_type: id,
            'pageToken': page_token
        }
    )
    result = json.loads(response.text)
    return result

def get_playlists(channel_id, page_token=None):
    result = api_request('channelId', 'playlists', channel_id, page_token)

    for playlist in result['items']:
        title = playlist['snippet']['localized']['title']
        id = playlist['id']
        print(title + ' : ' + id)
        playlists_dict[title] = id
    try:
        page_token = result['nextPageToken']
        get_playlists(channel_id, page_token=page_token)
    except:
        pass

def get_tracks(playlist_id, page_token=None):
    result = api_request('playlistId', 'playlistItems', playlist_id, page_token)

    for track in result['items']:
        id = track['id']
        title = track['snippet']['title']
        playlist_id = track['snippet']['playlistId']
        date_added = track['snippet']['publishedAt']
        video_id = track['snippet']['resourceId']['videoId']
        video_url = 'http://www.youtube.com/watch?v=' + video_id
        print('\n')
        print(json.dumps(track))
        #print('\n')

        tracks_dict[id] = {
            'title': title,
            'playlist_id': playlist_id,
            'date_added': date_added,
            'url': video_url
            }
    try:
        page_token = result['nextPageToken']
        get_tracks(playlist_id, page_token=page_token)
    except:
        pass

def get_artist_channel(track_id):
    result = api_request('id', 'videos', track_id)

    artist_id = result['items']['snippet']['channelId']
    return artist_id

def get_artist(artist_id):
    result = api_request('id', 'channels', artist_id)

    artist_name = result['items'][0]['snippet']['title']
    print(artist_name)

page_token = None
channel_id = get_user()

playlists_dict = {}
tracks_dict = {}
get_playlists(channel_id)
for playlist_id in playlists_dict.values():
    page_token = None
    get_tracks(playlist_id)
'''


playlists_dict = {'LA': 'PLMe82geRCZIP5Htj2mmwkAtYDA4BUxl_P'}


page_token = None
get_artist_channel('IzR_wNY7kXg')
'''
page_token = None
get_artist('UCaiezXO8LnkG6S9b6ABXJ1w')
'''
#print(tracks_dict)
for track in tracks_dict.values():
    print(track['title'])
    #print(track['url'])
    print('\n')
'''
