
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
    #this will get changed once we see how data will be communicated
    sentence = request.data

    sentenceTree = []
    words = sentence.split(" ")

    #this is where we will make the tree? for the sentence breakdown

    for word in sentenceTree:
        print(word)
        #check db
        #if db returns something
            #continue
        #else
            #call the api
            #if api returns something
                #continue
            #else
                #go up to next node to include the following in search
                #if we go the whole phrase unable to find a match
                    #return unable to make playlist
    
    return

@app.route('/getSong',methods=['GET'])
def getSong():
    #songObject = calls.callSong()
    return



