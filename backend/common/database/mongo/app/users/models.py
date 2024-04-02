from mongoengine import Document, StringField, IntField, ReferenceField, ListField

class Booking(Document):  # Assuming you have a separate Booking model
    # Add relevant fields for your Booking model here
    pass

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    loyalty_points = IntField(default=0)
    past_bookings = ListField(ReferenceField(Booking))
    upcoming_bookings = ListField(ReferenceField(Booking))