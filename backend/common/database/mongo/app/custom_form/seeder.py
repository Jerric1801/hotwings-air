import os
import json
import datetime
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

def seed_form():
    app = Flask(__name__)
    CORS(app)

    try: 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/admin')

        try:
            client.customform.command(
                'createUser', 'root', 
                pwd='example',
                roles=[{'role': 'readWrite', 'db': 'customform'}]
            )
        except Exception as e:
            print("User Already Exists") 


        # client = MongoClient('mongodb://root:example@host.docker.internal:27017/customform')

        # db = client['customform'] 

        # engine = connect(db='customform', host='mongodb', port=27017, username='root', password='example', authentication_source='admin') 
        
    except Exception as e:
        print("Failed to connect to mongodb", e) 

