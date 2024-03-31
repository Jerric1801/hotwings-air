from flask import Blueprint, request, jsonify
from .models import ActivityLog  # Import your ActivityLog model
from .services import add_activity_log, get_all_activity_logs  # Import your service functions
import json
from mongoengine import connect  # Import MongoDB connection

activity_blueprint = Blueprint('activity', __name__)

connect('activity_logs_db')  # Replace 'activity_logs_db' with actual database name

@activity_blueprint.route('/activities', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        
        # Call the add_activity_log service function to create and save the new ActivityLog entry
        new_log = add_activity_log(
            service=data['service'],
            timestamp=data['timestamp'],
            action=data['action']
        )
        
        # Convert the log to JSON and return a success response
        return jsonify(json.loads(new_log.to_json())), 201
    
    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error': str(e)}), 500

@activity_blueprint.route('/activities', methods=['GET'])
def get_activities():
    try:
        # Call the service function to retrieve all activity logs
        logs = get_all_activity_logs()
        
        # Convert the logs to JSON
        logs_json = [json.loads(log.to_json()) for log in logs]
        
        # Return the logs
        return jsonify(logs_json), 200
    
    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error': str(e)}), 500
