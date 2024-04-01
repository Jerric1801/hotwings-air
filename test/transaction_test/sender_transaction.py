#THIS FILE IS A PLACEHOLDER FOR PAYMENT MICROSERVICE SENDING OVER TRANSACTION DETAILS WHEN A TRANSACTION OCCURS
import pika
import json

# Establish connection 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (Create a Queue)
channel.queue_declare(queue='Transactions', durable=True)

# Send a message
test_message = {
  "type": "transaction_type",
  "user_id": "user_id_value",
  "payment_amt": 100.0,
  "loyalty_points": 50,
  "price_difference": 20.0
}
channel.basic_publish(exchange='',
                      routing_key='Transactions',
                      body=json.dumps(test_message))

print(" [x] Sent 'test_message'")

# Close the connection
connection.close()