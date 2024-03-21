class Payment: 

    def __init__(self, orig_price, final_price, seat_number, flight_id, origin, destination, redemption_loyalty_points,  user_id, user_email):
        self.orig_price = orig_price
        self.final_price = final_price
        self.seat_number = seat_number
        self.flight_id = flight_id
        self.origin = origin 
        self.destination = destination
        self.redemption_loyalty_points = redemption_loyalty_points
        self.user_id = user_id
        self.user_email = user_email

    def json(self):
        return { 
            "orig_price": self.orig_price,
            "final_price": self.final_price, 
            "seat_number": self.seat_number, 
            "flight_id": self.flight_id,
            "origin": self.origin,
            "destination": self.destination,
            "redemption_loyalty_points": self.redemption_loyalty_points,
            "user_id": self.user_id,
            "user_email": self.user_email
        }
    