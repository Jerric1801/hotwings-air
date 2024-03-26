import requests
import json

response = requests.post("http://127.0.0.1:5001/flight_search", json = {
    "origin": "Bangkok",
    "destination": "Kuala Lumpur",
    "departureDate": "2024-04-01T15:50:06.107Z",
    "returnDate": "2024-04-10T01:50:06.107Z",
    "pax": 2,
    "seatClass": "Economy",
    "tripType": "roundtrip"
})

print(json.loads(response.content))

# entry = {
#     "flight_id": "HWA574", 
#     "seat_class": "Economy",
#     "customer_id": "CUST12345" 
# }
# # response = requests.post("http://localhost:5002/flights/new", json = entry)

# response = requests.get("http://localhost:5002/pricing/HW390/First")
# print(response.content)