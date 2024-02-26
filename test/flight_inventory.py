from flask import Flask, jsonify

app = Flask(__name__)

payment_url = "http://localhost:5000/payment"

@app.route('/flight_inventory') 
def get_seats():
    
    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 