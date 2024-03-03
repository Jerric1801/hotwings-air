import requests
import json

response = requests.get("http://localhost:5000/flights")

print(response.content)

data = {
    "flight_number": "AB123",
    "departure": "2024-03-05T10:00:00",
    "arrival": "2024-03-05T13:30:00",
    "origin": "Singapore",
    "destination": "London",
    "aircraft": {
        "model": "Boeing 777",
        "capacity": 300,
        "seating_plan": {
            "seats": [
                {"seat_number": "1A", "class_type": "Business"},
                {"seat_number": "2A", "class_type": "Business"},
                # ... more seats ...
            ]
        }
    }
}

response = requests.post("http://localhost:5000/flights/new"
                         , headers={"Content-Type": "application/json"} 
                         , json = data)

print(response.content)
