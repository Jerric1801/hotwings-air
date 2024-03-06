import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

try: 
    client = MongoClient('mongodb', port=27017)
    db = client['flight_inventory'] 
    connect(db='flight_inventory', host='mongodb', port=27017) 

except:
    print("Failed to connect to mongodb") 

from . import models 
from . import routes 