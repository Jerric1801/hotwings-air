class Itinerary: 

    def __init__(self, **kwargs):
        self.flight_number = kwargs("flight_number")
        self.user_email = kwargs("user_list")
        self.flight_id = kwargs("flight_id")
        self.date = kwargs("date")

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
