

#these are for the server (calling api and parsing)
import calls
from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import json
from requests import get,post,put

app = Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return 
'''
Hello
'''

@app.route('/getSong',methods=['GET'])
def getSong():
    return



