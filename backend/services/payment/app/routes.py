from flask import Flask, render_template, request, jsonify, make_response, redirect
from app import app
from .utils import stripe_keys
from .services import send_payment_details_to_flight_inventory,send_payment_details_to_transactions,send_payment_details_to_users,send_payment_details_to_notifications, send_errors, create_stripe_checkout_session
from .models import Payment
import os, sys
import json 
import stripe


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/config", methods = ["GET"])
def get_publishable_key():
    if request.method == "GET":
        stripe_config = {"publicKey": stripe_keys["publishable_key"]}
        return jsonify(stripe_config)

@app.route('/payment/stripe', methods = ["POST"])
def send_payment_data():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            data = request.get_json()
            print("\nReceived a record of payment details in JSON:", data)
            total_price = data.get('total_price')
            seat_number = data.get('seat_number')
            flight_id = data.get('flight_id')
            loyalty_points = data.get('loyalty_points')
            user_id = data.get('user_id')
            user_email = data.get('user_email')

            paymentDetails = Payment(total_price, seat_number, flight_id, loyalty_points, user_id, user_email)

            # do the actual work
            # 1. Send payment info to Stripe
            # stripe_data = {
            #     "description": paymentDetails.flight_id , 
            #     "price": paymentDetails.total_price,
            #     "points_used": loyalty_points,
            # }
            print('\n-----Invoking Stripe API-----')
            # stripe_result = send_payment_details_to_stripe(stripe_data)
        
            print('\n------------------------')
            # print('stripe_result:', session_data)

            session_data = create_stripe_checkout_session(
                product_description = paymentDetails.flight_id,
                unit_amount = paymentDetails.total_price,
                points_used = paymentDetails.loyalty_points
            )
            print('stripe_result:', session_data)

            # code = stripe_result["code"]
            code = session_data["code"]

            if code not in range(200, 300):
                # Inform the error microservice
                print('\n\n-----Publishing the Stripe error message with routing_key=stripe.error-----')
                # stripe_result = send_errors("stripe.topic", "topic", "stripe", stripe_result)
                session_data = send_errors("stripe.topic", "topic", "stripe", session_data)
            
            # return jsonify(stripe_result), code
            return jsonify(session_data), code

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({"error": "Stripe Payment has an internal error: " + ex_str}), 500
        
        try:
            pass 
        except: 
            pass

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400



    # Notice that we are publishing to "Activity Log" only when there is no error in order creation.
    # In http version, we first invoked "Activity Log" and then checked for error.
    # Since the "Activity Log" binds to the queue using '#' => any routing_key would be matched 
    # and a message sent to “Error” queue can be received by “Activity Log” too.

    # else:
    #     # 4. Record successful stripe payment
    #     # record the transaction anyway
    #     print('\n\n-----Invoking transaction microservice-----')
    #     # print('\n\n-----Publishing the stripe info message with routing_key=stripe.info-----')        

    #     send_payment_details_to_transactions(stripe_result)            
    #     # channel.basic_publish(exchange=exchangename, routing_key="stripe.info", body=message)
    
    # print("\nStripe Payment published to RabbitMQ Exchange.\n")
    
    # # 5. Send payment details to flight_inventory
    # print('\n\n-----Invoking flight_inventory microservice-----')    
    # flight_inventory_data = {
       
    # }
    # flight_inventory_result = send_payment_details_to_flight_inventory(flight_inventory_data)
    # print("flight_inventory_result:", flight_inventory_result, '\n')

    # # Check the flight_inventory_result;
    # # if a failure, send it to the error microservice.
    # code = flight_inventory_result["code"]
    # if code not in range(200, 300):
    #     # Inform the error microservice
    #     print('\n\n-----Invoking error microservice as updating flight inventory fails-----')
    #     # print('\n\n-----Publishing the flight_inventory message with routing_key=flight_inventory.error-----')

    #     send_errors(flight_inventory_result)
    #     # message = json.dumps(flight_inventory_result)
    #     # channel.basic_publish(exchange=exchangename, routing_key="flight_inventory.error", 
    #     #     body=message, properties=pika.BasicProperties(delivery_mode = 2))

    #     print("\nFlight inventory update status ({:d}) published to the RabbitMQ Exchange:".format(code), flight_inventory_result)

    #     # 7. Return error
    #     return {
    #         "code": 400,
    #         "data": {
    #             "stripe_result": stripe_result,
    #             "flight_inventory_result": flight_inventory_result
    #         },
    #         "message": "Simulated flight_inventory error sent for error handling."
    #     }

    # 7. Return created stripe payment, flight_inventory record
    return {
        "code": 201,
        "data": {
            "stripe_result": stripe_result,
            "flight_inventory_result": flight_inventory_result
        }
    } 

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
        points = round(amount_paid*1.2/100)
        # currency = payment_intent.currency

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
