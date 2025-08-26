# main.py - FIXED VERSION
import calls, db
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify, session, redirect
import json
from db import get_db
from requests import get, post, put
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Add this for sessions

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')

# Initialize database with app
db.init_app(app)

CORS(app, origins=["http://localhost:3000"])  # Allow your frontend

# Create the node class that will hold the word and combinations
class Node:
    def __init__(self, words):
        left = None
        right = None
        parent = None
        sentence = words

@app.route('/')
def root():
    return "Systrum Backend is running!"

@app.route('/createPlaylist', methods=['GET'])
def generatePlaylist():
    sentence = request.args.get('sentence')
    
    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400
    
    print(f"Creating playlist for: {sentence}")

    sentenceTree = []
    words = sentence.split(" ")
    results = []

    for word in words:
        print(f"Processing word: {word}")
        
        # Check db
        db_conn = get_db()
        song_matches_from_db = db_conn.execute(
            'SELECT name, artist, album_name, id, url FROM songs WHERE name = ?',
            (word,)
        ).fetchall()

        # If song is found in database
        if len(song_matches_from_db) > 0:
            print("Song found in database")
            
            artist = song_matches_from_db[0]['artist']
            album = song_matches_from_db[0]['album_name']

            cover = db_conn.execute(
                'SELECT link FROM covers WHERE artist = ? AND album_name = ?',
                (artist, album,)
            ).fetchone()
            
            formatted_db_result = {
                "name": song_matches_from_db[0]['name'],
                "artist": artist,
                "album": album,
                "cover": cover[0] if cover else "https://via.placeholder.com/300x300?text=No+Cover",
                "url": song_matches_from_db[0]['url'],
                "id": song_matches_from_db[0]['id']
            }
            results.append(formatted_db_result)
            continue

        else:
            # Call the API
            print("Calling Spotify API")
            returned_songs = calls.search_for_song(word)
            
            if returned_songs is None:
                print(f"No song found for word: {word}")
                continue
            
            # Add the new song to the database
            db_conn.execute(
                'INSERT INTO songs (name, url, id, artist, album_name) VALUES (?, ?, ?, ?, ?)', 
                (returned_songs["name"], returned_songs["url"], returned_songs["id"], 
                 returned_songs["artist"], returned_songs["album"])
            )
            db_conn.commit()

            # Check if album cover has already been added to covers table
            cover_matches_from_db = db_conn.execute(
                'SELECT link FROM covers WHERE artist = ? AND album_name = ?',
                (returned_songs["artist"], returned_songs["album"],)
            ).fetchone()
            
            # If not found, create a new entry
            if cover_matches_from_db is None or len(cover_matches_from_db) == 0:
                db_conn.execute(
                    'INSERT INTO covers (album_name, artist, link) VALUES (?, ?, ?)',
                    (returned_songs["album"], returned_songs["artist"], returned_songs["cover"])
                )
                db_conn.commit()

            results.append(returned_songs)

    print(f"Generated playlist with {len(results)} songs")
    return jsonify(results), 200

@app.route('/authorizeUser', methods=['GET'])
def authorize():
    link = calls.authorize_user()
    return redirect(link)

@app.route('/callback', methods=['GET'])  # Changed from POST to GET
def handle_callback():
    code = request.args.get("code")
    calls.set_user_token(code)
    return redirect('http://localhost:3000/CreatePlaylist')

@app.route('/sendPlaylist', methods=['POST'])
def send_playlist():
    user_id = request.args.get("id")
    list_data = request.json["playlist"]  # Use request.json instead of request["playlist"]
    calls.send_playlist(user_id, list_data)
    return jsonify({"success": True}), 200

