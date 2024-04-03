from flask import jsonify, request
from app import app, db
from .models import Pricing
import json

@app.route('/pricing/<flight_str>', methods = ["GET"])
def get_flight(flight_str):
    if request.method == "GET":
        try:
            all_flights = Pricing.query.filter_by(flight_id=flight_str).all()
            flight_data = []
            for flight in all_flights:
                flight_data.append({
                    "flight_id": flight.flight_id,
                    "seat_class": flight.seat_class,
                })

            if flight:
                return json.dumps(flight_data), 200
            else:
                return jsonify(error="invalid flight id"), 400
        except:
            return jsonify(error="Internal server error"), 500 

@app.route('/pricing/<route_str>/<class_str>', methods=["GET"])
def get_price(route_str, class_str):
    try:
        price = 10
        return jsonify(price), 200  # Success

    except ValueError as e:
        return jsonify(error="Invalid input parameters"), 400  # Bad request
    except Exception as e:  # Catch-all for unexpected errors
        # Log the error 
        return jsonify(error="Internal server error"), 500 

@app.route('/flights/new', methods=['POST'])
def add_flight_price():
    try:
        data = request.get_json()

        flight_price = Pricing(
            flight_id=data['flight_id'],
            seat_class=data['seat_class'],
            customer_id=data['customer_id'],
        )
        db.session.add(flight_price)
        db.session.commit()

        return jsonify({'message': 'Flight price added successfully'}), 201
    except Exception as e:  
        return jsonify({'error': str(e)}), 400


@app.route('/pricing/all', methods=["GET"])  # Create a route for this
def print_all_pricing():
    if request.method =="GET":
        all_flights = db.session.scalars(db.select(Pricing)).all()
        flight_data = []
        for flight in all_flights:
            flight_data.append({
                "flight_id": flight.flight_id,
                "seat_class": flight.seat_class,
                "customer_id": flight.customer_id
            })

        return json.dumps(flight_data), 200
    