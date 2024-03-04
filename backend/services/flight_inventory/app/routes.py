from flask import jsonify, request
from app import app, db
from .models import Flight, Seating_Plan
from bson import json_util
import json
from datetime import datetime, timedelta

@app.route('/flight', methods = ["GET"])
def get_all_flights():
    if request.method == "GET":
        flights = db.flight.find()  
        flights_list = [flight["_id"] for flight in flights]  
        return jsonify(flights_list) 
    
@app.route('/flight/search', methods = ["POST"])
def search_flights():
    if request.method == "POST":
        try:
            data = request.get_json() 
            origin = data.get("origin")
            destination = data.get("destination")
            date = data.get("date")
            pax = data.get("pax")
            seatClass = data.get("class")

            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

            start_of_day = date_obj - timedelta(days = 7)
            end_of_day = date_obj + timedelta(days = 7)

            query = {
                "origin":origin,
                "destination": destination,
                "departure": {
                    "$gte": start_of_day,
                    "$lt": end_of_day
                }
            }

            flight_results = db.flight.find(query).limit(5)

            possible_flights = []

            for flight in flight_results:
                print(flight)
                possible_flights.append(flight)
            
            if flight_results:
                return json.loads(json_util.dumps(possible_flights))
            else:
                return jsonify({"message": "Flight not found."}), 404 
        except ValueError:
            return jsonify({"message": "Invalid flight number."}), 400 
    
@app.route('/flight/<flight_number>', methods = ["GET"])
def get_flight(flight_number):
    if request.method == "GET":
        try:
            flight = db.flight.find_one({"_id":flight_number})
            if flight:
                return json.loads(json_util.dumps(flight))
            else:
                return jsonify({"message": "Flight not found."}), 404 
        except ValueError:
            return jsonify({"message": "Invalid flight number."}), 400  
        
@app.route('/flight/<origin>/origin', methods = ["GET"])
def get_origin(origin):
    if request.method == "GET":
        try:
            flight = db.flight.find_one({"origin": origin})
            print(flight)
            if flight:
                return json.loads(json_util.dumps(flight))
            else:
                return jsonify({"message": "Flight not found."}), 404 
        except ValueError:
            return jsonify({"message": "Invalid flight number."}), 400  


@app.route('/flight/new', methods = ["POST"])
def create_flight():
    if request.method == "POST":
        data = request.get_json()
        try:
             # 1. Create and Save Seating Plan
            seating_plan_data = data['aircraft'].pop('seating_plan', None)  # Extract and remove 
            if seating_plan_data:
                seating_plan = Seating_Plan(**seating_plan_data)
                seating_plan.save()
                data['aircraft']['seating_plan_id'] = seating_plan.id

            # 2. Create and Save Flight
            new_flight = Flight(**data)
            new_flight.save()
            return jsonify(new_flight.to_json()), 201
        except Exception as e: 
            print(e)
            return jsonify({'error': str(e)}), 500