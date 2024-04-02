import os
import json
import datetime
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from .models import Booking, User
from mongoengine.connection import disconnect

def seed_user():
    app = Flask(__name__)
    CORS(app)

    try: 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/admin')

        # db = client['flight_inventory'] 
    
        try:
            client.user.command(
                'createUser', 'root', 
                pwd='example',
                roles=[{'role': 'readWrite', 'db': 'user'}]
            )
        except Exception as e:
            print("User Already Exists") 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/user')

        db = client['user'] 

        engine = connect(db='user', host='mongodb', port=27017, username='root', password='example', authentication_source='admin') 
        
    except Exception as e:
        print("Failed to connect to mongodb", e) 

    if db.flight.count_documents({}) == 0: 
        with open('app/users/user.json') as f:
            user_data = json.load(f)

        for data in user_data:
            print(data)
            try:
                userModel = User(**data)
                userModel.save()

            except Exception as e:
                print("error detected", e)

        engine.disconnect()
    else: 
        engine.disconnect()