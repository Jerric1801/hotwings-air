from mongoengine import Document, StringField, DateTimeField

class ErrorLog(Document):
    logId = StringField(required=True, primary_key=True)
    dateTime = DateTimeField(required=True)
    error_source = StringField(required=True)
    errorDescription = StringField(required=True)