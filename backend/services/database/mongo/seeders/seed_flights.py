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



def create_flights():

    flights = {}
    flights_list = []
    for location in locations:
        for location2 in locations:
            flight = {}
            if location != location2:
                flight["flight_number"] = str(flight_type + str(random.randint(100, 999)))
                flight["origin"] = location
                flight["destination"] = location2
                flight["model"] = random.choice(list(aircraft_data.keys()))
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
                seat = {"seat_number":seat_number, 
                        "class_type":class_type,
                        "available": True}
                seating_plan.append(seat)

            seat_number_row += 1

    return seating_plan

def seed_flight(no_flights):
    new_flights = []
    for i in range(no_flights):
        with open('flights.json', 'r') as infile:
            flight_dict = json.load(infile)

        flights = flight_dict["flights"]
        flight = flights[random.randint(0, len(flights)-1)]

        flight_number = flight["flight_number"]
        origin = flight["origin"]
        destination = flight["destination"]
        model = flight["model"]

        # Generate departure and arrival times
        departure_time = datetime.now() + timedelta(days=random.randint(1, 14))  # Within the next 2 weeks
        duration = timedelta(hours=random.randint(1, 12)) # 1-12 hour range 
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

async def main():  # Example of how to use it
    flights = seed_flight(200)
    # for flight in flights:
    #     result = await add_flight(flight)
    #     if result and result.status_code == 201:
    #         print("Flight added successfully!")
    #     else:
    #         print("Failed to add flight")

    return flights

if __name__ == "__main__":
     
    flight_data =asyncio.run(main())
    with open('../flight_inventory.json', 'w') as outfile:
        json.dump(flight_data, outfile, indent=4)  # Indent for readability

    # create_flights()
