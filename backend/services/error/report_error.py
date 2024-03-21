#THIS FILE IS A PLACEHOLDER FOR PAYMENT MICROSERVICE SENDING OVER DETAILS WHEN AN ERROR OCCURS
import pika
import json

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='error_logs')

# Send a message
test_message = {
    'error_source': 'user',
    'error_description': 'unsuccessful update of loyalty points.'
}
channel.basic_publish(exchange='',
                      routing_key='error_logs',
                      body=json.dumps(test_message))

print(" [x] Sent 'test_message'")

# Close the connection
connection.close()