'''
Use this file to clear any tokens saved from testing.

I want to keep db mounted for deployment (and for storing words), but need to clear out tokens 
so we don't push our access tokens
'''
import os
from flask import Flask
from db import get_db


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
os.path.join(BASE_DIR, 'database.db')

db = get_db()

db.execute('DELETE * FROM token')
db.commit()