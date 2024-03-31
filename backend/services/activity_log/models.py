from mongoengine import Document, StringField, DateTimeField

class ActivityLog(Document):
    """
    Model to represent activity logs.
    """

    service = StringField(required=True)
    timestamp = DateTimeField(required=True)
    action = StringField(required=True)

    meta = {'collection': 'activity_logs'}  # Specify the collection name in the database
