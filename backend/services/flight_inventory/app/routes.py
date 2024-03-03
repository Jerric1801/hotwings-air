from flask import jsonify, request
from app import app, db
from .models import Flight, Seating_Plan
from bson import json_util
import json

@app.route('/flight', methods = ["GET"])
def get_all_flights():
    if request.method == "GET":
        flights = db.flight.find()  
        flights_list = [flight["_id"] for flight in flights]  
        return jsonify(flights_list) 
    
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