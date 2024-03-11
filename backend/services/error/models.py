from mongoengine import Document, StringField, DateTimeField

class ErrorLog(Document):
    logId = StringField(required=True, primary_key=True)
    dateTime = DateTimeField(required=True)
    flightId = StringField(required=True)
    email = StringField(required=True)
    errorDescription = StringField(required=True)