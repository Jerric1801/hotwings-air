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
    "loyalty_points": 20,
    "other_passengers": [],
    "return_arrival_time": "2024-04-23T07:17:29.591Z",
    "return_departure_time": "2024-04-23T00:35:29.591Z",
    "return_destination": "Kuala Lumpur",
    "return_flight_number": "HW452",
    "return_id": "660991144564d0b4199d7275",
    "return_origin": "Dubai",
    "return_seat_id": "660991144564d0b4199d7274",
    "return_seats": ["4B", "4C"],
    "total_price": 1800,
    "user_email": "jerric.chan.2022@scis.smu.edu.sg",
    "user_first": "Jerric",
    "user_gender": "Mr",
    "user_last": "Chan",
    "user_phone": ""
}

boyang = "byzhou.2022@scis.smu.edu.sg"
# response = requests.post("http://127.0.0.1:5004/payment", json = body)
    # private String flight_id;
    # private String date;
    # private String flight_number;
body1 =  {	
            "flight_id":"660cd42cbbb3208d39d36620",
            "flight_number": "HW586",
            "departure": "2024-04-03T00:35:29.626561",
        }

# response = requests.post("http://localhost:5008/flight_tracker/invoke", json = body1)
# response = requests.post("http://localhost:5010/create_itinerary", json = body1)

print("running")
body1 =  {'departure': '2024-04-03T00:35:29.626561', 'flight_number': 'HW586', 'recommended_flights': [{'departure': 'Fri, 05 Apr 2024 00:35:29 GMT', 'flight_number': 'HW586', 'availability': 132}], 'recommended_accommodation': [{'hotel_name': 'Four Seasons', 'availability': 2}, {'hotel_name': 'Four Seasons', 'availability': 4}, {'hotel_name': 'Four Seasons', 'availability': 4}, {'hotel_name': 'Four Seasons', 'availability': 2}], 'user_emails': ['jerric.chan.2022@scis.smu.edu.sg', 'byzhou.2022@scis.smu.edu.sg', 'jerric1811@gmail.com']}


response = requests.post("http://127.0.0.1:5012/form", json = body1)

# print(response.content)

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
