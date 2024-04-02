import json
import pika
from .models import TransactionLogEntry
from config import RABBITMQ_HOST, QUEUE_NAME
from flask import jsonify

transactions = []

def add_transaction(entry):
    transactions.append(entry)
    print(f"Transaction added: {entry}")

def callback(ch, method, properties, body):
    print("Received raw message:", body)
    try:
        message = json.loads(body)
        entry = TransactionLogEntry(
            type=message.get('type'),
            user_id=message.get('user_id'),
            payment_amt=message.get('payment_amt'),
            loyalty_points=message.get('loyalty_points'),
            price_difference=message.get('price_difference')
        )
        add_transaction(entry)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except KeyError as e:
        print(f"Missing key in message: {e}")

def consume_transaction():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=False) 

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def get_all_transactions():
    return transactions