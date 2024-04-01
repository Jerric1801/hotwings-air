# from flask import Flask, request, jsonify
# import pika
# import json

# app = Flask(__name__)

# # Replace these with your actual connection parameters
# rabbitmq_host = 'localhost'
# queue_name = 'test.queue'  # The queue your Pricing microservice consumes from

# def send_message_to_queue(message):
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()
    
#     # Ensure the queue exists
#     channel.queue_declare(queue=queue_name, durable=True)
    
#     # Sending the message
#     channel.basic_publish(
#         exchange='',
#         routing_key=queue_name,
#         body=json.dumps(message),
#         properties=pika.BasicProperties(
#             delivery_mode=2,  # Make message persistent
#         ))
    
#     print(f"Sent: {message}")
#     connection.close()

# @app.route('/send', methods=['POST'])
# def send():
#     data = request.json
#     send_message_to_queue(data)
#     return jsonify({'message': 'Message sent successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
