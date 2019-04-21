from mongoengine import *
import datetime


class User(Document):
    username = StringField(required=True, max_length=50)
    greenhouses = ListField(ReferenceField(Greenhouse))


class Greenhouse(Document):
    location = StringField()
    users = ListField(required=True, ReferenceField(User))
    beds = ListField(EmbeddedDocumentField(Bed))


class Bed(EmbeddedDocument):
    plant = StringField()
    sensors = ListField(EmbeddedDocumentField(Sensor))


SENSORS = ('moisture', 'humidity')


class Sensor(EmbeddedDocument):
    telemetric = StringField(required=True, choices=SIZE)
    uuid = UUIDField()


class Moisture(Document):
    sensor = UUIDField()
    value = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)


class Humidity(Document):
    sensor = UUIDField()
    value = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)
