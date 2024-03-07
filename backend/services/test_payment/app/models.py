

# from mongoengine import Document, fields, EmbeddedDocument

# class Seat(EmbeddedDocument):
#     seat_number = fields.StringField(required=True)
#     class_type = fields.StringField(choices=('Economy','Premium Economy', 'Business', 'First'))
#     available = fields.BooleanField(default=True) 

# class Seating_Plan(Document):
#     seats = fields.ListField(fields.EmbeddedDocumentField(Seat))

# class Aircraft(EmbeddedDocument):
#     model = fields.StringField()
#     capacity = fields.IntField()
#     seating_plan_id = fields.ObjectIdField() 

# class Flight(Document):
#     flight_number = fields.StringField(required=True, primary_key=True)  
#     departure = fields.DateTimeField(required=True)
#     arrival = fields.DateTimeField(required=True)
#     origin = fields.StringField()
#     destination = fields.StringField()
#     aircraft = fields.EmbeddedDocumentField(Aircraft) 

