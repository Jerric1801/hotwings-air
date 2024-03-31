#!/usr/bin/env python3
import threading
import amqp_connection
import json
import pika
from flask import Flask, jsonify, request
from jinja2 import Template
import requests

# Initialize Flask app
app = Flask(__name__)

a_queue_name = 'Activity_Log'  # Queue to be subscribed by Activity_Log microservice
activity_log_data = []  # Global variable to store the activity logs

def callback(channel, method, properties, body): 
    global activity_log_data
    print("\nactivity_log: Received an activity log")
    activity_data = json.loads(body)
    activity_log_data.append(activity_data)
    print("activity_log: Recorded activity log.")
    send_to_activities_route(activity_data)  # Call function to send data to Flask route

def processActivityLog(activity_data):
    print("activity_log: Recording activity log from all sources:")

    template_text = """
    {% for service, activities in services_activities.items() %}
    Microservice: {{ service }}
    Actions:
    {% for activity in activities %}
        - Timestamp: {{ activity.timestamp }}
    {% else %}
      No actions recorded.
    {% endfor %}
    {% endfor %}
    """

    template = Template(template_text)
    rendered_output = template.render(services_activities=activity_data)

    print(rendered_output)

def receiveActivityLog(channel):
    try:
        channel.basic_consume(queue=a_queue_name, on_message_callback=callback, auto_ack=True)
        print(f'activity_log: Consuming from queue: {a_queue_name}')
        channel.start_consuming()
    except pika.exceptions.AMQPError as e:
        print(f"activity_log: Failed to connect: {e}")
    except KeyboardInterrupt:
        print("activity_log: Program interrupted by user.")

def send_to_activities_route(activity_data):
    # Define the URL of the Flask app where the route is hosted
    url = 'http://127.0.0.1:5000/activities'  # Update the URL if needed

    try:
        # Send a POST request to the route with the activity_data as JSON
        response = requests.post(url, json=activity_data)

        # Check the response status
        if response.status_code == 200:
            print("Data sent successfully to /activities route.")
        else:
            print("Error sending data to /activities route. Status Code:", response.status_code)
    except requests.RequestException as e:
        print("Error sending data to /activities route:", e)

@app.route('/activities', methods=['GET', 'POST'], endpoint='activities_route')
def activities():
    global activity_log_data
    if request.method == 'GET':
        return jsonify(activity_log_data)
    elif request.method == 'POST':
        data = request.get_json()
        activity_log_data.append(data)
        return jsonify({'message': 'Data received successfully.'})

def start_consuming():
    print("activity_log: Getting Connection")
    connection = amqp_connection.create_connection()
    print("activity_log: Connection established successfully")
    channel = connection.channel()
    receiveActivityLog(channel)

if __name__ == "__main__":
    threading.Thread(target=start_consuming).start()  # Run the RabbitMQ consumer in a separate thread
    app.run(debug=True)  # Start the Flask web server
