class Payment: 

    def __init__(self, total_price, seat_number, flight_id, loyalty_points,  user_id, user_email):
        self.total_price = total_price
        self.seat_number = seat_number
        self.flight_id = flight_id
        self.loyalty_points = loyalty_points
        self.user_id = user_id
        self.user_email = user_email

    def json(self):
        return { 
            "total_price": self.total_price, 
            "seat_number": self.seat_number, 
            "flight_id": self.flight_id,
            "loyalty_points": self.loyalty_points,
            "user_id": self.user_id,
            "user_email": self.user_email
        }
    