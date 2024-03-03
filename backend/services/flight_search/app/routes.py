from flask import jsonify, request
from app import app

@app.route('/search', methods = ["GET"])
def search_flights():
    if request.method == "GET":
        pass