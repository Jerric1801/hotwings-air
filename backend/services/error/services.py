# Add error log function has been moved to rabbitmq_consumer.py (THIS FILE MIGHT NOT BE NEEDED)

# import os
# import json
# import uuid
# from datetime import datetime

# # Service to add a new error log
# # Assuming this script is located in the 'services/error' directory
# # Adjust the path as necessary if running from a different location
# db_path = os.path.join(os.getcwd(), 'tests', 'db.json')

# def add_error_log(flight_id, user_email, error_description):
#     log_id = str(uuid.uuid4())
#     date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Construct the new log entry
#     log_entry = {
#         "log_id": log_id,
#         "date_time": date_time,
#         "flight_id": flight_id,
#         "user_email": user_email,
#         "error_description": error_description
#     }

#     # Read the existing data from db.json
#     try:
#         with open(db_path, 'r') as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = {"logs": []}

#     # Append the new log entry
#     data["logs"].append(log_entry)

#     # Write the updated data back to db.json
#     with open(db_path, 'w') as file:
#         json.dump(data, file, indent=4)

#     print("Log entry added to db.json:", log_entry)