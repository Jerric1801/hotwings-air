#THIS FILE IS A PLACEHOLDER FOR PAYMENT MICROSERVICE SENDING OVER TRANSACTION DETAILS WHEN A TRANSACTION OCCURS
import pika
import json

# Establish connection 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (Create a Queue)
channel.queue_declare(queue='transaction_logs')

# Send a message
test_message = {
    'user_id': '1123465.',
    'loyalty_points': '1005',
    'price_difference': '100.50.'
    
}
channel.basic_publish(exchange='',
                      routing_key='transaction_logs',
                      body=json.dumps(test_message))

print(" [x] Sent 'test_message'")

# Close the connection
connection.close()