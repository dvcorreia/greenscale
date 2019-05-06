from mongoengine import Document, EmbeddedDocument, StringField, ListField, ReferenceField, EmbeddedDocumentField, UUIDField
import datetime
import uuid

sensorCatalog = ('moisture',
                 'humidity',
                 'light')


class Sensor(EmbeddedDocument):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False)
    telemetric = StringField(required=True, choices=sensorCatalog)
    hardwareId = StringField(default='Dunno')


class Bed(EmbeddedDocument):
    uuid = UUIDField(required=True, default=lambda: str(uuid.uuid4()))
    plant = StringField()
    sensors = ListField(EmbeddedDocumentField('Sensor'))


class Greenhouse(Document):
    location = StringField()
    beds = ListField(EmbeddedDocumentField('Bed'))
