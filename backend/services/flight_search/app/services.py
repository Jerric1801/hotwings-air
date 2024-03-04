import requests  # Or the library you use for API calls
from datetime import datetime, timedelta

def call_flight_inventory(payload):
    url = "http://localhost:5000"
    endpoint = f"/flight/search"
    response = requests.post(url + endpoint, json = payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to retrieve flight details")  # Handle error appropriately

# Other service functions for querying the inventory service 