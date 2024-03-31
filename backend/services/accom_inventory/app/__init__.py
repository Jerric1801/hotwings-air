import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from .schema import Query
import graphene

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
schema = graphene.Schema(query=Query)


try: 
    client = MongoClient('localhost', port=27017)
    db = client['accom_inventory'] 
    connect(db='accom_inventory', host='localhost', port=27017) 

except:
    print("Failed to connect to mongodb") 


from . import models 
from . import routes 