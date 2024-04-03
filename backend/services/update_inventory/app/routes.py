from flask import jsonify, request, render_template

from app import app
from .services import update_flight_inventory, send_message_to_rabbitmq, create_email_template
from .models import Inventory


import os, sys
  
@app.route('/update_inventory', methods = ["POST"]) #ASK JERRICCCCCCCCCCCCCCCCCCCCCCCCCCCC
def inventory_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
             #1. Request: Receiving Flight Details from UI- HTTP POST
            data = request.get_json()
            print("\nReceived a record of payment details in JSON:", data)
            new_flight_data = data.get('new_flight_data')
            old_flight_data = data.get('old_flight_data')
            user_id = data.get('user_id')
            user_email = data.get('user_email')
            accommodation = data.get('accommodation')

            InventoryDetails = Inventory(new_flight_data, old_flight_data, accommodation,user_id, user_email)


           
            #3. Update Accommodation Inventory to accommodation inventory - AMQP
            payload = {
               "room_id" : InventoryDetails.accommodation["room_id"],
               "hotel_id" : InventoryDetails.accommodation["hotel_id"]
            }

            print("\n ---- Updating Accommodation Inventory ----")

            accomodation_result = send_message_to_rabbitmq('hotwings', 'topic', accommodation_inventory, 'update.accommodation', payload)

            print('\n------------------------')
            print('accommodation_result:', accommodation_inventory)

        
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Update Inventory microservice has an internal error: " + ex_str}), 500


            #3. Send confirmation email to notificiation - AMQP

        try:
                flight_details = {
                                "origin" : InventoryDetails.new_flight_data['origin'],
                                "destination" : InventoryDetails.new_flight_data['destination'],
                                "seat_num" : InventoryDetails.new_flight_data['seat_num']
                            }
                confirmation_email = create_email_template("confirmation", flight_details)
                confirmation_data = {
                                "user_email": InventoryDetails.user_email,
                                "subject": confirmation_email["subject"],
                                "message_body": confirmation_email["message"]
                            }   
                print('\n-----Invoking Notifications -----')

                noti_payment_result = send_message_to_rabbitmq("hotwings", "topic", "notifications", "confirmation.noti", confirmation_data)

                print('\n------------------------')
                print('noti_payment_result:', noti_payment_result)
                            
        except Exception as e:
            # Unexpected error in code
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                print(ex_str)

                return jsonify({"error": "Update Inventory microservice has an internal error: " + ex_str}), 500
        


            #3. Request update to flight inventory - HTTP PUT 
        try:
                flight_data = {
                    "user_id": InventoryDetails.user_id,
                    "flight_id": InventoryDetails.new_flight_data['flight_id'],
                    "seat_number": InventoryDetails.new_flight_data['seat_num']
                    }   
                print('\n-----Invoking Flight Inventory -----')

                flight_result = update_flight_inventory(flight_data)

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
       

            #5. Send flight details to Pricing - AMQP

        try:

            flight_data_to_pricing = {
                "user_email": InventoryDetails.user_email,
                "new_flight":{
                    "flight_number": InventoryDetails.new_flight_data['flight_number'],
                    "flight_class": InventoryDetails.new_flight_data['flight_class']
            },

                "old_flight":{
                    "flight_number": InventoryDetails.old_flight_data['flight_number'],
                    "flight_class": InventoryDetails.old_flight_data['flight_class']
                }
            }


            print('\n-----Invoking Flight Inventory -----')

            flight_result = update_flight_inventory(flight_data_to_pricing)

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




      
    
