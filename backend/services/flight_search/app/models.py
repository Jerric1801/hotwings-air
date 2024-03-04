class FlightSearch:
    def __init__(self, origin, destination, startdate, enddate, pax, flight_class, trip_type):
        self.origin = origin
        self.destination = destination
        self.startdate = startdate
        self.enddate = enddate
        self.pax = pax
        self.flight_class = flight_class
        self.trip_type = trip_type

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
    
    