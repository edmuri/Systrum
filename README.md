# Systrum 🎼


---
### ℹ️ About


<img width="1840" height="899" alt="Screenshot 2025-08-22 111008" src="https://github.com/user-attachments/assets/dd67282d-208e-4a8d-b322-8e0cdd42feb4" />

A new interactive way to create spotify playlists! Just put in a sentence that you want to represent and our application will map out each word to a song for you to listen to on a new playlist! Discover new songs by inputting creative outlandish sentences, or create a message to send out to your friends!

This was inspired by the twitter trend of indirect messages through your playlists! Our team decided to automate this process and allow for a new way to discover songs! Keep an eye on the repo for a link to our deployed site!

---
### 🌟 Features

:atom: Automation of sentences to playlists to spell out a message through your songs

:atom: Spotify user authentication to send playlist to user's account

 :atom: Reactive frontend

---
### ⚡Tech Stack

  🎵 React [ HTML, CSS, Javascipt ]

  🎵 Flask [ Python ] 

  🎵 mySQL [ SQL ] 

  🎵 SpotifyAPI

---
### 👓 How to Use

#### Backend
Get a set of credentials from Spotify Developers API at https://developer.spotify.com/documentation/web-api?r_done=1

You can put the client_id and client_secret into a .env file and insert that into your backend folder.

You can now run the program using these commands

Windows:

    cd backend
    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    cd app 
    python init_db.py
    set FLASK_APP=main.py
    flask --app main.py --debug run

Mac:

    cd backend
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt 
    cd app 
    python3 init_db.py
    set FLASK_APP=main.py
    flask --app main.py --debug run

#### Frontend
In a second terminal run:

    cd frontend
    npm install

This will install the necessary node modules. 

Then, you can run the frontend with

    npm run dev
---
### 🕙 Future Plans

 💮 Genre filtering
 
 💻 Deployment
 
---
### 🎹 Contributors
🖤 Eduardo Murillo: Project Manager, Backend Developer

🩶 Basil Tiongson: Frontend Developer

💜 Claudia Varnas: Backend Developer

🩷 Julia Bowman: Frontend Developer

