class Itinerary: 

    email_list =[]
    potential_flights = []
    potential_accommodation =[]
    total_pax = 0

    def __init__(self, **kwargs):
        self.flight_number = kwargs.get("flight_number")
        self.user_email = kwargs.get("user_list")
        self.departure = kwargs.get("departure")

        self.handle_emails()

    # def json(self):
    #     return { 
    #         "old_flight_data": self.old_flight_data,
    #         "new_flight_data": self.new_flight_data, 
    #         "accommodation": self.accommodation, 
    #         "user_email": self.user_email
    #     }
    
    def update_new_flight_data(self, new_flight_data):
        for flight in new_flight_data:
            self.potential_flights.append({
                "departure": flight["date"],
                "flight_number": flight["flight_number"],
                "availability": flight["avaliable_seats"]
            })
    
    def update_accommodation(self, accommodation):
        for acc in accommodation["rooms"]:
            self.potential_accommodation.append({
                "hotel_name": accommodation["hotelName"],
                "availability": acc["maxOccupancy"]
            })

    def handle_emails(self):
        for email in self.user_email:
            upcoming_bookings = email["upcoming_bookings"]
            for booking in upcoming_bookings:
                if booking["flight_number"] == self.flight_number:
                    booking_pax = booking['pax']
                    self.total_pax += booking_pax
                    break
            self.email_list.append({"email": email["email"],
                                    "pax": booking_pax})
