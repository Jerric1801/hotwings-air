from app.flight_inventory.seeder import seed_flight_inventory
from app.users.seeder import seed_user

if __name__ == "__main__":
    seed_flight_inventory()
    seed_user()
