

#these are for the server (calling api and parsing)
# from flask import Flask
# from flask_cors import CORS
from flask import request,jsonify,session
import json
from requests import get,post,put
import base64
from urllib.parse import urlencode



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

def encode_to_64(string):
    bytes_version = string.encode('utf-8')
    encoded = base64.b64encode(bytes_version)
    return encoded

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

def get_user_profile():

    token = get_client_credentials()

    endpoint = "https://api.spotify.com/v1/me"
    
    header = {
        "Authorization" : f"Bearer {token}"
    }

    response = get(endpoint,headers=header)

    response = json.loads(response.content)

    print(response)

    return

def authorize_user():
    scope = "playlist-modify-public"
    
    endpoint = "https://accounts.spotify.com/authorize?"

    query_string = {
        "response_type":'code',
        "client_id":ID,
        "scope":scope,
        "redirect_uri":Redirect
    }

    full_query = endpoint + urlencode(query_string)
    
    response = get(full_query)
    print(response.url)

def set_user_token(code):
    
    endpoint = "https://accounts.spotify.com/api/token"

    data = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":Redirect
    }

    Authorization = encode_to_64(ID + ":" + Secret)

    header = {
        "Authorization": Authorization,
        "Content-Type":"application/x-www-form-urlencoded"
    }

    response = post(url=endpoint, params=data, headers=header)
    print("Trying to get access code")
    print(response.content)


    return

