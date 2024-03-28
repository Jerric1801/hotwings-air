from flask import Blueprint, request, jsonify
from .models import ErrorLog
from .services import add_error_log
from .services import get_all_error_logs
import json
from mongoengine import connect

error_blueprint = Blueprint('error', __name__)

connect('error_logs_db')  # Replace 'error_logs_db' with actual database name

@error_blueprint.route('/log', methods=['POST'])
def create_log():
    try:
        data = request.get_json()
        
        # Call the add_error_log service function to create and save the new ErrorLog entry
        new_log = add_error_log(
            code=data['code'],
            data=data['data'],
            message=data['message']
        )
        
        # Convert the log to JSON and return a success response
        return jsonify(json.loads(new_log.to_json())), 201
    
    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error': str(e)}), 500

@error_blueprint.route('/logs', methods=['GET'])

def get_logs():
    try:
        # Call the service function to retrieve all error logs
        logs = get_all_error_logs()
        
        # Convert the logs to JSON
        logs_json = [json.loads(log.to_json()) for log in logs]
        
        # Return the logs
        return jsonify(logs_json), 200
    
    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error': str(e)}), 500