# Add this to actually run the server
if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        try:
            db.init_db()
            print("Database initialized")
        except Exception as e:
            print(f"Database already exists or error: {e}")
    
    print("Starting Systrum Backend Server...")
    print("Backend will be available at: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

# #these are for the server (calling api and parsing)
# import calls,db
# from flask import Flask
# from flask_cors import CORS
# from flask import request,jsonify,session,redirect
# import json
# from db import get_db
# from requests import get,post,put
# import os
# from dotenv import load_dotenv

# app = Flask(__name__)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# app.config['DATABASE'] = os.path.join(BASE_DIR, 'database.db')

# CORS(app)

# #create the node class that will hold the word and combinations

# class Node:
#     def __init__(self, words):
#         left = None
#         right = None
#         parent = None
#         sentence = words

# @app.route('/')
# def root():
#     return ""

# '''
# This is the main function that does most of the calling to api and construction of playlists
# '''
# @app.route('/createPlaylist', methods=['GET'])
# def generatePlaylist():
#     sentence = request.args.get('sentence')
#     # print(sentence)

#     sentenceTree = []
#     words = sentence.split(" ")
#     #this is where we will make the tree? for the sentence breakdown

#     #this will be the list that we continuously add to while we make the playlist
#     results = []

#     for word in words:
#         #print(word)

#         #check db
#         db = get_db()
#         song_matches_from_db = db.execute('SELECT name,artist,album_name,id,url FROM songs WHERE name = ?',
#         (word,)).fetchall()

#         #if song is found then this will skip to the next word
#         if len(song_matches_from_db) > 0:
#             print("song found in db")

#             #adding to create a results list to return
#             # need to 
#             # results.append([song_matches_from_db[0]['name'],song_matches_from_db[0]['url']])
#             artist = song_matches_from_db[0]['artist']
#             album = song_matches_from_db[0]['album_name']

#             cover = db.execute('SELECT link FROM covers WHERE artist = ? AND album_name = ?',
#                                                (artist, album,)).fetchone()
            
#             formatted_db_result = {
#                 "name":song_matches_from_db[0]['name'],
#                 "artist": artist,
#                 "album" : album,
#                 "cover": cover[0],
#                 "url":song_matches_from_db[0]['url'],
#                 "id":song_matches_from_db[0]['id']
#              }
#             results.append(formatted_db_result)

#             continue

#         else:
#             #call the api
#             # print(calls.search_for_song(word))
#             print("calling api")
#             returned_songs = calls.search_for_song(word)
            
#             # add the new song to the database
#             db.execute('INSERT INTO songs (name, url, id, artist, album_name) VALUES (?, ?, ?, ?, ?)', 
#                        (returned_songs["name"], returned_songs["url"], returned_songs["id"], 
#                         returned_songs["artist"], returned_songs["album"]))
#             db.commit()

#             # check if album cover has already been added to covers table
#             cover_matches_from_db = db.execute('SELECT link FROM covers WHERE artist = ? AND album_name = ?',
#                                                (returned_songs["artist"], returned_songs["album"],)).fetchone()
            
#             # if not found, we create a new entry.
#             if cover_matches_from_db == None or len(cover_matches_from_db) == 0:
#                 db.execute('INSERT INTO covers (album_name, artist, link) VALUES (?, ?, ?)',
#                            (returned_songs["album"], returned_songs["artist"], returned_songs["cover"]))
#                 db.commit()

#             results.append(returned_songs)

#     # calls.send_playlist(results)
    
#     return jsonify(results),200

# '''
# Call that leads to users being redirected to spotify's authentication
# '''
# @app.route('/authorizeUser',methods=['GET'])
# def authorize():
#     link = calls.authorize_user()
#     return redirect(link)

# '''
# This sets the authentication code that will lead to the user's access code being set and redirected
# back to Systrum page
# '''
# @app.route('/callback', methods=['POST'])
# def handle_callback():
#     code = request.args.get("code")
#     calls.set_user_token(code)
#     return redirect('http://localhost:3000/CreatePlaylist')

# @app.route('/sendPlaylist',methods=['POST'])
# def send_playlist():
#     user_id = request.args.get("id")
#     list = request["playlist"]
#     calls.send_playlist(user_id, list)

#     return




