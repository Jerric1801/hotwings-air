from mongoengine import Document, StringField, DateTimeField

class ErrorLog(Document):
    logId = StringField(required=True, primary_key=True)
    dateTime = DateTimeField(required=True)
    code = StringField(required=True)
    data = StringField(required=True)
    message = StringField(required=True)
    