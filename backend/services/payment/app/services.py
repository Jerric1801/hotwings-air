import requests  # Or the library you use for API calls
import os, sys
import pika
import json 
import amqp_connection

# function 1 to stripe
def send_payment_details_to_stripe(payload):
    url="http://localhost:5000/payment/stripe"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to stripe")

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
             
# function 3 to transactions
def send_payment_details_to_transactions(payload):
    url="http://localhost:5000/transaction"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to transactions")
       
# function 4 to users
def send_payment_details_to_users(payload):
    user_id = payload["user_id"]
    url=f"http://localhost:5000/users/{user_id}"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to users")
        
# function 5 to notifications
def send_payment_details_to_notifications(payload):
    url="http://localhost:5000/notifications"
    response = requests.post(url, json = payload)
    print(response) 

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to send payment details over to notifications")
    
# function 6 to errors
def send_errors(exchangename, exchangetype, error_key, payload):
    
    #create a connection and a channel to the broker to publish messages to error queues
    connection = amqp_connection.create_connection() 
    channel = connection.channel()

    #if the exchange is not yet created, exit the program
    if not amqp_connection.check_exchange(channel, exchangename, exchangetype):
        print("\nCreate the 'Exchange' before running this microservice. \nExiting the program.")
        sys.exit(0)  # Exit with a success status

    url="http://localhost:5000/errors"
    response = requests.post(url, json = payload)
    print(response) 
    code = payload["code"]
    message = json.dumps(payload)

    if response.status_code == 200:
        channel.basic_publish(exchange=exchangename, routing_key=f"{error_key}.error", 
                    body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
        print(f"\n {error_key} status ({code}) published to the RabbitMQ Exchange:", message)

        # Return error
        return {
            "code": 500,
            "data": {f"{error_key}_result":message},
            "message": f"{error_key} failure sent for error handling."
        }
    
    else:
        raise Exception("Failed to send error details over to errors")