from mongoengine import *
import datetime


class Moisture(Document):
    sensor = UUIDField()
    value = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'moisture-db'}
