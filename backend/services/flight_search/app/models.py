class FlightSearch:
    def __init__(self, **kwargs):
        self.origin = kwargs.get("origin")
        self.destination = kwargs.get("destination")
        self.startdate = kwargs.get("departureDate")
        self.enddate = kwargs.get("returnDate")
        self.pax = kwargs.get("pax")
        self.flight_class = kwargs.get("seatClass")
        self.trip_type = kwargs.get("tripType")

    def get_search_params(self, return_flight = False):
        if return_flight:
            search_parameters = {
                "origin": self.destination,
                "destination": self.origin,
                'date': self.enddate,
                "pax": self.pax,
                "class": self.flight_class ,
            }
        else:
            search_parameters = {
                "origin": self.origin,
                "destination": self.destination,
                'date': self.startdate,
                "pax": self.pax,
                "class": self.flight_class ,
            }

        return search_parameters
    
    