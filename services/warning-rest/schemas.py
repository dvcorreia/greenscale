from mongoengine import Document, StringField, UUIDField, DateTimeField
import mongoengine_goodjson as gj
import uuid
import datetime

actuatorTypeCatalog = ('onoff')


class WarningSchema(gj.Document):
    target = UUIDField(required=True, binary=False)
    description = StringField(required=False)
    date = DateTimeField(default=datetime.datetime.utcnow)
