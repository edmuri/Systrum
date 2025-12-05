
import calls,db
from flask import Flask
from flask_cors import CORS
from flask import request,jsonify,redirect, make_response
import json
from db import get_db
from requests import get,post,put
import os
from dotenv import load_dotenv

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')

CORS(app, supports_credentials=True)

#create the node class that will hold the word and combinations

class Node:
    def __init__(self, words):
        left = None
        right = None
        parent = None
        sentence = words

@app.route('/')
def root():
    return ""

'''
This is the main function that does most of the calling to api and construction of playlists
'''
@app.route('/createPlaylist', methods=['GET'])
def generatePlaylist():
    sentence = request.args.get('sentence')
    # print(sentence)

    sentenceTree = []
    words = sentence.split(" ")
    #this is where we will make the tree? for the sentence breakdown
    sentence = ""
    prevWord = ""
    #this will be the list that we continuously add to while we make the playlist
    results = []

    for word in words:
        # if calls.normalize(word) == 'i':
        #     sentence = 'I'
        #     continue
        
        sentence += ( " " + word)
        print("Sentence",sentence)
        sentence = calls.normalize(word)
        #check db
        #add wildcard
        db = get_db()
        song_matches_from_db = db.execute('SELECT name,artist,album,id,url FROM songs WHERE word LIKE ?',
        (sentence,)).fetchall()

        #if song is found then this will skip to the next word
        if len(song_matches_from_db) > 0:
            # print("song found in db")

            #adding to create a results list to return
            # need to 
            # results.append([song_matches_from_db[0]['name'],song_matches_from_db[0]['url']])
            artist = song_matches_from_db[0]['artist']
            album = song_matches_from_db[0]['album']

            cover = db.execute('SELECT link FROM covers WHERE artist = ? AND album = ?',
                                               (artist, album,)).fetchone()
            
            formatted_db_result = {
                "name":song_matches_from_db[0]['name'],
                "artist": artist,
                "album" : album,
                "cover": cover[0],
                "url":song_matches_from_db[0]['url'],
                "id":song_matches_from_db[0]['id']
             }
            results.append(formatted_db_result)
            sentence=""
            continue

        else:
            #call the api
            # print(calls.search_for_song(word))
            # print("calling api")
            # print(sentence)
            returned_songs = calls.search_for_song(sentence, 0)

            if returned_songs is None:
                if prevWord is not sentence:
                    prevWord = sentence
                    continue
                else:
                    return jsonify({"Message:Cannot find matching playlist"}),400
            
            # add the new song to the database
            db.execute('INSERT INTO songs (word, name, url, id, artist, album) VALUES (?, ?, ?, ?, ?, ?)', 
                       (returned_songs['word'],returned_songs["name"], returned_songs["url"], returned_songs["id"], 
                        returned_songs["artist"], returned_songs["album"]))
            db.commit()

            # check if album cover has already been added to covers table
            cover_matches_from_db = db.execute('SELECT link FROM covers WHERE artist = ? AND album = ?',
                                               (returned_songs["artist"], returned_songs["album"],)).fetchone()
            
            # if not found, we create a new entry.
            if cover_matches_from_db == None or len(cover_matches_from_db) == 0:
                db.execute('INSERT INTO covers (album, artist, link) VALUES (?, ?, ?)',
                           (returned_songs["album"], returned_songs["artist"], returned_songs["cover"]))
                db.commit()

            results.append(returned_songs)
            sentence=""

    # calls.send_playlist(results)
    
    return jsonify(results),200

'''
Call that leads to users being redirected to spotify's authentication
'''
@app.route('/authorizeUser')
def authorize():
    # print("IN AUTH")
    link = calls.authorize_user()
    # print("OUTSITE LINK")
    return redirect(link)

'''
This sets the authentication code that will lead to the user's access code being set and redirected
back to Systrum page
'''
@app.route('/callback')
def handle_callback():
    code = request.args.get("code")
    userID = calls.set_user_token(code)
    # print("INSIDE CALLBACK")
    # print(userID)

    response = make_response(redirect('http://localhost:3000/PlaylistResult'))
    response.headers['user_id'] = userID
    return response

@app.route('/sendPlaylist',methods=['POST'])
def send_playlist():
    user_id = request.args.get("id")
    list = request["playlist"]
    calls.send_playlist(user_id, list)

    return

@app.route('/pullStats',methods=['GET'])
def get_info():
    db.execute("SELECT * FROM DEVS")
    return



