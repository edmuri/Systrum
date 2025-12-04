'''
This is the file I used to test all the spotify api calls.
I made this over a year ago and have been using this to test since its all through the
terminal and it makes it way easier to use the calls. 

'''


import os
import base64
import json
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from requests import post,get,put
import webbrowser
import time

'''
Additional class that allows me to authorize my log in and get the authorization code for the calls

This opens up a window and takes the url, then parses it to get the info I need
'''
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if 'code' in query_params:
            auth_code = query_params['code'][0]
            print(f"Authorization code received: {auth_code}")

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Authorization successful! You can close this window.')

            results = get_Codes(auth_code)
            mainCalls(results['access_token'],results['refresh_token'])

        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        return 

def start_server():
    server_address = ('', 5000) 
    httpd = HTTPServer(server_address, RequestHandler)
    print('Waiting for the callback from Spotify...')
    httpd.serve_forever()

#works with client credentials
def get_Codes(authorizationCode):
    print("IN GET CODES\n\n\n\n")
    auth_string = clientID + ":" + clientSecret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": authorizationCode,
        "redirect_uri":redirectURL
    } 
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    print(json_result)
    return json_result


def get_token_info():
    print("Get token info\n\n\n\n")
    authURL = "https://accounts.spotify.com/authorize?"
    query_string = {
        "client_id": clientID,
        "response_type": "code",
        "redirect_uri": redirectURL,
        "scope": "user-top-read streaming user-read-playback-state user-modify-playback-state",
    }
    query_url = authURL + urlencode(query_string)
    response = get(query_url)
    print("RESPONSE\n\n")
    print(response.url)
    webbrowser.open(query_url)

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "http://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result)==0:
        print("No Artist Found")
        return None
    return json_result[0]

def get_songs_by_artist(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?&country=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_top_songs(token):
    url = "https://api.spotify.com/v1/me/top/tracks?limit=10"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)
    print("HELLLOOOOOO\n\n\n")
    print(json_result["items"][0]["album"]['name'])
    print("\n")
    print(json_result["items"][0]['artists'][0]['id'])

    return json_result["items"]

def getCurrSong(token):
    url = "https://api.spotify.com/v1/me/player"
    headers = get_auth_header(token)
    result=get(url,headers=headers)

    if(result.status_code == 204):
        return "none"
    else:
        json_result = json.loads(result.content)
        print(json_result)
        result = json_result["item"]
        return result

def skipSong(token):
    url = "https://api.spotify.com/v1/me/player/next"
    headers = get_auth_header(token)
    result = post(url,headers=headers)

def resumeSong(token):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = get_auth_header(token)
    result = put(url,headers=headers)

def pauseSong(token):
    url = "https://api.spotify.com/v1/me/player/pause"
    headers = get_auth_header(token)
    result = put(url,headers=headers)

def StartResumePlayback(token):
    url = "https://api.spotify.com/v1/me/player/play"

def getArtistGenre(token):
    url="https://api.spotify.com/v1/artists/"

    headers = get_auth_header(token)

    # Gaga Spotify ID
    GagaID = "1HY2Jd0NmPuamShAr6KMms"

    full_url = url+GagaID
    response = get(full_url,headers=headers)

    result = json.loads(response.content)
    print(result['genres'])
    # print(result)



def mainCalls(token, refreshToken):
    selection = 9
    while(selection!=0):
        selection = menu()
        print(f"SELECTION CHOSEN :{selection}")

        match selection:
            case 1: 
                userTopSongs=get_top_songs(token)
                print("\n")
                for idx,song in enumerate(userTopSongs):
                    print(f"{idx+1}. {song['album']['name']}: {song['name']}")
                print("\n")
                # for int,song in enumerate(userTopSongs):
                #     print(f"{song['album']['images'][0]['url']}")
            case 2:
                print(getCurrSong(token))
            case 3:
                skipSong(token)
            case 4:
                resumeSong(token)
            case 5:
                pauseSong(token)
            case 6:
                getArtistGenre(token)

    print("Thank you")

#MENU FOR TESTING PURPOSES, WILL REMOVE FOR FURTHER IMPLEMENTATIONS
def menu():
    print("Please select from the menu:\n")
    print("1. Top Songs")
    print("2. Print Current Song")
    print("3. Skip Song")
    print("4. Resume Song")
    print("5. Pause Song")
    print("6.Genre")
    selection = int(input("Selection: "))
    return selection

def main():
    get_token_info()
    start_server()

if __name__ == "__main__":
    main()