import requests
import json

# response = requests.get("http://127.0.0.1:5000/flight/Singapore/origin")
response = requests.post("http://127.0.0.1:5001/flight_search", json = {
    "origin": "Bangkok",
    "destination": "Hong Kong",
    "departureDate": "2024-03-30T15:50:06.107Z",
    "returnDate": "2024-03-31T01:50:06.107Z",
    "pax": 2,
    "seatClass": "Premium Economy",
    "tripType": "roundtrip"
})

# response = requests.post("http://127.0.0.1:5000/flight/search", json = {
#     "origin": "Singapore",
#     "destination": "Manila",
#     "date": "2024-03-06T16:00:00.000Z",
#     "pax": 2,
#     "class": "Premium Economy",
# })
print(response.content)
