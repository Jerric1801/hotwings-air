#!/usr/bin/env python3
import pika
import json
import amqp_connection
from datetime import datetime

def send_activity_log(message, queue_name='Activity_Log'):
    # Establish a connection using the function from amqp_connection.py
    connection = amqp_connection.create_connection()
    channel = connection.channel()

    # Ensure the queue exists before sending a message
    channel.queue_declare(queue=queue_name, durable=True)

    # Convert the message to a JSON string if it's a dictionary
    if isinstance(message, dict):
        message = json.dumps(message)

    # Send the message
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(f"Sent to {queue_name}: {message}")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    # Get the current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Structure the message to fit the expected template format
    services_activities = {
        'Payment Microservice': [  
            {
                'timestamp': current_timestamp,
            },
        ],
    }

    send_activity_log(services_activities)
