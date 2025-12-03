<div align="center">

</div>

<h1 align="center">Systrum</h1>

<div align="center">

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

</div>

---  

A new interactive way to create spotify playlists! Just put in a sentence that you want to represent and our application will map out each word to a song for you to listen to on a new playlist! Discover new songs by inputting creative outlandish sentences, or create a message to send out to your friends!

<div align="center">
    <img src="./public/Systrum_landing.png">
</div>

This was inspired by the twitter trend of indirect messages through your playlists! Our team decided to automate this process and allow for a new way to discover songs! Keep an eye on the repo for a link to our deployed site!

## Features

- Automation of sentences to playlists to spell out a message through your songs

- Spotify user authentication to send playlist to user's account

- Reactive frontend

## How to Use

#### Backend
Get a set of credentials from Spotify Developers API at https://developer.spotify.com/documentation/web-api?r_done=1

You can put the client_id and client_secret into a .env file and insert that into your backend folder.

You can now run the program using these commands

Windows:
```bash
    cd backend
    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    cd app 
    python init_db.py
    set FLASK_APP=main.py
    flask --app main.py --debug run
```

Mac:
```bash
    cd backend
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt 
    cd app 
    python3 init_db.py
    set FLASK_APP=main.py
    flask --app main.py --debug run
```

#### Frontend
In a second terminal run:

```bash
    cd frontend
    npm install
    npm run dev
```

## Future Plans

- Genre filtering  
- Deployment
 

## Contributors

[![Eduardo](https://img.shields.io/badge/Eduardo_Murillo-313030?style=for-the-badge&logo=github&logoColor=white)](https://github.com/edmuri)
[![Claudia](https://img.shields.io/badge/Claudia_Varnas-90407E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cl-py)
[![Julia](https://img.shields.io/badge/Julia_Bowman-B6D0E2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juliafbowman)
[![Basil](https://img.shields.io/badge/Basil_Tiongson-9A290F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/basiltiongson0)



