import pika
import json
import uuid
from datetime import datetime

db_path = 'db.json'  # REPLACE WITH DB!!**

def add_transaction_log(total_price, user_id, loyalty_points=None, price_difference=None):
    log_id = str(uuid.uuid4())
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Construct the new log entry
    log_entry = {
        "log_id": log_id,
        "date_time": date_time,
        "user_id": user_id
    }

    # Add optional fields only if they have been provided (can be used by both scenario 1 & 3)
    if total_price is not None:
        log_entry["total_price"] = total_price
    if loyalty_points is not None:
        log_entry["loyalty_points"] = loyalty_points
    if price_difference is not None:
        log_entry["price_difference"] = price_difference

    # Read the existing data from DB
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

        # Extract data with defaults if not present
        total_price = message.get('total_price')
        user_id = message.get('user_id')
        loyalty_points = message.get('loyalty_points')
        price_difference = message.get('price_difference')

        add_transaction_log(
            total_price=total_price,
            user_id=user_id,
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

    queue_name = 'transaction_logs'
    channel.queue_declare(queue=queue_name)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_transaction()
