import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

try: 
    client = MongoClient('mongodb://root:example@host.docker.internal:27017/accom_inventory')
    db = client['accom_inventory'] 
    print(db)
    # connect(db='accom_inventory', host='localhost', port=27017) 

except:
    print("Failed to connect to mongodb") 


from . import models 
from . import routes 
from . import schema