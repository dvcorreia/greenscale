from mongoengine import Document, EmbeddedDocument, StringField, ListField, ReferenceField, EmbeddedDocumentField
import datetime


class Sensor(EmbeddedDocument):
    telemetric = StringField(required=True, choices=('moisture', 'humidity'))
    hardwareId = StringField()


class Bed(EmbeddedDocument):
    plant = StringField()
    sensors = ListField(EmbeddedDocumentField('Sensor'))


class Greenhouse(Document):
    location = StringField()
    beds = ListField(EmbeddedDocumentField('Bed'))
