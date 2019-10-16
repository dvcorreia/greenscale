from mongoengine import Document, UUIDField, DecimalField, DateTimeField, EmbeddedDocumentListField, EmbeddedDocument, StringField, DecimalField, IntField
import datetime
import uuid

eventTypeCatalog = ('actuator', 'warning')
eventVerificationCatalog = ('gt', 'gte', 'lt', 'lte', 'eq')
eventActuationType = ('momentary', 'switch')


class Event(EmbeddedDocument):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False)
    event_type = StringField(required=True, choices=eventTypeCatalog)
    target = UUIDField(binary=False)
    last_occurred = DateTimeField(default=datetime.datetime.utcnow)
    logic = StringField(required=True, choices=eventVerificationCatalog)
    logic_value = DecimalField(precision=2, rounding='ROUND_HALF_UP')
    warning_message = StringField(required=False)
    actuation_type = StringField(required=False, choices=eventActuationType)
    time = IntField(required=False)


class Sensor(Document):
    sensor = UUIDField(required=True, binary=False)
    events = EmbeddedDocumentListField('Event')
