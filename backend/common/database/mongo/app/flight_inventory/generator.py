import random 
from datetime import datetime, timedelta
import requests
import json
import asyncio

flight_type = "HW"
locations = ["Singapore", "Tokyo", "Bangkok", "Sydney", "Hong Kong", "London", "New York", "Kuala Lumpur", "Jakarta", "Manila", "Dubai", "Paris", "Los Angeles"]
models = []
aircraft_data = {
    "Boeing 737": {
        "capacity_range": 120,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Boeing_737-800_United_Airlines.jpg/220px-Boeing_737-800_United_Airlines.jpg"
    },
    "Airbus A320": {
        "capacity_range": 150,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Airbus_A320_neo_Iberia_livery.jpg/220px-Airbus_A320_neo_Iberia_livery.jpg"
    },
    "Boeing 777": {
        "capacity_range": 300,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Boeing_777-300ER_Emirates.jpg/220px-Boeing_777-300ER_Emirates.jpg"
    },
    "Airbus A350": {
        "capacity_range": 300,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Airbus_A350-900_Qatar_Airways.jpg/220px-Airbus_A350-900_Qatar_Airways.jpg"
    },
    "Boeing 787": {
        "capacity_range": 240,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/All_Nippon_Airways_Boeing_787-8_Dreamliner.jpg/220px-All_Nippon_Airways_Boeing_787-8_Dreamliner.jpg"
    },
    "Airbus A380": {
        "capacity_range": 500,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Emirates_A380-800_at_Dubai_International_Airport.jpg/220px-Emirates_A380-800_at_Dubai_International_Airport.jpg"
    }
}

regions = {
    "Southeast Asia": ["Singapore", "Bangkok", "Kuala Lumpur", "Jakarta", "Manila"],
    "East Asia": ["Tokyo", "Hong Kong"],
    "Oceania": ["Sydney"],
    "Middle East": ["Dubai"],
    "Europe": ["London", "Paris"],
    "North America": ["New York", "Los Angeles"]
}
adjacent_regions = {
    "Southeast Asia": ["East Asia", "Oceania", "Middle East"],
    "East Asia": ["Southeast Asia", "Oceania"],
    "Oceania": ["Southeast Asia", "East Asia", "North America"],
    "Middle East": ["Southeast Asia", "Europe"],
    "Europe": ["Middle East", "North America"],
    "North America": ["Oceania", "Europe"] 
}
distance_tiers = {
    "intraregional": (500,  2000),  # Within the same region
    "interregional_close": (2000, 5000),  # Between neighboring regions
    "interregional_far":  (5000, 9000),  # Between distant regions 
}
seat_classes = {"First":2.5, "Business":1.75, "Premium Economy":1.23, "Economy": 1}
locations = ["Singapore", "Tokyo", "Bangkok", "Sydney", "Hong Kong", "London", "New York", "Kuala Lumpur", "Jakarta", "Manila", "Dubai", "Paris", "Los Angeles"]
tiers = {
    "short": (500, 2000), 
    "medium": (2000, 5000),
    "long": (5000, 10000)
}

def are_regions_adjacent(region1, region2):
    return region2 in adjacent_regions[region1] 

def estimate_distance(origin, destination):
    origin_region = None
    destination_region = None

    # Find the regions of the origin and destination
    for region_name, cities in regions.items():
        if origin in cities:
            origin_region = region_name
        if destination in cities:
            destination_region = region_name

    # Distance estimation
    if origin_region == destination_region:
        distance_tier = "intraregional"
    elif are_regions_adjacent(origin_region, destination_region):  # You'll need to define this
        distance_tier = "interregional_close"
    else:
        distance_tier = "interregional_far"

    # Pick a random distance within the chosen tier (adjust ranges as needed)
    distance = random.randint(*distance_tiers[distance_tier])
    return distance



def create_flights():
    taken = []
    flights = {}
    flights_list = []
    for location in locations:
        for location2 in locations:
            flight = {}
            if location != location2:
                flight_num = ""

                while flight_num in taken or flight_num == "":
                    flight_num = str(flight_type + str(random.randint(100, 999)))
                
                flight["flight_number"] = flight_num

                flight["origin"] = location
                flight["destination"] = location2
                flight["model"] = random.choice(list(aircraft_data.keys()))
                taken.append(flight_num)
                flights_list.append(flight)

    flights["flights"] = flights_list
    with open('flights.json', 'w') as outfile:
        json.dump(flights, outfile, indent=4)  # Indent for readability

    
