

#these are for the server (calling api and parsing)
# from flask import Flask
# from flask_cors import CORS
from flask import session
import json
from requests import get,post,put
import base64
from urllib.parse import urlencode
import db
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
    spotify_id = ""
    ##call db for spotify id using passed in user_id
        #at this point it should always return an id
    return spotify_id

def get_token_from_db(user_id):
    token=""
    #call db for access token using user_id
        #at this point it should always return a token
    return token

def refresh_the_token(refresh_token):
    endpoint = "https://accounts.spotify.com/api/token"

    # print(session.get('refresh_token'))
    # print("Access" + session.get('access_token'))
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
    # print(results)

    if response.status_code == 200:
        #update the access token and refresh token for that user
        return results["access_token"]
    else :
        return None



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

    #will only continue if we receive a successful call, returns the access token
    '''
        This is how we receive the response.content
        {
            "access_token": token,
            "token_type":"Bearer",
            "expires_in":3600
        }
    '''
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

    # print(tmp[0]["album"]["images"][0])
    # print(tmp[0]["external_urls"])
    # print(tmp[0]["id"])
    return results

def get_spotify_id():

    refresh_the_token()

    endpoint = "https://api.spotify.com/v1/me"
    
    header = {
        "Authorization" : f"Bearer {session.get('access_token')}"
    }

    response = get(endpoint,headers=header)

    response = json.loads(response.content)



    print(response)

    return response['id']

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
    # session["access_token"]=results["access_token"]
    # session["refresh_token"]=results["refresh_token"]
    # access_token = results["access_token"]
    # refresh_token = results["refresh_token"]

    # user_id = get_user_id(access_token,refresh_token)

    access_token = results["access_token"]
    refresh_token = results["refresh_token"]

    '''
        set access_token, refresh token here

        extract userID from db 
    '''

    access_token = refresh_the_token(refresh_token)
    print("after refresh token")

    id_endpoint = "https://api.spotify.com/v1/me"
    
    id_header = {
        "Authorization" : f"Bearer {access_token}"
    }

    id_response = get(id_endpoint,headers=id_header)

    id_result = json.loads(id_response.content)

    print(id_result["id"])

    return

def create_empty_playlist(user_id,sentence):

    endpoint = f'https://api.spotify.com/v1/users/{get_spotify_id(user_id)}/playlists'
    header = {
        "Authorization": f"Bearer {get_token_from_db(user_id)}",
        "Content-Type": "application/json"
    }
    data={
        "name" : f"{sentence}",
        "description":"",
        "public":"true"
    }

    request = post(url=endpoint,headers=header,params=data)
    results=json.loads(request.content)
    return results["id"]


def send_playlist(list):
   
   playlist_id = create_empty_playlist()
   print("after get playlist id")
   return
#    endpoint = f"https://api.spotify.com/v1/playlists/{id}/tracks"


#    header = {
#        "Authorization": f"Bearer {session.get("access_token")}",
#        "Content-Type": "application/json"
#    }

#    data = {
       
#    }




   

