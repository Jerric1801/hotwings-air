from flask import jsonify, request
from app import app, db
# from .models import Flight

available_seats = {
    "flight_123": ["A1", "A2", "B3"],
    "flight_456": ["C4", "D5"]
}

# @app.route('/flights/<flight_id>/seats', methods=['GET'])
# def get_available_seats(flight_id):
#     seats = available_seats.get(flight_id)
#     if seats:
#         return jsonify(seats)
#     else:
#         return jsonify({"message": "Flight not found"}), 404

@app.route('/flights')
def get_all_flights():
    flight = db.flights.find()
    for document in flight:  # Each 'document' is a flight 
        return document['flight_no']