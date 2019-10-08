from mongoengine import Document, UUIDField, DecimalField, DateTimeField, EmbeddedDocumentListField, EmbeddedDocument, StringField
import datetime
import uuid

eventTypeCatalog = ('actuator', 'warning')


class Event(EmbeddedDocument):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False)
    event_type = StringField(required=True, choices=eventTypeCatalog)
    target = UUIDField(binary=False)
    last_occurred = DateTimeField(default=datetime.datetime.utcnow)


class Sensor(Document):
    sensor = UUIDField(required=True, binary=False)
    events = EmbeddedDocumentListField('Event')
