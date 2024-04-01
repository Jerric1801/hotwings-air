# import requests
# import json

# # response = requests.get("http://127.0.0.1:5000/flight/Singapore/origin")
# response = requests.post("http://127.0.0.1:5001/flight_search", json = {
#     "origin": "Singapore",
#     "destination": "Manila",
#     "departureDate": "2024-03-06T16:00:00.000Z",
#     "returnDate": "2024-03-19T16:00:00.000Z",
#     "pax": 2,
#     "seatClass": "Premium Economy",
#     "tripType": "roundtrip"
# })

# # response = requests.post("http://127.0.0.1:5000/flight/search", json = {
# #     "origin": "Singapore",
# #     "destination": "Manila",
# #     "date": "2024-03-06T16:00:00.000Z",
# #     "pax": 2,
# #     "class": "Premium Economy",
# # })
# print(response.content)
