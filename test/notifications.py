import pika
import json
import amqp_connection as ampq

def callback(channel, method, property, body):
    print(body)

connection = ampq.create_connection()
channel = connection.channel()
channel.basic_consume(queue="notification_queue", on_message_callback=callback, auto_ack=True) 
channel.start_consuming()