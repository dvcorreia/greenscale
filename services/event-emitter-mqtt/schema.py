from mongoengine import Document, UUIDField, DecimalField, DateTimeField, EmbeddedDocumentListField, EmbeddedDocument, StringField, DecimalField
import datetime
import uuid

eventTypeCatalog = ('actuator', 'warning')
eventVerificationCatalog = ('gt', 'lt', 'eq')


class Event(EmbeddedDocument):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False)
    event_type = StringField(required=True, choices=eventTypeCatalog)
    target = UUIDField(binary=False)
    last_occurred = DateTimeField(default=datetime.datetime.utcnow)
    logic = StringField(required=True, choices=eventVerificationCatalog)
    logic_value = DecimalField(precision=2, rounding='ROUND_HALF_UP')


class Sensor(Document):
    sensor = UUIDField(required=True, binary=False)
    events = EmbeddedDocumentListField('Event')
