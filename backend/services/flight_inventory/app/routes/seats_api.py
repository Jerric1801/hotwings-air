from flask import Blueprint, jsonify, request

seats_bp = Blueprint('seats', __name__)

# Example data - Adapt this based on your actual requirements
available_seats = {
    "flight_123": ["A1", "A2", "B3"],
    "flight_456": ["C4", "D5"]
}

@seats_bp.route('/flights/<flight_id>/seats', methods=['GET'])
def get_available_seats(flight_id):
    seats = available_seats.get(flight_id)
    if seats:
        return jsonify(seats)
    else:
        return jsonify({"message": "Flight not found"}), 404

# ... Other routes related to seat selection, booking, etc. 