
#these are for the server (calling api and parsing)
import calls,db
from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import json
from requests import get,post,put

app = Flask(__name__)

CORS(app)

#create the node class that will hold the word and combinations

@app.route('/')
def root():
    return


@app.route('/createPlaylist', methods=['GET'])
def createPlaylist():
    sentence = request.sentence

    sentenceTree = []
    words = sentence.split(" ")

    #this is where we will make the tree? for the sentence breakdown

    #for each node with an individual word, check the sql db
    #if returns none, then call the api
    
    return

@app.route('/getSong',methods=['GET'])
def getSong():
    #songObject = calls.callSong()
    return



