from mongoengine import Document, StringField, ListField


class User(Document):
    username = StringField(unique=True, required=True, max_length=50)
    greenhouses = ListField(StringField())
