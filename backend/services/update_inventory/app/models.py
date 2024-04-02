class Inventory: 

    def __init__(self,new_flight_data, old_flight_data, user_id, user_email, accommodation):
        self.new_flight_data = new_flight_data
        self.old_flight_data = old_flight_data
        self.user_id = user_id
        self.user_email = user_email
        self.accommodation = accommodation

    def json(self):
        return { 
            "new_flight_data": self.new_flight_data,
            "old_flight_data": self.old_flight_data,
            "user_id": self.user_id,
            "user_email": self.user_email,
            "accommodation": self.accommodation
        }
    