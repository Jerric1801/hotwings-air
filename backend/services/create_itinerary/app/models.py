class Itinerary: 

    def __init__(self, old_flight_data=None, new_flight_data=None, accommodation=None, user_email=None):
        self.old_flight_data = old_flight_data
        self.new_flight_data = new_flight_data
        self.accommodation = accommodation
        self.user_email = user_email

    def json(self):
        return { 
            "old_flight_data": self.old_flight_data,
            "new_flight_data": self.new_flight_data, 
            "accommodation": self.accommodation, 
            "user_email": self.user_email
        }
    
    def update_new_flight_data(self, new_flight_data):
        self.new_flight_data = new_flight_data
    
    def update_accommodation(self, accommodation):
        self.accommodation = accommodation
