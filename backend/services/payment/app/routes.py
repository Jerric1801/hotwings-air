from flask import jsonify, request, render_template

from app import app
from .services import create_stripe_checkout_session, send_payment_details_to_flight_inventory,send_payment_details_to_rabbitmq,send_payment_details_to_users, create_email_template
from .models import Payment
from .utils import stripe_keys

import os, sys
import json
import stripe 

@app.route("/config", methods = ["GET"])
def get_publishable_key():
    if request.method == "GET":
        stripe_config = {"publicKey": stripe_keys["publishable_key"]}
        return jsonify(stripe_config)
    
@app.route("/payment/cancelled")
def cancelled():
    return render_template("cancelled.html")

@app.route('/payment/success')
def payment_success():
    # Retrieve the session ID from the query string
    session_id = request.args.get('session_id')

    if not session_id:
        return "Session ID is missing", 400

    try:
        stripe.api_key = stripe_keys["secret_key"]

        # Retrieve the checkout session to get the payment_intent
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        payment_intent_id = checkout_session.payment_intent

        # Retrieve the payment intent to get details like amount and currency
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        amount_paid = payment_intent.amount_received
        points = round(amount_paid)

        # Convert amount to a more readable format (e.g., from cents to dollars)
        amount_paid = amount_paid/100  # Adjust based on the smallest currency unit
        currency = payment_intent.currency
        points_used = checkout_session.metadata.get('points_used', '0')

        # Render success.html with dynamic payment details
        return render_template("success.html", payment_intent_id=payment_intent_id, amount_paid=amount_paid, currency=currency.upper(), deets=payment_intent, points=points, points_used=points_used)
    except stripe.error.StripeError as e:
        # Handle Stripe errors (e.g., session not found)
        return jsonify(error=str(e)), 403
    except Exception as e:
        # Handle other exceptions
        return jsonify(error=str(e)), 500
    
