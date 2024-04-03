class Inventory: 

    def __init__(self, **kwargs):
        self.new_flight_data = kwargs.get("new_flight_data")
        self.old_flight_data = kwargs.get("old_flight_data")
        self.user_email = kwargs.get("user_email")
        self.accommodation = kwargs.get("accommodation")
        self.pax = int(kwargs.get("pax"))
