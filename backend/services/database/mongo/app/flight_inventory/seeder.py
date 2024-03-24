import os
import json
import datetime
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from mongoengine import connect
from .models import Flight, Seating_Plan

def seed_flight_inventory():
    app = Flask(__name__)
    CORS(app)

    try: 
        client = MongoClient('mongodb', port=27017)
        db = client['flight_inventory'] 
        connect(db='flight_inventory', host='mongodb', port=27017, username='root', password='example', authentication_source='admin') 

    except:
        print("Failed to connect to mongodb") 


    with open('app/data/flight_inventory.json') as f:
        flights_data = json.load(f)

    for data in flights_data:
        data['departure'] = datetime.datetime.strptime(data['departure'],  '%Y-%m-%dT%H:%M:%S.%f')
        data['arrival'] = datetime.datetime.strptime(data['arrival'], '%Y-%m-%dT%H:%M:%S.%f')
        # 1. Create and Save Seating Plan
        seating_plan_data = data['aircraft'].pop('seating_plan', None)  # Extract and remove 
        if seating_plan_data:
            seating_plan = Seating_Plan(**seating_plan_data)
            seating_plan.save()
            data['aircraft']['seating_plan_id'] = seating_plan.id

        # 2. Create and Save Flight
        new_flight = Flight(**data)
        new_flight.save()
