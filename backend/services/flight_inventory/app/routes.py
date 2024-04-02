from flask import jsonify, request
from app import app, db
from .models import Flight, Seating_Plan, FlightTemplate
from .services import update_seats
from bson import json_util
import json
from datetime import datetime, timedelta
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

            flight_id = data.get("flight_id")
            flight_query = {
                "_id":ObjectId(flight_id),
            }

            old_flight_query = db['flight'].find_one(flight_query)

            old_flight = FlightTemplate(**old_flight_query)

            alternative_query = {
                "flight_number": old_flight.flight_number,
                "departure": {
                    "$gt": old_flight.departure,
                    "$lt": old_flight.departure + timedelta(days=10)
                }
            }


            alternative_flights = db['flight'].find(alternative_query).limit(5)

            possible_flights = []

            for flight in alternative_flights:
                flight_item = FlightTemplate(**flight)
                if flight_item.flight_id != old_flight.flight_id:
           
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
                        "date": flight_item.departure
                    }

                    possible_flights.append(itinerary_details)
                
            if alternative_flights:
                return json.loads(json_util.dumps(possible_flights))
            else:
                return jsonify({"message": "Flight not found."}), 404 

        except Exception as e:
            return jsonify({"Failed": "Unable to find alternative flights"}), 404 
        

# @app.route('/flight', methods = ["GET"])
# def get_all_flights():
#     if request.method == "GET":
#         flights = db.test.find_one({"field1":"value1"})
#         return json.loads(json_util.dumps(flights))
     
# @app.route('/flight/<flight_number>', methods = ["GET"])
# def get_flight(flight_number):
#     if request.method == "GET":
#         print("called")
#         try:
#             flight = db.flight.find_one({"_id":flight_number})
#             if flight:
#                 return json.loads(json_util.dumps(flight))
#             else:
#                 return jsonify({"message": "Flight not found."}), 404 
#         except ValueError:
#             return jsonify({"message": "Invalid flight number."}), 400  
        
# @app.route('/flight/<origin>/origin', methods = ["GET"])
# def get_origin(origin):
#     if request.method == "GET":
#         try:
#             flight = db.flight.find_one({"origin": origin})
#             print(flight)
#             if flight:
#                 return json.loads(json_util.dumps(flight))
#             else:
#                 return jsonify({"message": "Origin not found."}), 404 
#         except ValueError:
#             return jsonify({"message": "Invalid flight number."}), 400  


# @app.route('/flight/new', methods = ["POST"])
# def create_flight():
#     if request.method == "POST":
#         data = request.get_json()
#         try:
#              # 1. Create and Save Seating Plan
#             seating_plan_data = data['aircraft'].pop('seating_plan', None)  # Extract and remove 
#             if seating_plan_data:
#                 seating_plan = Seating_Plan(**seating_plan_data)
#                 seating_plan.save()
#                 data['aircraft']['seating_plan_id'] = seating_plan.id

#             # 2. Create and Save Flight
#             new_flight = Flight(**data)
#             new_flight.save()
#             return jsonify(new_flight.to_json()), 201
#         except Exception as e: 
#             print(e)
#             return jsonify({'error': str(e)}), 500