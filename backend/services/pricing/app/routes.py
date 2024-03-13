from flask import jsonify, request
from app import app, db
from flask_sqlalchemy import SQLAlchemy
# from .services import call_flight_inventory
from .models import Pricing

@app.route('/pricing/<string:flight_id>', methods = ["GET"])
def get_flight(flight_id):
    if request.method =="GET":
        print(flight_id)
        flight = db.session.query(Pricing).filter_by(flight_id=flight_id).first()
        try:
            flight = db.session.query(Pricing).filter_by(flight_id=flight_id).first()
            # print(flight_id)
            # flight = db.session.scalars(db.select(Pricing).filter_by(flight_id=flight_id).limit(1)).first()
            print(flight)
            if flight:
                return jsonify(flight), 200
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

@app.route('/pricing/new', methods = ["POST"])
def add_route_pricing():
    try:
        pass
    except:
        pass


@app.route('/pricing/all', methods=["GET"])  # Create a route for this
def print_all_pricing():
    if request.method =="GET":
        all_flights = db.session.scalars(db.select(Pricing)).all()

        for flight in all_flights:
            print(f"Flight ID: {flight.flight_id}")
            print(f"Seat Class: {flight.seat_class}")
            print(f"Customer ID: {flight.customer_id}")
            print("----------------")  # Separator between records

        return "All pricing records printed to console", 200