import pika
import json
import uuid
from datetime import datetime

db_path = 'db.json'  # REPLACE WITH DB!!**

def add_transaction_log(type, user_id, payment_amt=None, loyalty_points=None, price_difference=None):
    log_id = str(uuid.uuid4())
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "log_id": log_id,
        "date_time": date_time,
        "type": type,
        "user_id": user_id,
    }

    # Add optional fields only if they have been provided (can be used by both scenario 1 & 3)
    if payment_amt is not None:
        log_entry["payment_amt"] = payment_amt
    if loyalty_points is not None:
        log_entry["loyalty_points"] = loyalty_points
    if price_difference is not None:
        log_entry["price_difference"] = price_difference

    # Read the existing data from DB (REPLACE WITH DB!!**)
    try:
        with open(db_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If DB does not exist, start with an empty list
        data = {"logs": []}

    # Append the new log entry
    data["logs"].append(log_entry)

    # Write the updated data back to DB (Will be replaced with sending in SQL/DB Syntax)
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Log entry added to db.json:", log_entry)

def callback(ch, method, properties, body):
    print("Received raw message:", body)
    try:
        message = json.loads(body)
        print(" [x] Received %r" % message)

        type = message['type']  
        user_id = message['user_id']
        # Extract data with defaults if not present
        payment_amt = message.get('payment_amt')
        loyalty_points = message.get('loyalty_points')
        price_difference = message.get('price_difference')

        add_transaction_log(
            type=type,
            user_id=user_id,
            payment_amt=payment_amt,
            loyalty_points=loyalty_points,
            price_difference=price_difference
        )
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")

def consume_transaction():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    queue_name = 'Transactions'
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_transaction()
