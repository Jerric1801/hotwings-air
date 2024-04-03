import os
import json
import datetime
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from .models import Flight, Seating_Plan
from mongoengine.connection import disconnect

def seed_flight_inventory():
    app = Flask(__name__)
    CORS(app)

    try: 

        client = MongoClient('mongodb://root:example@host.docker.internal:27017/admin')

        # db = client['flight_inventory'] 
    
        try:
            client.flight_inventory.command(
                'createUser', 'root', 
                pwd='example',
                roles=[{'role': 'readWrite', 'db': 'flight_inventory'}]
            )
        except Exception as e:
            print("User Already Exists") 


        client = MongoClient('mongodb://root:example@host.docker.internal:27017/flight_inventory')

        db = client['flight_inventory'] 

        engine = connect(db='flight_inventory', host='mongodb', port=27017, username='root', password='example', authentication_source='admin') 
        
    except Exception as e:
        print("Failed to connect to mongodb", e) 

    if db.flight.count_documents({}) == 0: 
        with open('app/data/flight_inventory.json') as f:
            flights_data = json.load(f)

        for data in flights_data:
            data['departure'] = datetime.datetime.strptime(data['departure'],  '%Y-%m-%dT%H:%M:%S.%f')
            data['arrival'] = datetime.datetime.strptime(data['arrival'], '%Y-%m-%dT%H:%M:%S.%f')
            # 1. Create and Save Seating Plan
            seating_plan_data = data['aircraft'].pop('seating_plan', None)  # Extract and remove 
            try:
                seating_plan = Seating_Plan(**seating_plan_data)
                seating_plan.save()

                data['aircraft']['seating_plan_id'] = seating_plan.id

                # 2. Create and Save Flight
                new_flight = Flight(**data)
                new_flight.save()
            except:
                print("error detected")

        disconnect()
    else:
        disconnect()