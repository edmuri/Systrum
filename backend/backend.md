copy and paste these commands into your terminal from the repo home

WINDOWS:

cd backend
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
cd app 
set FLASK_APP=backend.py
flask --app backend.py --debug run

MAC:

cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
cd app 
set FLASK_APP=backend.py
flask --app backend.py --debug run