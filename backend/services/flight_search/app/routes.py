from flask import jsonify, request
from app import app
from .services import call_flight_inventory, add_pricing
from .models import FlightSearch

@app.route('/flight_search/test', methods = ["GET"])
def test_flights():
     if request.method == "GET":
        return jsonify("success")

@app.route('/flight_search', methods = ["POST"])
def search_flights():
    """
    Receives flight details from ui 
        1. calls flight_inventory based on trip type
        2. if flight found, calls pricing to get price

    Arguments:
    
    
    """
    try:
        if request.method == "POST":
            data = request.get_json() 
            searchInstance = FlightSearch(**data)

            #assume that plane has vast amount of particular seat class
            seat_class = searchInstance.flight_class

            if searchInstance.trip_type == "oneway":
                payload = searchInstance.get_search_params()
                try:
                    depart_option = call_flight_inventory(payload)
                except: 
                    print("Error with flight_inventory api")
                return_option = None
            else:
                payload_depart = searchInstance.get_search_params()
                payload_return = searchInstance.get_search_params(return_flight=True)
                #write asynchronous calls for this
                try:
                    depart_option = call_flight_inventory(payload_depart)
                    return_option = call_flight_inventory(payload_return)
                except:
                    print("Error with flight_inventory api")

            depart_option = add_pricing(depart_option, seat_class)
            return_option = add_pricing(return_option, seat_class)

            return jsonify([depart_option, return_option])


    except KeyError as e:
            return jsonify({"error": f"Missing required parameter: {e}"}), 400
    except Exception as e:  # Catch potential errors from call_flight_inventory
        return jsonify({"error": "Flight Search experienced an error"}), 500 