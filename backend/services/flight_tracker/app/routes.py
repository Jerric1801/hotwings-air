from flask import jsonify, request, render_template
from app import app
from .services import send_payment_details_to_rabbitmq


@app.route('/flight_tracker')
def flight_tracker():
    return render_template('index.html.j2') 


@app.route('/flight_tracker/invoke', methods = ["POST"])
def invoke():
    if request.method == "POST":
        data = request.get_json() 
        send_payment_details_to_rabbitmq("hotwings", "topic", "tracker", 'dispatch.tracker', data)
        return jsonify({"message":"data sent"}), 200