import requests  # Or the library you use for API calls
import os, sys
import pika
import json 
from .amqp_connection import create_connection, check_exchange



       
# function 1 to flight_inventory #ASK JERRIC
def update_flight_inventory(payload):
    url="http://localhost:5000/flight_inventory"
    response = requests.put(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send flight details over to flight inventory")
        
    
# function 2 to send message to AMQP via rabbitMQ
def send_message_to_rabbitmq(exchangename, exchangetype,microservice, routing_key, payload):
    
    #create a connection and a channel to the broker to publish messages 
    connection = create_connection() 
    channel = connection.channel()

    #if the exchange is not yet created, exit the program
    if not check_exchange(channel, exchangename, exchangetype):
        print("\nCreate the 'Exchange' before running this microservice. \nExiting the program.")
        sys.exit(0)  # Exit with a success status

    message = json.dumps(payload)

    channel.basic_publish(exchange=exchangename, routing_key=f"{routing_key}", 
                body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
    print(f"\n Message is published to RabbitMQ Exchange under {microservice} and Activity_Log queue:", message)

#function 3:

def create_email_template(type, details):
    if type == "confirmation":
        subject = "Flight Booking Confirmed!"

        if "accommodation" in details:
            accommodation = details["accommodation"]
            message = f"Dear Sir/Madam, \n\nThanks for flying with Hotwings. \
            \n\n We're sorry to hear about your delayed flights and have arranged a new flight and accommodation for you. Your confirmed itinerary details are shown below: \
            \n\n Place of Origin: {details['origin']}\n Place of Destination: {details['destination']} \n Seat Numbers: {','.join([seat for seat in details['seat_num']])}\n \
            \n\nYou have successfully secured an accomodation at {accommodation['hotel_name']} located at {accommodation['location_near']} \
            \n\nWe hope you have a pleasant trip ahead! \
             \n\n~~~~~~~~~~Hotwings provide you the wings to fly to any destinations possible!~~~~~~~~~~"
        else: 
            message = f"Dear Sir/Madam, \n\nThanks for flying with Hotwings. \
            \n\nWe're excited to inform you of your flight details for your upcoming trip. Your confirmed itinerary details are shown below: \
            \n\n Place of Origin: {details['origin']}\n Place of Destination: {details['destination']} \n Seat Numbers: {','.join([seat for seat in details['seat_num']])} \
            \n\nWe hope you have a pleasant trip ahead!\
            \n\n~~~~~~~~~~Hotwings provide you the wings to fly to any destinations possible!~~~~~~~~~~"

    elif type == "points": 
        subject = "Accumulated Loyalty Points"
        message = f"Dear Sir/Madam, \n\nThanks for flying with Hotwings.\
        \n\nYour total loyalty point as of today is: {details}. \
        \n\nHope to see you onboard of our flight soon!\
        \n\n~~~~~~~~~~Hotwings provide you the wings to fly to any destinations possible!~~~~~~~~~~"


       