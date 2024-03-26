import requests  # Or the library you use for API calls
from datetime import datetime, timedelta
import json

def call_flight_inventory(payload):
    url = "http://flight_inventory:5000/flight/search"
    response = requests.post(url, json = payload)

    if response.status_code == 200:

        return response.json()
    else:
        raise Exception("Failed to retrieve flight details")  

# Other service functions for querying the inventory service 
def add_pricing(options, seat_class):
    res = []

    if options == [] or options == None:
        return res

    for option in options:
        try:
            flight_number = option["flight_number"]
            try:
                url = f"http://pricing:5002/pricing/{flight_number}/{seat_class}"
                response = requests.get(url)
            except: 
                print("Error with calling price api")

            if response.status_code == 200:
                option["price"] = json.loads(response.content)
                #add to existing option
                res.append(option)
            else:
                raise Exception(f"Failed to retrieve pricing for flight {flight_number}")
        except Exception as e:
            print("Error retriving price and modifying option")


    return res