def generate_seating_plan(aircraft_model, capacity):
    typical_proportions = {
        "small": {"Business": 0.2, "Economy": 0.8},  # Smaller planes, more business focus
        "medium": {"Business": 0.15, "Premium Economy": 0.1, "Economy": 0.75}, 
        "large": {"First": 0.05, "Business": 0.15, "Premium Economy": 0.15, "Economy": 0.65}
    }

    # Select proportions based on aircraft size (you'll need to map this yourself)
    if aircraft_model in ["Boeing 737", "Airbus A320"]:
        size_category = "small"
        seats_per_row = 6
    elif aircraft_model in ["Boeing 777", "Airbus A350"]:
        size_category = "medium"
        seats_per_row = 9
    else:
        size_category = "large"  # Or a default if you don't recognize the model
        seats_per_row = 9

    proportions = typical_proportions[size_category]

    total_capacity = capacity 
    rows_per_class = {}
    for class_type, proportion in proportions.items():
        rows_per_class[class_type] = round(total_capacity * proportion / seats_per_row)  

    for class_type in rows_per_class:
        rows_per_class[class_type] += random.randint(-2, 2)  # Tweak the range as needed

    seating_config = {class_type: (num_rows, seats_per_row)
                      for class_type, num_rows in rows_per_class.items()}

    seating_plan = []
    seat_number_row = 1  

    for class_type, (num_rows, seats_per_row) in seating_config.items():
        seat_letters = "ABCDEFGHIJK"[:seats_per_row]

        for row in range(1, num_rows + 1):
            for letter in seat_letters:
                seat_number = f"{seat_number_row}{letter}"
                available = random.random() < 0.70 
                seat = {"seat_number":seat_number, 
                        "class_type":class_type,
                        "available": available}
                seating_plan.append(seat)

            seat_number_row += 1

    return seating_plan

def seed_flight(no_flights):
    new_flights = []
    with open('flights.json', 'r') as infile:
        flight_dict = json.load(infile)

    flights = flight_dict["flights"]

    for i in range(no_flights):
        flight = flights[random.randint(0, len(flights)-1)]

        flight_number = flight["flight_number"]
        origin = flight["origin"]
        destination = flight["destination"]
        model = flight["model"]

        # Generate departure and arrival times
        departure_time = datetime.now() + timedelta(days=random.randint(1, 40))  # Within the next 40 days
        distance = estimate_distance(origin, destination)
        if tiers["short"][0] <= distance <= tiers["short"][1]:
            duration = timedelta(hours=random.randint(1, 3)) + timedelta(minutes=random.randint(1, 60)) 
        elif tiers["medium"][0] <= distance <= tiers["medium"][1]:
            duration = timedelta(hours=random.randint(3, 7)) + timedelta(minutes=random.randint(1, 60)) 
        else:  # long
            duration = timedelta(hours=random.randint(7, 13)) + timedelta(minutes=random.randint(1, 60)) 
        arrival_time = departure_time + duration

        # Select an aircraft model
        # model = random.choice(list(aircraft_data.keys()))
        capacity = aircraft_data[model]["capacity_range"]

        seating_plan = generate_seating_plan(model, capacity)

        flight_data = {
            "flight_number": flight_number, 
            "departure": departure_time.isoformat(),
            "arrival": arrival_time.isoformat(),
            "origin": origin,
            "destination": destination,
            "aircraft": {
                "model": model,
                "capacity": capacity, 
                "seating_plan": {
                    "seats": seating_plan
                }
            }
        }
        new_flights.append(flight_data)

    return new_flights

async def add_flight(flight_data):
    try:
        response = requests.post("http://localhost:5000/flight/new",
                                 headers={"Content-Type": "application/json"}, 
                                 json = flight_data)
        return response  # Return the response object
    except requests.exceptions.RequestException as e:
        print(f"Error adding flight: {e}")
        return None  # Or handle the error differently

async def main(reps = 1000):  # Example of how to use it
    flights = seed_flight(reps)
    # for flight in flights:
    #     result = await add_flight(flight)
    #     if result and result.status_code == 201:
    #         print("Flight added successfully!")
    #     else:
    #         print("Failed to add flight")

    return flights

if __name__ == "__main__":
    reps = 1000
    flight_data = asyncio.run(main(reps))
    with open('../data/flight_inventory.json', 'w') as outfile:
        json.dump(flight_data, outfile, indent=4)  # Indent for readability

    # create_flights()
