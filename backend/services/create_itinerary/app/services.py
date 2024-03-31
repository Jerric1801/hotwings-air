import requests  # Or the library you use for API calls
import os, sys
import pika
import json 
from .amqp_connection import create_connection, check_exchange

# function 1 to flight inventory
def send_flight_details_to_search_flight(payload):
    json_string = json.dumps(payload)
    url=f"http://localhost:5000/search_flight"
    response = requests.post(url, json = json_string)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send flight details over to flight search")   
       
# function 2 to search accomodation
def send_flight_details_to_search_accomodation(payload):
    json_string = json.dumps(payload)
    url=f"http://localhost:5000/search_accomodation"
    response = requests.post(url, json = json_string)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send flight details over to search accomodation")

# function 3 to create webpage
def send_flight_details_to_custom_webpage(payload):
    json_string = json.dumps(payload)
    url=f"http://localhost:5000/custom_webpage"
    response = requests.post(url, json = json_string)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send itinerary details over to create webpage")
    
# function 4 publishing message via amqp to RabbitMQ
def send_flight_details_to_rabbitmq(exchangename, exchangetype, microservice, routing_key, payload):

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

    # Return error
    return {
        "code": 500,
        "data": {f"{microservice}_error":message},
        "message": f"Transmission of data to {microservice} microservice failure sent for error handling."
    }
    
