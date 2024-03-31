import pika
from .models import ActivityLog

# Dummy in-memory storage for logs
# In a real application, this should be replaced with a database
logs = []

def consume_messages():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='activity_log')

    def callback(ch, method, properties, body):
        print(f"Received {body}")
        logs.append(ActivityLog(message=body.decode()))
        ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message

    channel.basic_consume(queue='activity_log', on_message_callback=callback, auto_ack=False)

    print('Starting to consume messages from RabbitMQ')
    channel.start_consuming()

def get_logs():
    return logs
