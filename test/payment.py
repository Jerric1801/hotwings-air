from flask import Flask, jsonify
import requests 

app = Flask(__name__)

payment_url = "http://localhost:5000/flight_inventory"

@app.route('/payment',  methods=['POST']) 
def update_inventory():
    payment_data = "{'seat': '20a'}"
    response = requests.post(payment_url, json = payment_data)

    if response.status_code == 200:
        reply = "flight updated"
    else:
        reply = "flight not updated"

    return reply


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5001) 