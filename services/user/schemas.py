from mongoengine import Document, EmbeddedDocument, StringField, ListField, ReferenceField, UUIDField, EmbeddedDocumentField
import datetime


class User(Document):
    username = StringField(unique=True, required=True, max_length=50)
    greenhouses = ListField(StringField())


class Sensor(EmbeddedDocument):
    telemetric = StringField(required=True, choices=('moisture', 'humidity'))
    uuid = UUIDField()


class Bed(EmbeddedDocument):
    plant = StringField()
    sensors = ListField(EmbeddedDocumentField('Sensor'))


class Greenhouse(Document):
    location = StringField()
    users = ListField(StringField())
    beds = ListField(EmbeddedDocumentField('Bed'))
