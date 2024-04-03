# import json
# import pika

# log = {}

# def consume_messages():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='activity_log')
    
#     def flush_logs_to_file(logs):
#         # Write the logs to the file in one go
#         with open('./test/db.json', 'w') as file:
#             json.dump(logs, file, indent=4)
    
#     def callback(ch, method, properties, body):
#         print(f"Received {body}")
#         log_data = json.loads(body.decode())

#         # Load existing data from the file
#         try:
#             with open('./test/db.json', 'r') as file:
#                 existing_data = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             existing_data = []

#         # Append new log data and flush to file
#         existing_data.append(log_data)
#         flush_logs_to_file(existing_data)

#         ch.basic_ack(delivery_tag=method.delivery_tag)

#     channel.basic_consume(queue='activity_log', on_message_callback=callback, auto_ack=True)

#     print('Starting to consume messages from RabbitMQ')
#     channel.start_consuming()

# def get_logs():
#     file_path = './test/db.json'
    
#     # Read and return the logs from db.json
#     try:
#         with open(file_path, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         # If the file doesn't exist, return an empty list
#         return []
#     except json.JSONDecodeError:
#         # If there's an error decoding the file, return an empty list or handle differently
#         return []
