import json
import pika
from .models import TransactionLogEntry
from config import RABBITMQ_HOST, QUEUE_NAME, DB_PATH

def add_transaction_log(entry):
    try:
        with open(DB_PATH, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"logs": []}

    data["logs"].append(entry.__dict__)

    with open(DB_PATH, 'w') as file:
        json.dump(data, file, indent=4)
    print("Log entry added:", entry.__dict__)

def callback(ch, method, properties, body):
    print("Received raw message:", body)
    try:
        message = json.loads(body)
        entry = TransactionLogEntry(
            type=message['type'],
            user_id=message['user_id'],
            payment_amt=message.get('payment_amt'),
            loyalty_points=message.get('loyalty_points'),
            price_difference=message.get('price_difference')
        )
        add_transaction_log(entry)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except KeyError as e:
        print(f"Missing key in message: {e}")

def consume_transaction():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
