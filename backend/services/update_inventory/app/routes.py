from flask import jsonify, request, render_template

from app import app
from .services import update_flight_inventory, send_message_to_rabbitmq, create_email_template
from .models import Inventory, NewFlight


import os, sys
  
@app.route('/update_inventory', methods = ["POST"]) 
def inventory_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
             #1. Request: Receiving Flight Details from UI- HTTP POST
            data = request.get_json()
            InventoryDetails = Inventory(**data)

             #2. Request update to flight inventory - HTTP PUT 
            flight_data = {
                "pax": InventoryDetails.pax,
                "flight_id": InventoryDetails.new_flight_data,
                }   
            
            print('\n-----Invoking Flight Inventory -----')

            flight_result = update_flight_inventory(flight_data)
            print(flight_result)
            new_flight = NewFlight(**flight_result)
            print('\n------------------------')
            print('flight_result:', flight_result)


            if not flight_result:
                # Inform the error microservice
                print('\n\n-----Publishing the Flight Inventory error message with routing_key=flight.error-----')
                send_message_to_rabbitmq("hotwings", "topic", "error", "flight.error", flight_result)
            
                return jsonify(flight_result)
        


            #3. Update Accommodation Inventory to accommodation inventory - AMQP
            payload = {
               "room_id" : InventoryDetails.accommodation,
            }

            print(payload)

            print("\n ---- Updating Accommodation Inventory ----")

            send_message_to_rabbitmq('hotwings','topic',"accommodation", "up.accommodation" ,payload)

            print('\n------------------------')
            # print('accommodation_result:', accomodation_result)

            
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Update Inventory microservice has an internal error: " + ex_str}), 500
        
            #3. Send confirmation email to notificiation - AMQP

        try:
            print(new_flight.seats)
            flight_details = {
                            "origin" : new_flight.origin,
                            "destination" : new_flight.destination,
                            "seat_num": new_flight.seats
                        }
            confirmation_email = create_email_template("confirmation", flight_details)
            confirmation_data = {
                            "email": InventoryDetails.user_email,
                            "notification_type": confirmation_email["subject"],
                            "notification_message": confirmation_email["message"]
                        }   
            print('\n-----Invoking Notifications -----')

            noti_payment_result = send_message_to_rabbitmq("hotwings", "topic", "notifications", "confirmation.notifications", confirmation_data)

            print('\n------------------------')
            print('noti_payment_result:', noti_payment_result)
                        
        except Exception as e:
            # Unexpected error in code
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                print(ex_str)

                return jsonify({"error": "Update Inventory microservice has an internal error: " + ex_str}), 500
        




            #5. Send flight details to Pricing - AMQP

        try:

            flight_data_to_pricing = {
                "user_email": InventoryDetails.user_email,
                "new_flight":{
                    "flight_number": new_flight.flight_number,
                    "flight_class": "Economy"
            },

                "old_flight":{
                    "flight_number": InventoryDetails.old_flight_data,
                    "flight_class": "Economy"
                }
            }


            print('\n-----Invoking Flight Inventory -----')

            flight_result = send_message_to_rabbitmq("hotwings", "topic", "pricing", "flight_details.pricing", flight_data_to_pricing)

            print('\n------------------------')
            print('flight_result:', flight_result)

            flight_code = flight_result["code"]

            if flight_code not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Flight Inventory error message with routing_key=flight.error-----')
                send_message_to_rabbitmq("hotwings", "topic", "error", "flight.error", flight_result)
                
                return jsonify(flight_result), flight_code


        except Exception as e:
            # Unexpected error in code
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                print(ex_str)

                return jsonify({"error": "Update Inventory mciroservice has an internal error: " + ex_str}), 500

            
    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400




      
    