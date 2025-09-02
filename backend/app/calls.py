

#these are for the server (calling api and parsing)
# from flask import Flask
# from flask_cors import CORS
# from flask import session
import json
from requests import get,post,put
import base64
from urllib.parse import urlencode
from db import get_db


#these two allow us to get the api keys from the env file
import os
from dotenv import load_dotenv

# app = Flask(__name__)

# CORS(app)

#fetching the api credentials for the calls
load_dotenv()
ID = os.getenv('clientID')
Secret = os.getenv('clientSecret')
Redirect = "http://127.0.0.1:5000/callback"

'''
Result 200: ALL GOOD
Result 401: Bad or Expired Token
Result 403: Forbidden - Bad OAth Request (when using client credentials instead of access token
                                            scope incorrect)
Result 429: Too Many Requests 
'''

def encode_to_64(string):
    bytes_version = string.encode('utf-8')
    encoded = str(base64.b64encode(bytes_version), "utf-8")
    return encoded

def get_id_from_db(user_id):
    db=get_db()
    spotify_id = db.execute('SELECT spotify_id FROM tokens WHERE user_id = ?',
                            (user_id,)).fetchone()
    return spotify_id

def get_token_from_db(user_id):
    db=get_db()
    token = db.execute('SELECT access_token FROM tokens WHERE user_id = ?',
                            (user_id,)).fetchone()
    return token

def refresh_token(user_id):
    endpoint = "https://accounts.spotify.com/api/token"

    '''
    ACCESS DB FOR refresh token
    
    '''
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization":f"Basic {encode_to_64(ID + ':' + Secret)}"
    }
    data = {
        "grant_type":"refresh_token",
        "refresh_token":refresh_token,
    }

    response = post(url=endpoint, headers=headers, data=data)
    results = json.loads(response.content)

    if response.status_code == 200:
        #update the access token and refresh token for that user
        # return results["access_token"]
        return 200
    else:
        return 403


'''
    get_client_credentials: gets the access token that allows us to access public 
                            non-user specific information.
    parameters - NONE
    returns - access token acquired from the api call
'''
def get_client_credentials():
    #endpoint that will get us the access token
    endpoint = "https://accounts.spotify.com/api/token"

    #string needs to be encoded in base64 as per spotify documentation
    #this is where i build the final full string that gets passed into the call
    access_string =ID + ":" + Secret
    query_string = str(base64.b64encode(access_string.encode("utf-8")), "utf-8")
    full_string =  "Basic " + query_string

    query_data = {
        "grant_type":"client_credentials"
    }

    query_header = {
        "Authorization" : full_string,
        "Content-Type":"application/x-www-form-urlencoded"
    }

    #call
    response = post(endpoint,headers=query_header,data=query_data)

    
    '''
        This is how we receive the response.content
        {
            "access_token": token,
            "token_type":"Bearer",
            "expires_in":3600
        }
    '''
    #will only continue if we receive a successful call, returns the access token
    if response.status_code == 200:
        response_content = json.loads(response.content)
        # print(response_content)
        token = (response_content)['access_token']
        # print(token)
        return token
    else:
        print("Error receiving access token")
        return None

'''
    search_for_song: calls the spotify api to search for a song matching the given name
    parameters - the name of the song that will be searched for
    returns - an json object that will contain the spotify link, song name, spotify id for song

    This will be eventually changed slightly to incorporate filtering
'''
'''
    return will look as follows 

    {
     "name" : "Zombieboy",
     "url" : "http://spotify.com/zombieboy",
     "id" : fhhjwis1242
     "artist" : Lady Gaga,
     "cover" : "http://spotify.com/cover",
     "album" : "MAYHEM"
    }
'''
def search_for_song(name):
    token = get_client_credentials()

    if token == None:
        print("Token not properly returned")
        return None
        
    endpoint = "https://api.spotify.com/v1/search"

    # looks for the first track with a matching name
    data = {
        "q" : name,
        "type": "track",
        "limit":1
    }
    header = {
        "Authorization" : f"Bearer {token}"
    }

    response = get(endpoint,params=data,headers=header)
    song_result = json.loads(response.content)
    
    if response.status_code != 200:
        return None

    tmp = song_result["tracks"]["items"]
    # print(name)

    url = tmp[0]["external_urls"]["spotify"]
    albumCover = tmp[0]["album"]["images"][0]['url']
    id = tmp[0]["id"]
    artist = tmp[0]['artists'][0]['name']
    album = tmp[0]["album"]['name']

    results = {
        "name":name,
        "artist": artist,
        "album" : album,
        "cover": albumCover,
        "url":url,
        "id":id
    }

    return results

