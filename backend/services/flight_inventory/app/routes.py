from flask import jsonify, request
from app import app, db
from .models import Flight
import json

@app.route('/flights', methods = ["GET"])
def get_all_flights():
    if request.method == "GET":
        flights = db.flight.find()  
        flights_list = [flight["_id"] for flight in flights]  
        return jsonify(flights_list) 

    
@app.route('/flights/new', methods = ["POST"])
def create_flight():
    if request.method == "POST":
        data = request.get_json()
        try:
            new_flight = Flight(**data)
            new_flight.save()
            return jsonify(new_flight.to_json()), 201
        except Exception as e: 
            return jsonify({'error': str(e)}), 500