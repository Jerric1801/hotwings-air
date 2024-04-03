import os
import json
import datetime
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from .models import Room, Hotel
from mongoengine.connection import disconnect

def seed_accomodations():
    app = Flask(__name__)
    CORS(app)

    try: 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/admin')

        try:
            client.accom_inventory.command(
                'createUser', 'root', 
                pwd='example',
                roles=[{'role': 'readWrite', 'db': 'accom_inventory'}]
            )
        except Exception as e:
            print("User Already Exists") 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/accom_inventory')

        db = client['accom_inventory'] 

        engine = connect(db='accom_inventory', host='mongodb', port=27017, username='root', password='example', authentication_source='admin') 
        
    except Exception as e:
        print("Failed to connect to mongodb", e) 

    if db.hotel.count_documents({}) == 0:
        with open('app/data/accommodation.json') as f:
            accom_data = json.load(f)

        for data in accom_data:
            print(data)

            rooms = []
            for room_data in data.pop('rooms', []):  # Extract rooms, handle if they don't exist
                try:
                    room = Room(**room_data)
                    rooms.append(room)
                except Exception as e:
                    print("Error creating room:", e)

            hotel = Hotel(**data)
            hotel.rooms = rooms
                
            try:
                hotel.save()
                print("Hotel seeded successfully")
            except Exception as e:
                print("Error during seeding:", type(e), e)

        disconnect() 
    else: 
        disconnect()