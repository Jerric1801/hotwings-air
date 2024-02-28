from flask import Flask, jsonify
import requests 
import pika
import amqp_connection as amqp

app = Flask(__name__)

payment_url = "http://localhost:5000/flight_inventory"

connection = amqp.create_connection()
channel = connection.channel()

if not amqp.check_exchange(channel, "payment_topic", "topic"):
    print("broker error")

@app.route('/payment',  methods=['POST']) 
def update_inventory():
    payment_data = "{'seat': '20a'}"
    response = requests.post(payment_url, json = payment_data)

    #send to message broker
    channel.basic_publish(exchange = "payment_topic", routing_key = "payment.#.", body = payment_data, properties = pika.BasicProperties(delivery_mode=2))

    if response.status_code == 200:
        reply = "flight updated"
    else:
        reply = "flight not updated"

    return reply


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5001) 