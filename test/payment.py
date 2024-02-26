from flask import Flask, jsonify
import requests 

app = Flask(__name__)

payment_url = "http://localhost:5000/flight_inventory"

@app.route('/payment') 
def payment():
    
    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 