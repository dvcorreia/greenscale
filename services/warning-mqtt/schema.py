from mongoengine import Document, StringField, UUIDField, DateTimeField
import uuid
import datetime

actuatorTypeCatalog = ('onoff')


class WarningSchema(Document):
    target = UUIDField(required=True, binary=False, unique=True)
    description = StringField(unique=True, required=False)
    date = DateTimeField(default=datetime.datetime.utcnow)