'''
    This is called to construct the url that users will be redirected 
    to in order to authorize the spotify connection. This will not do anything else directly,
    but when the user comes back from authorizing it is taken to set_user_token
'''
def authorize_user():
    scope = "playlist-modify-public user-read-private"
    
    endpoint = "https://accounts.spotify.com/authorize?"

    query_string = {
        "response_type":'code',
        "client_id":ID,
        "scope":scope,
        "redirect_uri":Redirect
    }

    full_query = endpoint + urlencode(query_string)
    
    response = get(full_query)
    return response.url

'''
    This is where the user is redirected to once they authorize the spotify interaction.
    It calls the api with the authorization code to get the access token, refresh token, and the
    spotify id to store in the sql db for future use

    it returns the user_id from the new sql addition to main.py
'''
def set_user_token(code):
    
    endpoint = "https://accounts.spotify.com/api/token"

    data = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":Redirect
    }

    Authorization = encode_to_64(ID + ":" + Secret)

    header = {
        "Authorization": "Basic " + Authorization,
        "Content-Type":"application/x-www-form-urlencoded"
    }
    print("Trying to get access code")
    response = post(url=endpoint, params=data, headers=header)
   
    results = json.loads(response.content)

    access_token = results["access_token"]
    refresh_token = results["refresh_token"]

    # Start getting the spotify accout id 
    id_endpoint = "https://api.spotify.com/v1/me"
    
    id_header = {
        "Authorization" : f"Bearer {access_token}"
    }

    id_response = get(id_endpoint,headers=id_header)

    id_result = json.loads(id_response.content)

    spotify_id = id_result["id"]

    db=get_db()
    db.execute('INSERT INTO tokens (access_token, refresh_token, spotify_id, is_logged_in) VALUES (?,?,?,?)',
                            (access_token,refresh_token,spotify_id,1))
    db.commit()
    user_id = db.execute('SELECT user_id FROM tokens WHERE spotify_id = ?', (spotify_id,)).fetchone()
    

    # return user_id
    return user_id[0]

'''
    This is called from the send_playlist function and returns a playlist id to the calling function
    It creates a playlist with the name of the sentence
'''
def create_empty_playlist(user_id,sentence):

    endpoint = f'https://api.spotify.com/v1/users/{get_id_from_db(user_id)}/playlists'
    header = {
        "Authorization": f"Bearer {get_token_from_db(user_id)}",
        "Content-Type": "application/json"
    }
    data={
        "name" : f"{sentence}",
        "description":"Playlist made from Systrum",
        "public":"true"
    }

    request = post(url=endpoint,headers=header,params=data)
    results=json.loads(request.content)
    return results["id"]

'''
    This is what we will use to create the playlist for the user and send it to their account
    The platlist id is created and we iterate through all the elements of the sent playlist
'''
def send_playlist(user_id, list):
   sentence = list["sentence"]
   playlist_id = create_empty_playlist(user_id, sentence)
   
   endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"


   header = {
       "Authorization": f"Bearer {get_token_from_db(user_id)}",
       "Content-Type": "application/json"
   }

   data = {
       "uris": list["songs"]
   }


   response = post(endpoint, headers=header, params=data)

   return




   

