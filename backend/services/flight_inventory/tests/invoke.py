import requests
import json

body = {
    "base_price": 406,
    "depart_arrival_time": "2024-04-02T02:11:26.949Z",
    "depart_departure_time": "2024-04-02T00:02:26.949Z",
    "depart_destination": "Manila",
    "depart_flight_number": "HW333",
    "depart_id": "66090cfdc5e575df516309eb",
    "depart_origin": "Jakarta",
    "depart_seat_id": "66090cfdc5e575df516309ea",
    "depart_seats": ["5C"],
    "loyalty_points": 0,
    "other_passengers": [],
    "return_arrival_time": "2024-04-02T01:44:26.960Z",
    "return_departure_time": "2024-04-02T00:02:26.960Z",
    "return_destination": "Jakarta",
    "return_flight_number": "HW244",
    "return_id": "66090cfec5e575df51630a25",
    "return_origin": "Manila",
    "return_seat_id": "66090cfec5e575df51630a24",
    "return_seats": ["1F"],
    "total_price": 0,
    "user_email": "jerric1801@gmail.com",
    "user_first": "Jerric",
    "user_gender": "Mr",
    "user_last": "Chan",
    "user_phone": ""
}
response = requests.post("http://127.0.0.1:5004/payment", json = body)


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

# response = requests.post("http://127.0.0.1:5001/flight_search/seating", json = {
#     "departId":"6602c23382d1f7e577cbdb53",
#     "returnId":"6602c25782d1f7e577cbddad"
# })

print(response.content)
