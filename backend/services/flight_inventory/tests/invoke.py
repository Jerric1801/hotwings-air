import requests
import json

body = {
    "base_price": 1658,
    "depart_arrival_time": "2024-04-02T05:23:29.636Z",
    "depart_departure_time": "2024-04-02T00:35:29.636Z",
    "depart_destination": "Dubai",
    "depart_flight_number": "HW436",
    "depart_id": "6609911c4564d0b4199d7359",
    "depart_origin": "Kuala Lumpur",
    "depart_seat_id": "6609911c4564d0b4199d7358",
    "depart_seats": ["11E", "11F"],
    "loyalty_points": 0,
    "other_passengers": [],
    "return_arrival_time": "2024-04-23T07:17:29.591Z",
    "return_departure_time": "2024-04-23T00:35:29.591Z",
    "return_destination": "Kuala Lumpur",
    "return_flight_number": "HW452",
    "return_id": "660991144564d0b4199d7275",
    "return_origin": "Dubai",
    "return_seat_id": "660991144564d0b4199d7274",
    "return_seats": ["4B", "4C"],
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
