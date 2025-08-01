
#these are for the server (calling api and parsing)
import calls,db
from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import json
from db import get_db
from requests import get,post,put
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')

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
    sentence = "Zombieboy Happy Fun Juno"
    sentenceTree = []
    words = sentence.split(" ")
    #this is where we will make the tree? for the sentence breakdown

    #this will be the list that we continuously add to while we make the playlist
    results = []

    for word in words:
        #print(word)

        #check db
        db = get_db()
        song_matches_from_db = db.execute('SELECT name FROM songs WHERE name = ?',
        (word,)).fetchall()

        #if song is found then this will skip to the next word
        if len(song_matches_from_db) > 0:
            print("song found in db")

            #adding to create a results list to return
            results.append(song_matches_from_db)

            continue

        else:
            #call the api
            print(calls.search_for_song(word))
            returned_songs = calls.search_for_song(word)

            # add the new song to the database
            db.execute('INSERT INTO songs (name, url, id) VALUES (?, ?, ?)', 
                       (returned_songs["name"], returned_songs["url"], returned_songs["id"]))
            db.commit()
            results.append(returned_songs)

            # this might not work so i commented it out for now. feel free to fix it idk 
            #if returned_songs is not None:
            #    continue
            #else
                #go up to next node to include the following in search
                #if we go the whole phrase unable to find a match
                    #return unable to make playlist
    print(results)
    
    return

@app.route('/getSong',methods=['GET'])
def getSong():
    #songObject = calls.callSong()
    return



