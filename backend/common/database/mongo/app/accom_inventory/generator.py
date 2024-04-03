import json
import random
import string
import uuid

# Data for seeding
countries = ["Singapore", "Tokyo", "Bangkok", "Sydney", "Hong Kong", "London", 
             "New York", "Kuala Lumpur", "Jakarta", "Manila", "Dubai", "Paris", 
             "Los Angeles"]
hotel_names = ["Marriott", "Hilton", "InterContinental", "Hyatt", "Sheraton", "Westin", "Four Seasons", "Ritz-Carlton"]
locations = ["Downtown", "Riverside", "Beachfront", "City Center", "Old Town", "Financial District"]
room_types = ["Standard", "Deluxe", "Suite", "Premium Suite"]
amenities = ["WiFi", "Breakfast", "Pool", "Gym", "Spa", "Room Service", "Airport Shuttle"]
import json
import random

def generate_hotel():
    hotel = {
        "hotel_name": random.choice(hotel_names),
        "location_near": random.choice(countries),
        "address": {
            # You can add street address generation here
        },
        "standard_amenities": random.sample(amenities, random.randint(3, 5)),
        "rooms": []
    }

    # Generate 2-5 room types per hotel
    for _ in range(random.randint(20, 50)):
        room = {
            "room_id": str(uuid.uuid4()),
            "type": random.choice(room_types),
            "max_occupancy": random.randint(1, 4),
            "description": "A comfortable and spacious room.",  # Add more descriptions if needed
            "price_per_night": random.randint(80, 300),
            "is_available": (random.randint(0, 100) < 80)
        }
        hotel["rooms"].append(room)

    return hotel

if __name__ == '__main__':
    # Clear existing data (optional)
    hotels = []

    # Generate hotels
    for _ in range(500):
        hotel = generate_hotel()
        hotels.append(hotel)

    # Write data to JSON file
    with open("../data/accommodation.json", "w") as json_file:
        json.dump(hotels, json_file, indent=4)