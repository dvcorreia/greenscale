from mongoengine import Document, StringField, UUIDField
import datetime
import uuid

sensorCatalog = ('moisture',
                 'humidity',
                 'light')


class Sensor(Document):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False)
    telemetric = StringField(required=True, choices=sensorCatalog)
