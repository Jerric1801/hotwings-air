import requests  # Or the library you use for API calls
from datetime import datetime, timedelta

def call_flight_inventory(payload):
    url = "http://flight_inventory:5000/flight/search"
    response = requests.post(url, json = payload)

    print(response)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to retrieve flight details")  # Handle error appropriately

# Other service functions for querying the inventory service 