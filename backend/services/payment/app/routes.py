from flask import Flask, render_template, request, jsonify
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
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]
    try:
        product = stripe.Product.create(
            name='ticket',
            description='SIN-NZ',
        )

        price = stripe.Price.create(
            product=product.id,
            unit_amount= 900,
            currency='sgd',
        )
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            mode="payment",
            line_items=[
                {
                    'price': price.id,
                    'quantity': 1,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403   

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")