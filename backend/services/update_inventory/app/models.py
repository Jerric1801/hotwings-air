class Inventory: 
    def __init__(self, **kwargs):
        self.new_flight_data = kwargs.get("new_flight_data")
        self.old_flight_data = kwargs.get("old_flight_data")
        self.user_email = kwargs.get("user_email")
        self.accommodation = kwargs.get("accommodation")
        self.pax = int(kwargs.get("pax"))


class NewFlight:
    def __init__(self, **kwargs) :
        self.origin =  kwargs.get("origin")
        self.destination = kwargs.get("destination")
        self.departure = kwargs.get("departure") 
        self.flight_number = kwargs.get("flight_number")
        self.seats = kwargs.get('seats')
