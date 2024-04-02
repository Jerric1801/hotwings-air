import requests  # Or the library you use for API calls
import os, sys
import pika
import json 
from .amqp_connection import create_connection, check_exchange
import stripe 
from .utils import stripe_keys

# function 1 for creating checkout session to stripe
def create_stripe_checkout_session(product_description, unit_amount, points_used, currency='sgd'):
    stripe.api_key = stripe_keys["secret_key"]
    try:
        product = stripe.Product.create(name='ticket', description=product_description)
        price = stripe.Price.create(product=product.id, unit_amount=unit_amount, currency=currency)
        domain_url = "http://127.0.0.1:5001"

        checkout_session = stripe.checkout.Session.create(
            success_url=f"{domain_url}/payment/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{domain_url}/payment/cancelled",
            mode="payment",
            custom_text={
                "submit": {"message":"Points used: " + str(points_used)}
            },
            line_items=[{'price': price.id, 'quantity': 1}],
            metadata={"points_used": str(points_used)},  # Store points used here
        )
        return {"sessionId": checkout_session["id"],"code":200}
    except Exception as e:
        raise Exception(f"Stripe Checkout Session creation failed: {str(e)}")
#return stripe.redirectToCheckout({sessionId: data.sessionId}) --> redirects to stripe checkout page, shld be implemented on front end

# function 2 to flight inventory
def send_payment_details_to_flight_inventory(payload):
    flight_id = payload["flight_id"]
    url=f"http://localhost:5000/flight/{flight_id}"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to flight inventory")   
       
# function 3 to users
def send_payment_details_to_users(payload):
    user_id = payload["user_id"]
    print(user_id)
    url=f"http://localhost:5000/users/{user_id}"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to users")

# function 4 publishing message via amqp to RabbitMQ
def send_payment_details_to_rabbitmq(exchangename, exchangetype, microservice, routing_key, payload):

   #create a connection and a channel to the broker to publish messages to the different queues
    connection = create_connection() 
    channel = connection.channel()

    #if the exchange is not yet created, exit the program
    if not check_exchange(channel, exchangename, exchangetype):
        print(f"\nCreate the 'Exchange' before running the {microservice} microservice. \nExiting the program.")
        sys.exit(0)  # Exit with a success status

    message = json.dumps(payload)
    print(message)

    # Publish message to specific queue based on the routing_key
    channel.basic_publish(exchange=exchangename, routing_key=f"{routing_key}", 
                body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        
    print(f"\n Message is published to the RabbitMQ Exchange under {microservice} and Activity_Log queue:", message)
    