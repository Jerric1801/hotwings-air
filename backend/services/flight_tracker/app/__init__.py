import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect

app = Flask(__name__)
CORS(app)
app.config.from_object('config')


from . import models 
from . import routes 