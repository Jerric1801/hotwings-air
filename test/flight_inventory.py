from flask import Flask, jsonify, request

app = Flask(__name__)

payment_url = "http://localhost:5001/payment"

@app.route('/flight_inventory', methods = ['POST']) 
def get_payment():
    data = request.get_json()

    return 'Inventory updated', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000) 