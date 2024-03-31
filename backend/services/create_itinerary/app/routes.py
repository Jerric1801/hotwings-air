from flask import jsonify, request

from app import app
from .services import send_flight_details_to_search_flight, send_flight_details_to_search_accomodation, send_flight_details_to_custom_webpage, send_flight_details_to_rabbitmq
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
            old_flight_data = data.get('old_flight_data')
            user_email = data.get('user_email')

            itinerary = Itinerary(old_flight_data, user_email)

            # 5. Send flight data to Search Flight complex microservice
            search_flight_data = {
                old_flight_data : itinerary.old_flight_data,
                user_email : itinerary.user_email
            }
            print('\n-----Invoking Search Flight-----')

            # 8. Receive recommended flight from Search Flight complex microservice
            search_flight_result = send_flight_details_to_search_flight(search_flight_data)
        
            print('\n------------------------')
            print('search_flight_result:', search_flight_result)

            search_flight_code = search_flight_result["code"]

            # 9. Activate error handler if the search flight fails
            if search_flight_code not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Search Flight error message with routing_key=search_flight.error-----')
                send_flight_details_to_rabbitmq("payment_topic", "topic", "Error", "search_flight.error", search_flight_result)
                
                return jsonify(search_flight_result), search_flight_code
            
            else:

                try:
                    # 9. Send new flight details to Search Accommodation microservice
                    flight_data = search_flight_result["data"]
                    itinerary.update_new_flight_data(new_flight_data=flight_data)
                    print('\n-----Invoking Search Accommodation -----')

                    accommodation_result = send_flight_details_to_search_accomodation(flight_data)

                    # 12. Receive recommended accommodation from Search Accommodation
                    print('\n------------------------')
                    print('accommodation_result:', accommodation_result)

                    accommodation_code = accommodation_result["code"]

                    # 13.  Activate error handler if the search accommodation fails
                    if accommodation_code not in range(200, 300):
                        # Inform the error microservice
                        print('\n\n-----Publishing the Search Accommodation error message with routing_key=search_accommodation.error-----')
                        send_flight_details_to_rabbitmq("payment_topic", "topic", "Error", "search_accommodation.error", accommodation_result)
                
                        return jsonify(accommodation_result), accommodation_code
                    
                    else:

                        try:
                            # 13. Send new flight details and accommodation to Create Webpage microservice
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

                            custom_webpage_code = custom_webpage_result["code"]

                            # 14.  Activate error handler if the custom webpage fails
                            if custom_webpage_code not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the Custom Webpage error message with routing_key=webpage.error-----')
                                send_flight_details_to_rabbitmq("payment_topic", "topic", "Error", "webpage.error", custom_webpage_result)
                        
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

                    return jsonify({"error": "Search Accommodation microservice has an internal error: " + ex_str}), 500

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Search Flight has an internal error: " + ex_str}), 500
        
       
    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400




      
    