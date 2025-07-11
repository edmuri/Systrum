

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

# @app.route('/')
# def root():
#     return 
# '''
# Hello
# '''

def get_auth_code():
    query_url = "https://accounts.spotify.com/authorize?"
    query_string ={
        "response_type": 'code',
        "client_id": ID,
        "redirect_uri":Redirect,
    }
    full_query_url = query_url + urlencode(query_string)
    response = get(full_query_url)
    print(response.url)

# @app.route('/getSong',methods=['GET'])
def callSong():
    # first check the database
        
    return



