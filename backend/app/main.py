
#these are for the server (calling api and parsing)
import calls,db
from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import json
from db import get_db
from requests import get,post,put

app = Flask(__name__)

CORS(app)

#create the node class that will hold the word and combinations

class Node:
    def __init__(self, words):
        left = None
        right = None
        parent = None
        sentence = words

@app.route('/')
def root():
    createPlaylist()
    return "ALL DONE"


# @app.route('/createPlaylist', methods=['GET'])
def createPlaylist():
    #this will get changed once we see how data will be communicated
    # sentence = request.data
    sentence = "Zombieboy Happy Fun"
    sentenceTree = []
    words = sentence.split(" ")
    #this is where we will make the tree? for the sentence breakdown



    for word in words:
        print(word)

        #check db
        db = get_db()
        song_matches_from_db = db.execute("SELECT name FROM songs WHERE name = ?"),
        (word,).fetchall()

        if song_matches_from_db is not None:
            continue

        else:
            #call the api
            print(calls.search_for_song(word))
            returned_songs = calls.search_for_song(word)
            if returned_songs is not None:
                continue
            #else
                #go up to next node to include the following in search
                #if we go the whole phrase unable to find a match
                    #return unable to make playlist
    
    return

@app.route('/getSong',methods=['GET'])
def getSong():
    #songObject = calls.callSong()
    return



