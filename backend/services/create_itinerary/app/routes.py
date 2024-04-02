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
            print("\nReceived a record of flight delay:", data)

            itinerary = Itinerary(**data)

            # 6. Send flight data to Flight Inventory microservice
            flight_inventory_data = {
               "flight_id" : itinerary.flight_id,
            }
            print('\n-----Invoking Flight Inventory-----')

            # 7. Receive recommended flight from Flight Inventory microservice
            flight_inventory_result = send_flight_details_to_flight_inventory(flight_inventory_data)

            return jsonify({"success": "m"}), 200
            print('\n------------------------')
            print('flight_inventory_result:', flight_inventory_result)

            flight_inventory_code = flight_inventory_result["code"]

            # 7. Activate error handler if the search flight fails
            if flight_inventory_code not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Flight_inventory error message with routing_key=search_flight.error-----')
                send_error_to_rabbitmq("hotwings", "topic", "Error", "flight_inventory.error", flight_inventory_result)
                
                return jsonify(flight_inventory_result), flight_inventory_code
            
            else:

                try:
                    # 8. Send new flight details to Accommodation Inventory microservice
                    flight_data = flight_inventory_result["data"]
                    itinerary.update_new_flight_data(new_flight_data=flight_data)
                    print('\n-----Invoking Accommodation Inventory -----')

                    accommodation_result = send_flight_details_to_accomodation(flight_data)

                    # 9. Receive recommended accommodation from Accommodation Inventory
                    print('\n------------------------')
                    print('accommodation_result:', accommodation_result)

                    accommodation_code = accommodation_result["code"]

                    # 9.  Activate error handler if the search accommodation fails
                    if accommodation_code not in range(200, 300):
                        # Inform the error microservice
                        print('\n\n-----Publishing the Accommodation Inventory error message with routing_key=accommodation.error-----')
                        send_error_to_rabbitmq("hotwings", "topic", "Error", "accommodation.error", accommodation_result)
                
                        return jsonify(accommodation_result), accommodation_code
                    
                    else:

                        try:
                            # 10. Send new flight details and accommodation to Create Webpage microservice
                            accommodation = accommodation_result["data"]
                            itinerary.update_accommodation(accommodation=accommodation)
                            custom_webpage_data = {
                                "new_flight_data" : itinerary.new_flight_data,
                                "accommodation": itinerary.accommodation,
                                "user_email" : itinerary.user_email
                            }
                            print('\n-----Invoking Custom Webpage -----')

                            custom_webpage_result = send_flight_details_to_custom_webpage(custom_webpage_data)

                            print('\n------------------------')
                            print('custom_webpage_result:', custom_webpage_result)

                            # 11. Receive reply status
                            custom_webpage_code = custom_webpage_result["code"]

                            # 11.  Activate error handler if the custom webpage fails
                            if custom_webpage_code not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the Custom Webpage error message with routing_key=webpage.error-----')
                                send_error_to_rabbitmq("payment_topic", "topic", "Error", "webpage.error", custom_webpage_result)
                        
                                return jsonify(custom_webpage_result), custom_webpage_code
                            
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




      
    