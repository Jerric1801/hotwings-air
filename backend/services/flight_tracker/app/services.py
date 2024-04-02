import requests  # Or the library you use for API calls
import os, sys
import pika
import json 
from .amqp_connection import create_connection, check_exchange

def send_payment_details_to_rabbitmq(exchangename, exchangetype, microservice, routing_key, payload):

   #create a connection and a channel to the broker to publish messages to error queues
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
    return {"code": 200}