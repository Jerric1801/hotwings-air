from flask import jsonify, request
from app import app, db
from flask_sqlalchemy import SQLAlchemy
# from .services import call_flight_inventory
from .models import Pricing
import json

@app.route('/pricing/<flight_number>/<seat_class>', methods = ["GET"])
def get_price(flight_number, seat_class):
    if request.method == "GET":
        try:
            flight = Pricing.query.filter_by(flight_number=flight_number, seat_class=seat_class).first()
            if flight:
                price = flight.price
                print(price)
            if price:
                return json.dumps(price), 200
            else:
                return jsonify(error="invalid flight id"), 400
        except:
            return jsonify(error="Internal server error"), 500 
