from flask import Flask, render_template, request, jsonify, make_response, redirect
from app import app
from .utils import stripe_keys
import stripe

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/config", methods = ["GET"])
def get_publishable_key():
    if request.method == "GET":
        stripe_config = {"publicKey": stripe_keys["publishable_key"]}
        return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5001/"
    stripe.api_key = stripe_keys["secret_key"]
    try:
        product = stripe.Product.create(
            name='ticket',
            description='SIN-NZ',
        )

        price = stripe.Price.create(
            product=product.id,
            unit_amount= 90000,
            currency='sgd',
        )
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            mode="payment",
            custom_text={
                "submit": {"message":"Points used: 600"}
                #need to pass in the points used from the ui??
            },
            line_items=[
                {
                    'price': price.id,
                    'quantity': 1,
                }
            ],
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403   

@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")

@app.route('/success')
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

        # Render success.html with dynamic payment details
        return render_template("success.html", payment_intent_id=payment_intent_id, amount_paid=amount_paid, currency=currency.upper(), deets=payment_intent, points=points)
    except Exception as e:
        return f"An error occurred: {e}", 403