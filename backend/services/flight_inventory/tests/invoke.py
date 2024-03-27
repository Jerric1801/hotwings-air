import requests
import json

# response = requests.get("http://127.0.0.1:5000/flight/Singapore/origin")
# response = requests.post("http://127.0.0.1:5001/flight_search", json = {
#     "origin": "Bangkok",
#     "destination": "Hong Kong",
#     "departureDate": "2024-04-10T15:50:06.107Z",
#     "returnDate": "2024-04-15T01:50:06.107Z",
#     "pax": 2,
#     "seatClass": "Premium Economy",
#     "tripType": "roundtrip"
# })

# response = requests.post("http://127.0.0.1:5000/flight/search", json = {
#     "origin": "Singapore",
#     "destination": "Manila",
#     "date": "2024-03-06T16:00:00.000Z",
#     "pax": 2,
#     "class": "Premium Economy",
# })

response = requests.post("http://127.0.0.1:5001/flight_search/seating", json = {
    "departId":"6602c23382d1f7e577cbdb53",
    "returnId":"6602c25782d1f7e577cbddad"
})
print(response.content)
