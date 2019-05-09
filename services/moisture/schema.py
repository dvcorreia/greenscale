from mongoengine import Document, UUIDField, DecimalField, DateTimeField
import datetime


class Moisture(Document):
    sensor = UUIDField(required=True)
    value = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'indexes': [
            # Expires data in 1 day
            {'fields': ['date'], 'expireAfterSeconds': 86400}
        ]
    }
