from mongoengine import Document, StringField, ListField, UUIDField, IntField
import uuid

actuatorTypeCatalog = ('onoff')


class Actuator(Document):
    uuid = UUIDField(required=True, default=lambda: str(
        uuid.uuid4()), binary=False, unique=True)
    description = StringField(unique=True, required=False)
    time = IntField(required=False)  # Time in seconds
    ip = StringField(required=False)
