import requests
import json

entry = {
    "flight_id": "HWA550", 
    "seat_class": "Economy",
    "customer_id": "CUST12345" 
}
# response = requests.post("http://localhost:5002/flights/new", json = entry)

response = requests.get("http://localhost:5002/pricing/HWA550")
print(response.content)