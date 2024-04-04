from flask import jsonify, request, render_template
from flask_cors import cross_origin
from app import app
from .services import create_stripe_checkout_session, send_payment_details_to_flight_inventory,send_payment_details_to_rabbitmq,send_payment_details_to_users, create_email_template
from .models import Payment
from .utils import stripe_keys

import os, sys
import stripe 

EXCHANGE = "hotwings"

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
    
@app.route('/payment/stripe', methods = ["POST"])
@cross_origin() 
def generate_stripe():
    if request.is_json:
        data = request.get_json()
        product_description = data.get('flight_number')
        unit_amount = int(data.get('total_price') * 100)
        points_used = data.get('loyalty_points')
        print('\n-----Invoking Stripe API-----')

        # 3. Returns success or failure for payment via Stripe API
        checkout_link = create_stripe_checkout_session(product_description, unit_amount, points_used, currency='sgd')
        
        return jsonify(checkout_link), 200


    
@app.route('/payment', methods = ["POST"])
def send_payment_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            data = request.get_json()
            paymentDetails = Payment(**data)

            # 4. Update flight inventory
            flight_data = paymentDetails.get_flight_inventory()
            print('\n-----Invoking Flight Inventory -----')

            # flight_result = send_payment_details_to_flight_inventory(flight_data)
            flight_result = 200

            print('\n------------------------')
            print('flight_result:', flight_result)

            if flight_result not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Flight Inventory error message with routing_key=flight.error-----')
                send_payment_details_to_rabbitmq(EXCHANGE, "topic", "error", "flight.error", flight_result)
        
                return jsonify(flight_result)
            
            else:

                try:
                    # 5. Record payment details in transaction
                    transaction_data = {
                        "user_id": paymentDetails.user_email,
                        "type": "P",
                        "payment_amt": paymentDetails.total_price,
                        "loyalty_points": paymentDetails.loyalty_points,
                        "price_difference": 0
                    }   
                    print('\n-----Invoking Transactions -----')

                    transaction_result = send_payment_details_to_rabbitmq(EXCHANGE, "topic", "transactions", "payment.transactions", transaction_data)

                    print('\n------------------------')
                    print('transaction_result:', transaction_result)

                    transaction_code = transaction_result["code"]
                    # transaction_code = 200

                    if transaction_code not in range(200, 300):
                        # Inform the error microservice
                        print('\n\n-----Publishing the Transaction error message with routing_key=trans.error-----')
                        send_payment_details_to_rabbitmq(EXCHANGE, "topic", "error", "transactions.error", transaction_result)
                
                        return jsonify(transaction_result), transaction_code
                    
                except Exception as e:
                    # Unexpected error in code
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                    print(ex_str)

                    return jsonify({"error": "Transaction microservice has an internal error: " + ex_str}), 500
            
            
                try:
                    flight_details = {
                        "origin" : paymentDetails.depart_origin,
                        "destination" : paymentDetails.depart_destination,
                        "seat_num" : paymentDetails.depart_seats
                    }
                    email_details = create_email_template("confirmation", flight_details)
                    # 5. Sends confirmation email to user 
                    confirmation_data = {
                        "email": paymentDetails.user_email,
                        "notification_type": email_details["subject"],
                        "notification_message": email_details["message"],
                    }   
                    print('\n-----Invoking Notifications -----')

                    noti_payment_result =  send_payment_details_to_rabbitmq(EXCHANGE, "topic", "notifications", "complete.notifications", confirmation_data)

                    print('\n------------------------')
                    print('noti_payment_result:', noti_payment_result)

                    noti_payment_code = noti_payment_result["code"]

                    if noti_payment_code not in range(200, 300):
                        # Inform the error microservice
                        print('\n\n-----Publishing the Notification error message with routing_key=noti.error-----')
                        send_payment_details_to_rabbitmq(EXCHANGE, "topic", "error", "notifications.error", noti_payment_result)
                
                        return jsonify(noti_payment_result), noti_payment_code
                    
                except Exception as e:
                    # Unexpected error in code
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                    print(ex_str)

                    return jsonify({"error": "Notifications mciroservice has an internal error: " + ex_str}), 500
                
                
                try:
                    net_loyalty_points = int(paymentDetails.base_price * 0.1 - paymentDetails.loyalty_points)
                    # 5. Calculate loyalty points and send to Users
                    loyalty_points_data = {
                        "loyalty_points": net_loyalty_points
                    }   
                    print('\n-----Invoking User -----')

                    user_result = send_payment_details_to_users(paymentDetails.user_email, loyalty_points_data)

                    print('\n------------------------')
                    print('user_result:', user_result)

                    user_code = user_result['status']
                    accumulated_loyalty_points = user_result["loyalty_points"]

                    if not user_code:
                        # Inform the error microservice
                        print('\n\n-----Publishing the User error message with routing_key=user.error-----')
                        send_payment_details_to_rabbitmq(EXCHANGE, "topic", "error", "user.error", user_result)
                
                        return jsonify(user_result), user_code
                    
                    else:

                        # 6. Sends accumulated loyalty points email to user
                        points_details = accumulated_loyalty_points
                        email_details = create_email_template("points", points_details)

                        noti_points_data = {
                            "email": paymentDetails.user_email,
                            "notification_type": email_details["subject"],
                            "notification_message": email_details["message"],
                        }   

                        print('\n-----Invoking Notifications -----')

                        noti_points_result = send_payment_details_to_rabbitmq(EXCHANGE, "topic", "notifications", "points.notifications", noti_points_data)

                        print('\n------------------------')
                        print('noti_points_result:', noti_points_result)


                        if not noti_points_result:
                            # Inform the error microservice
                            print('\n\n-----Publishing the Notifications error message with routing_key=noti.error-----')
                            send_payment_details_to_rabbitmq(EXCHANGE, "topic", "error", "noti.error", noti_points_result)
                    
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
        
        return jsonify({"message":"success"}), 200