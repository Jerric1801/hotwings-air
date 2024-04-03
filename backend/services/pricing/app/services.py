import pika
import json
import os, sys
from .amqp_connection import create_connection, check_exchange


def send_amqp_message(exchangename, exchangetype, microservice, routing_key, payload):
    connection = create_connection() 
    channel = connection.channel()

    #if the exchange is not yet created, exit the program
    if not check_exchange(channel, exchangename, exchangetype):
        print(f"\nCreate the 'Exchange' before running the {microservice} microservice. \nExiting the program.")
        sys.exit(0)  # Exit with a success status

    message = json.dumps(payload)
    print(message)

    # Publish message to specific queue based on the routing_key
    channel.basic_publish(exchange=exchangename, routing_key=f"{routing_key}", body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        
    print(f"\n Message is published to the RabbitMQ Exchange under {microservice} and Activity_Log queue:", message)

    channel.close()
    connection.close()

def process_data(body):
    data = json.loads(body)
    print(data)
    if(data['new_flight'] != ""):
        user_email = data['user_email']
        flight_number_n = data['new_flight']['flight_number']
        flight_number_o = data['old_flight']['flight_number']
        seat_class_o = data['old_flight']['flight_class']
        seat_class_n = data['new_flight']['flight_class']
        original_pricing = get_pricing(flight_number_o,seat_class_o)
        new_pricing = get_pricing(flight_number_n,seat_class_n)
        difference = original_pricing - new_pricing
        if(new_pricing < original_pricing):
            add_points = original_pricing - new_pricing
            trans_payload = {
                "user_email": user_email,
                "type":"points",
                "amount": difference
            }
            user_payload = {
                "email": user_email,
                "loyalty_points": int(add_points)
            }
            print(user_payload)
            send_amqp_message("hotwings", "topic", "user", "p.user", user_payload)
        trans_payload = {
            "user_email": user_email,
            "type":"money",
            "amount": difference
        }
        print(trans_payload)
        send_amqp_message("hotwings", "topic", "transactions", "p.transactions", trans_payload)

    else:
        user_email = data['user_email']
        flight_number_o = data['old_flight']['flight_number']
        seat_class_o = data['old_flight']['flight_class']
        # points = 800
        points = get_pricing(flight_number_o,seat_class_o)
        user_payload = {
            "email":"",
            "loyalty_points": int(points)
        }
        trans_payload = {
            "user_email": user_email,
            "type":"points",
            "amount": points
        }
        print(trans_payload)
        print(user_payload)
        send_amqp_message("hotwings", "topic", "transactions", "p.transactions", user_payload)
        send_amqp_message("hotwings", "topic", "user", "p.user", trans_payload)

def callback(channel, method, properties, body):
    process_data(body)
    print(" [x] Received %r" % body)

def consume_amqp_messages(channel):
    try:
        channel.basic_consume(queue="pricing", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    
    except pika.exceptions.AMQPError as e:
        print(f"pricing microservice: Failed to connect: {e}") 

    except KeyboardInterrupt:
        print("pricing microservice: Program interrupted by user.")

def get_pricing(flight_number, seat_class):
    from .models import Pricing
    flight = Pricing.query.filter_by(flight_number=flight_number, seat_class=seat_class).first()
    if flight:
        price = flight.price
        print(price)
        return price