@app.route('/payment', methods = ["POST"])
def send_payment_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            # 1. Receive payment info from UI 
            data = request.get_json()
            print("\nReceived a record of payment details in JSON:", data)
            orig_price = data.get('orig_price')
            final_price = data.get('final_price')
            seat_number = data.get('seat_number')
            flight_id = data.get('flight_id')
            origin = data.get('origin')
            destination = data.get('destination')
            redemption_loyalty_points = data.get('loyalty_points')
            user_id = data.get('user_id')
            user_email = data.get('user_email')

            paymentDetails = Payment(orig_price, final_price, seat_number, flight_id, origin, destination, redemption_loyalty_points, user_id, user_email)

            # 2. Send payment info to Stripe
            product_description = paymentDetails.flight_id
            unit_amount = paymentDetails.final_price
            points_used = paymentDetails.redemption_loyalty_points
            print('\n-----Invoking Stripe API-----')

            # 3. Returns success or failure for payment via Stripe API
            stripe_result = create_stripe_checkout_session(product_description, unit_amount, points_used, currency='sgd')
        
            print('\n------------------------')
            print('stripe_result:', stripe_result)

            stripe_code = stripe_result["code"]

            # 4. Activate error handler if there payment fails
            if stripe_code not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Stripe error message with routing_key=stripe.error-----')
                send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "stripe.error", stripe_result)
                
                return jsonify(stripe_result), stripe_code
            
            else:

                try:
                    # 4. Update flight inventory
                    flight_data = {
                        "user_id": paymentDetails.user_id,
                        "flight_id": paymentDetails.flight_id,
                        "seat_number": paymentDetails.seat_number
                    }   
                    print('\n-----Invoking Flight Inventory -----')

                    flight_result = send_payment_details_to_flight_inventory(flight_data)

                    print('\n------------------------')
                    print('flight_result:', flight_result)

                    flight_code = flight_result["code"]

                    if flight_code not in range(200, 300):
                        # Inform the error microservice
                        print('\n\n-----Publishing the Flight Inventory error message with routing_key=flight.error-----')
                        send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "flight.error", flight_result)
                
                        return jsonify(flight_result), flight_code
                    
                    else:

                        try:
                            # 5. Record payment details in transaction
                            transaction_data = {
                                "user_id": paymentDetails.user_id,
                                "type": "P",
                                "payment_amt": stripe_result["price"]
                            }   
                            print('\n-----Invoking Transactions -----')

                            transaction_result = send_payment_details_to_rabbitmq("payment_topic", "topic", "Transactions", "payment.trans", transaction_data)

                            print('\n------------------------')
                            print('transaction_result:', transaction_result)

                            transaction_code = transaction_result["code"]

                            if transaction_code not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the Transaction error message with routing_key=trans.error-----')
                                send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "trans.error", transaction_result)
                        
                                return jsonify(transaction_result), transaction_code
                            
                        except Exception as e:
                            # Unexpected error in code
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                            print(ex_str)

                            return jsonify({"error": "Transaction microservice has an internal error: " + ex_str}), 500

                        try:
                            # 5. Sends confirmation email to user 
                            flight_details = {
                                "origin" : paymentDetails.origin,
                                "destination" : paymentDetails.destination,
                                "seat_num" : paymentDetails.seat_number
                            }
                            confirmation_email = create_email_template("confirmation", flight_details)
                            confirmation_data = {
                                "user_email": paymentDetails.user_email,
                                "subject": confirmation_email["subject"],
                                "message_body": confirmation_email["message"]
                            }   
                            print('\n-----Invoking Notifications -----')

                            noti_payment_result = send_payment_details_to_rabbitmq("payment_topic", "topic", "Notifications", "confirmation.noti", confirmation_data)

                            print('\n------------------------')
                            print('noti_payment_result:', noti_payment_result)

                            noti_payment_code = noti_payment_result["code"]

                            if noti_payment_code not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the Notification error message with routing_key=noti.error-----')
                                send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "noti.error", noti_payment_result)
                        
                                return jsonify(noti_payment_result), noti_payment_code
                            
                        except Exception as e:
                            # Unexpected error in code
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                            print(ex_str)

                            return jsonify({"error": "Notifications mciroservice has an internal error: " + ex_str}), 500
                        
                        try:
                            # 5. Calculate loyalty points and send to Users
                            loyalty_points_data = {
                                "user_id": paymentDetails.user_id,
                                "flight_id": paymentDetails.flight_id,
                                "loyalty_points": paymentDetails.orig_price
                            }   
                            print('\n-----Invoking User -----')

                            user_result = send_payment_details_to_users(loyalty_points_data)

                            print('\n------------------------')
                            print('user_result:', user_result)

                            user_code = user_result["code"]
                            accumulated_loyalty_points = user_result["accumulated_loyalty_points"]

                            if user_code not in range(200, 300):
                                # Inform the error microservice
                                print('\n\n-----Publishing the User error message with routing_key=user.error-----')
                                send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "user.error", user_result)
                        
                                return jsonify(user_result), user_code
                            
                            else:

                                # 6. Sends accumulated loyalty points email to user
                                points_email = create_email_template("points", accumulated_loyalty_points)
                                noti_points_data = {
                                    "user_email": paymentDetails.user_email,
                                    "subject": points_email["subject"],
                                    "message_body": points_email["message"]
                                }  
                                print('\n-----Invoking Notifications -----')

                                noti_points_result = send_payment_details_to_rabbitmq("payment_topic", "topic", "Notifications", "points.noti", noti_points_data)

                                print('\n------------------------')
                                print('noti_points_result:', noti_points_result)

                                noti_points_code = noti_points_result["code"]

                                if noti_points_code not in range(200, 300):
                                    # Inform the error microservice
                                    print('\n\n-----Publishing the Notifications error message with routing_key=noti.error-----')
                                    send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "noti.error", noti_points_result)
                            
                                    return jsonify(noti_points_result), user_code
                            
                        except Exception as e:
                            # Unexpected error in code
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                            print(ex_str)

                            return jsonify({"error": "User microservice has an internal error: " + ex_str}), 500
                except Exception as e:
                    # Unexpected error in code
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                    print(ex_str)

                    return jsonify({"error": "Flight Inventory microservice has an internal error: " + ex_str}), 500

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Stripe Payment has an internal error: " + ex_str}), 500
        
       
    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


