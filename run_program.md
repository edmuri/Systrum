backend: 

WINDOWS:

cd backend
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
cd app 
python init_db.py
set FLASK_APP=main.py
flask --app main.py --debug run

MAC:

cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
cd app 
python3 init_db.py
set FLASK_APP=main.py
flask --app main.py --debug run

in second terminal:
cd frontend
npm run dev