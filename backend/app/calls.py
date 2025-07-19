

#these are for the server (calling api and parsing)
# from flask import Flask
# from flask_cors import CORS
from flask import request,jsonify
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
Redirect = "http://localhost:5000/callback"

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

    print(response)
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

def search_for_song(name):
    token = get_client_credentials()

    if token == None:
        print("No can do!")
        
    endpoint = "https://api.spotify.com/v1/search"

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
        print("None")

    tmp = song_result["tracks"]["items"]
    print(name)
    print(tmp[0]["album"]["images"][0])
    print(tmp[0]["external_urls"])
    print(tmp[0]["id"])
    return
        
    return



