from mongoengine import Document, fields, EmbeddedDocument

class Room(EmbeddedDocument):
    room_id = fields.StringField(primary_key=True, required=True)
    type = fields.StringField(required=True)
    max_occupancy = fields.IntField(required=True)
    description = fields.StringField()
    price_per_night = fields.FloatField(required=True)
    is_available = fields.BooleanField(default=True)

class Hotel(Document):
    hotel_name = fields.StringField(required=True)
    location_near = fields.StringField(required=True)
    address = fields.DictField()
    standard_amenities = fields.ListField(fields.StringField())
    rooms = fields.ListField(fields.EmbeddedDocumentField(Room))