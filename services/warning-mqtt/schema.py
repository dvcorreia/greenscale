from mongoengine import Document, StringField, UUIDField, DateTimeField
import uuid
import datetime
import mongoengine_goodjson as gj

actuatorTypeCatalog = ('onoff')


class WarningSchema(gj.Document):
    target = UUIDField(required=True, binary=False)
    description = StringField(required=False)
    date = DateTimeField(default=datetime.datetime.utcnow)
