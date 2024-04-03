from mongoengine import Document, fields, EmbeddedDocument

class Seat(EmbeddedDocument):
    seat_number = fields.StringField(required=True)
    class_type = fields.StringField(choices=('Economy','Premium Economy', 'Business', 'First'))
    available = fields.BooleanField(default=True) 

class Seating_Plan(Document):
    seats = fields.ListField(fields.EmbeddedDocumentField(Seat))

class Aircraft(EmbeddedDocument):
    model = fields.StringField()
    capacity = fields.IntField()
    seating_plan_id = fields.ObjectIdField() 

class Flight(Document):
    flight_number = fields.StringField(required=True)  
    departure = fields.DateTimeField(required=True)
    arrival = fields.DateTimeField(required=True)
    origin = fields.StringField()
    destination = fields.StringField()
    aircraft = fields.EmbeddedDocumentField(Aircraft) 


class FlightTemplate:
    def __init__(self, **kwargs):
        self.flight_id = kwargs.get("_id")
        self.flight_number = kwargs.get('flight_number')
        self.departure = kwargs.get('departure')
        self.arrival = kwargs.get('arrival')
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')
        self.aircraft = kwargs.get('aircraft')
        self.seating_plan_id = self.aircraft["seating_plan_id"]

class Disrupted:
    def __init__(self, **kwargs):
        self.pax = kwargs.get('pax')
        self.flight_id = kwargs.get('flight_id')