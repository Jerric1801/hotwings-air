import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

client = MongoClient('localhost', 27017)
db = client['flight_inventory'] 
connect(db='flight_inventory', host='localhost', port=27017)  

from . import models 
from . import routes 