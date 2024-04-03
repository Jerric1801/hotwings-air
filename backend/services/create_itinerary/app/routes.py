from flask import jsonify, request

from app import app
from .services import send_flight_details_to_flight_inventory, send_flight_details_to_accomodation, send_flight_details_to_custom_webpage, send_error_to_rabbitmq
from .models import Itinerary

import os, sys


@app.route('/create_itinerary', methods = ["POST"])
def send_itinerary_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            # 4. Receive delayed flight details from Update Delay complex microservice
            data = request.get_json()

            itinerary = Itinerary(**data)

            # 6. Send flight data to Flight Inventory microservice
            flight_inventory_data = {
               "flight_number" : itinerary.flight_number,
               "departure": itinerary.departure
            }

            # 7. Receive recommended flight from Flight Inventory microservice
            flight_inventory_result = send_flight_details_to_flight_inventory(flight_inventory_data)    
            print(flight_inventory_result)
            
            # 7. Activate error handler if the search flight fails
            if not flight_inventory_result:
                # Inform the error microservice
                send_error_to_rabbitmq("hotwings", "topic", "Error", "flight_inventory.error", flight_inventory_result)
                
                return jsonify({"error": "no flights received"}), 404
                
        
            
            else:

                try:
                    #update itinerary obj for flight
                    flight_data = flight_inventory_result["flights"] #list of possible flights
                    itinerary.update_new_flight_data(flight_data)

                    accomodation_payload = {
                        "origin": flight_inventory_result["origin"]
                    }
                    accommodation_result = send_flight_details_to_accomodation(accomodation_payload)

                    if not accommodation_result:
                        # Inform the error microservice
                        send_error_to_rabbitmq("hotwings", "topic", "error", "accommodation.error", accommodation_result)
                        return jsonify({"error": "no accoms received"}), 404
                

                    else:

                        try:
                            print(accommodation_result)
                            #update itinerary obj for accommodation
                            accommodation_data = accommodation_result["data"]["availableRooms"][0]
                            itinerary.update_accommodation(accommodation_data)

                            custom_webpage_data = {
                                "departure": itinerary.departure,
                                "flight_number": itinerary.flight_number,
                                "recommended_flights" : itinerary.potential_flights,
                                "recommended_accommodation": itinerary.potential_accommodation,
                                "user_emails" : itinerary.email_list
                            }

                            print(custom_webpage_data)

                            custom_webpage_result = send_flight_details_to_custom_webpage(custom_webpage_data)

                            print('\n------------------------')
                            print('custom_webpage_result:', custom_webpage_result)

                            # 11. Receive reply status

                            # 11.  Activate error handler if the custom webpage fails
                            if custom_webpage_result not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the Custom Webpage error message with routing_key=webpage.error-----')
                                send_error_to_rabbitmq("payment_topic", "topic", "Error", "webpage.error", custom_webpage_result)
                        
                                return jsonify(custom_webpage_result)
                            
                        except Exception as e:
                            # Unexpected error in code
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                            print(ex_str)

                            return jsonify({"error": "Create webpage microservice has an internal error: " + ex_str}), 500
                            
                except Exception as e:
                    # Unexpected error in code
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                    print(ex_str)

                    return jsonify({"error": "Accommodation inventory microservice has an internal error: " + ex_str}), 500

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Flight Inventory has an internal error: " + ex_str}), 500
        
       
    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400




      
    