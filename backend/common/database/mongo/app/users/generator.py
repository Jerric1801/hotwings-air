# public class User {
#     @Id
#     private String userid;
#     private String name;
#     private String email;
#     private String password;
#     private int loyalty_points;
#     private Object past_bookings;
#     private Object upcoming_bookings;
# }

import json
import random
import string
from faker import Faker

fake = Faker()  # Initialize Faker for realistic data

def generate_user():
    """Generates a single user dictionary."""
    return {
        "userid": ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(),  # Consider using hashing for real applications
        "loyalty_points": random.randint(0, 1000),
        "past_bookings": [],  # Placeholder, adjust based on your booking structure
        "upcoming_bookings": []  # Placeholder, adjust based on your booking structure
    }

def generate_users(num_users):
    """Generates a list of user dictionaries."""
    return [generate_user() for _ in range(num_users)]

# Generate sample data
users = generate_users(100)  # Generate 100 users

# Save to JSON file
with open("seed_data.json", "w") as f:
    json.dump(users, f, indent=4)