from mongoengine import Document, fields

class Aircraft(EmbeddedDocument):
    model = fields.StringField()
    capacity = fields.IntField()

class Flight(Document):
    flight_number = fields.StringField(required=True, primary_key=True)  
    departure = fields.DateTimeField(required=True)
    arrival = fields.DateTimeField(required=True)
    origin = fields.StringField()
    destination = fields.StringField()
    aircraft = fields.EmbeddedDocumentField(Aircraft) 