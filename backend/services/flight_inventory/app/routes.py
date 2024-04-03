from flask import jsonify, request
from app import app, db
from .models import Flight, Seating_Plan, FlightTemplate, Disrupted
from .services import update_seats
from bson import json_util
import json
from datetime import datetime, timedelta
from bson.timestamp import Timestamp
from bson.objectid import ObjectId

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

            print(date)

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

            flight_results = db['flight'].find(query).limit(5)

            possible_flights = []

            for flight in flight_results:
                flight["pax"] = pax
                flight["seatClass"] = seatClass
                possible_flights.append(flight)

            if flight_results:
                return json.loads(json_util.dumps(possible_flights))
            else:
                return jsonify({"message": "Flight not found."}), 404 
        except ValueError:
            return jsonify({"message": "Invalid flight number."}), 400 
        

@app.route('/flight/seating', methods = ["POST"])
def search_seating():
    if request.method == "POST":
        try:
            seating_plans = {}
            data = request.get_json() 
            depart_id = data.get("depart_id")
            return_id = data.get("return_id")

            if depart_id:

                depart_query = {
                    "_id":ObjectId(depart_id),
                }

                depart_results = db['seating__plan'].find_one(depart_query)
                seating_plans["depart_plan"] = depart_results["seats"]

            if return_id:

                return_query = {
                    "_id":ObjectId(return_id),
                }

                return_results = db['seating__plan'].find_one(return_query)
                seating_plans["return_plan"] = return_results["seats"]

            if seating_plans:
                return json.loads(json_util.dumps(seating_plans))
            
            else:
                return jsonify({"message": "Flight not found."}), 404 
        except ValueError:
            return jsonify({"message": "Invalid flight number."}), 400 

@app.route('/flight/seating/update', methods = ["POST"])
def update_seating():
    if request.method == "POST":
        try:
            data = json.loads(request.get_json())
            #dictionary with [seat_id (string), seats(list)]
            departId= data.get("depart_id")
            returnId = data.get("return_id")
            departSeats = data.get("depart_seats")
            returnSeats = data.get("return_seats")
            depart_updated = update_seats(departId, departSeats)
            return_updated = True
            if returnId:
                return_updated = update_seats(returnId, returnSeats)

            if depart_updated and return_updated:  
                return jsonify({"Success": "Seats updated"}), 200
            else:
                return jsonify({"Failed": "Unable to update seats"}), 404 
            
        except Exception as e:
            return jsonify({"Failed": "Unable to update seats"}), 404 

@app.route('/flight/alternatives', methods = ["POST"])
def alternatives():
    if request.method == "POST":
        try:
            data = json.loads(request.get_json())
            data_departure = data.get('departure')
            old_flight_number = data.get('flight_number')
            print("***",type(data_departure))
            print("***",old_flight_number)
         
            #2024-04-03T00:35:29.626Z
            #2024-04-03T00:35:29.626561
            #2024-04-03T08:23:00.821Z

            old_departure = data_departure[:-3] + "Z"
            print(old_departure)
            old_departure = datetime.strptime(old_departure, "%Y-%m-%dT%H:%M:%S.%fZ")
            print(old_departure)

            alternative_query = {
                "flight_number": old_flight_number,
                "departure": {
                    "$gt": old_departure,
                    "$lt": old_departure + timedelta(days = 7)
                }
            }

            alternative_flights = db['flight'].find(alternative_query).limit(5)

            possible_flights = []

            for flight in alternative_flights:
                print(flight)
                flight_item = FlightTemplate(**flight)
                if flight_item.flight_id != old_flight_number:
           
                    seat_query = {
                        "_id":flight_item.seating_plan_id,
                    }

                    seating_plan = db['seating__plan'].find_one(seat_query)

                    if seating_plan:
                        available_seats_count = len([seat['available'] for seat in seating_plan['seats']])
                        print("Number of available seats:", available_seats_count)
                    else:
                        print("Seating plan not found.")

                    itinerary_details = {
                        "flight_number": flight_item.flight_number,
                        "avaliable_seats": available_seats_count,
                        "date": flight_item.departure,
                        "origin": flight_item.origin,
                        "destination": flight_item.destination
                    }

                    origin = flight_item.origin

                    possible_flights.append(itinerary_details)
                
            if alternative_flights:
                return jsonify({"flights": possible_flights, "origin": origin}), 200
            else:
                return jsonify({"message": "Flight not found."}), 404 

        except Exception as e:
            return jsonify({"Failed": "Unable to find alternative flights"}), 404 
        
@app.route('/flight/disrupted/update', methods = ["POST"])
def update_disrupted():
    if request.method == "POST":
        try:
            data = json.loads(request.get_json())

            
            details = Disrupted(**data)

            print(details)

            query = {
                "_id" : ObjectId(details.flight_id)
            }

        
            flight_results = db['flight'].find_one(query)

            print(flight_results)

            chosen_flight = FlightTemplate(**flight_results)
            print(chosen_flight)
            seat_query = {
                "_id": chosen_flight.seating_plan_id
            }

            seating_plan = db["seating__plan"].find_one(seat_query)
            print(seating_plan)
            seats = []
            for seat in seating_plan["seats"]:
                if seat['available']:
                    seats.append(seat['seat_number'])
                if len(seats) == details.pax:
                    break

            if update_seats(chosen_flight.seating_plan_id, seats):
                print("success")
                return jsonify({"origin": chosen_flight.origin,
                                "destination": chosen_flight.destination,
                                "departure": chosen_flight.departure,
                                "flight_number": chosen_flight.flight_number,
                                "seats": seats }), 200
            else:
                return jsonify({"Failed": "Unable to update seats"}), 404 
            
        except Exception as e:
            return jsonify({"Failed": "Unable to update seats"}), 404 
