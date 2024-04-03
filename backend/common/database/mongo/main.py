from app.flight_inventory.seeder import seed_flight_inventory
from app.users.seeder import seed_user
from app.accom_inventory.seeder import seed_accomodations
from app.custom_form.seeder import seed_form

if __name__ == "__main__":
    seed_flight_inventory()
    seed_user()
    seed_accomodations()
    seed_form()
