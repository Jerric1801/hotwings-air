class Payment: 

    def __init__(self, **kwargs):
        self.base_price = kwargs.get('base_price')
        self.depart_arrival_time = kwargs.get('depart_arrival_time')
        self.depart_departure_time = kwargs.get('depart_departure_time')
        self.depart_destination = kwargs.get('depart_destination')
        self.depart_id = kwargs.get('depart_id')
        self.depart_origin = kwargs.get('depart_origin')
        self.depart_seat_id = kwargs.get('depart_seat_id')
        self.depart_seats = kwargs.get('depart_seats')
        self.loyalty_points = kwargs.get('loyalty_points')
        self.other_passengers = kwargs.get('other_passengers')
        self.return_arrival_time = kwargs.get('return_arrival_time')
        self.return_departure_time = kwargs.get('return_departure_time')
        self.return_destination = kwargs.get('return_destination')
        self.return_id = kwargs.get('return_id')
        self.return_origin = kwargs.get('return_origin')
        self.return_seat_id = kwargs.get('return_seat_id')
        self.return_seats = kwargs.get('return_seats')
        self.total_price = kwargs.get('total_price')
        self.user_email = kwargs.get('user_email')
        self.user_first = kwargs.get('user_first')
        self.user_gender = kwargs.get('user_gender')
        self.user_last = kwargs.get('user_last')
        self.user_phone = kwargs.get('user_phone')
        self.flight_number = kwargs.get('flight_number')

    def get_flight_inventory(self):
        #check if return flight exists
        if self.return_seat_id:
            return {
                "depart_id":self.depart_seat_id,
                "depart_seats":self.depart_seats, 
                "return_id": self.return_seat_id, 
                "return_seats": self.return_seats
                }
        else:
            return {
                "depart":[self.depart_seat_id, self.depart_seats], 
                }


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
    