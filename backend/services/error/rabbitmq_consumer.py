import pika
import json
import uuid
from datetime import datetime


db_path = 'tests/db.json'  # REPLACE WITH DB!!**

def add_error_log(error_source, error_description):
    log_id = str(uuid.uuid4())
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Construct the new log entry
    log_entry = {
        "log_id": log_id,
        "date_time": date_time,
        "error_source": error_source,
        "error_description": error_description
    }

    # Read the existing data from DB
    try:
        with open(db_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If DB does not exist, start with an empty list
        data = {"logs": []}

    # Append the new log entry
    data["logs"].append(log_entry)

    # Write the updated data back to DB
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Log entry added to db.json:", log_entry)

def callback(ch, method, properties, body):
    print("Received raw message:", body)
    try:
        message = json.loads(body)
        print(" [x] Received %r" % message)
        add_error_log(
            error_source=message.get('error_source'),
            error_description=message.get('error_description')
        )
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")

def consume_errors():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='hotwings', exchange_type='topic')

    queue_name = 'error_logs'
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange='hotwings', queue=queue_name, routing_key='hotwings')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_errors()


