from flask import jsonify, request
from app import app
from .services import call_flight_inventory
from .models import FlightSearch

@app.route('/flight_search/test', methods = ["GET"])
def test_flights():
     if request.method == "GET":
        return jsonify("success")

@app.route('/flight_search', methods = ["POST"])
def search_flights():
    try:
        if request.method == "POST":
            data = request.get_json() 
            searchInstance = FlightSearch(**data)
            
            if searchInstance.trip_type == "oneway":
                payload = searchInstance.get_search_params()
                depart_option = call_flight_inventory(payload)

                return jsonify(depart_option)
            else:
                payload_depart = searchInstance.get_search_params()
                payload_return = searchInstance.get_search_params(return_flight=True)
                depart_option = call_flight_inventory(payload_depart)
                return_option = call_flight_inventory(payload_return)

                return jsonify([depart_option, return_option])


    except KeyError as e:
            return jsonify({"error": f"Missing required parameter: {e}"}), 400
    except Exception as e:  # Catch potential errors from call_flight_inventory
        return jsonify({"error": "Flight inventory service error"}), 500 