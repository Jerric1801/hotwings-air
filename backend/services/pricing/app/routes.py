from flask import jsonify, request
from app import app
from .services import call_flight_inventory
from .models import FlightSearch

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