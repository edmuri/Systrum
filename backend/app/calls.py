

#these are for the server (calling api and parsing)
# from flask import Flask
# from flask_cors import CORS
from flask import request,jsonify
import json
from requests import get,post,put

#these two allow us to get the api keys from the env file
import os
from dotenv import load_dotenv

# app = Flask(__name__)

# CORS(app)

#fetching the api credentials for the calls
load_dotenv()
ID = os.getenv('clientID')
Secret = os.getenv('clientSecret')


# @app.route('/')
# def root():
#     return 
# '''
# Hello
# '''

# @app.route('/getSong',methods=['GET'])
def callSong(genre = None):
    # first check the database
        
    return



