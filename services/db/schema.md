# Schemas

This documents contains the mongodb data schemas

## Management

### User

```json
{
    "id": ObjectIdField(required=True),
    "username": StringField(required=True),
    "password": StringField(required=True),
    "greenhouses": EmbeddedDocumentListField(Greenhouse, required=True)
}
```

### Greenhouse

```json
{
    "id": ObjectIdField(required=True),
    "users": EmbeddedDocumentListField(User, required=True),
    "beds": EmbeddedDocumentListField(Bed, required=True),
    "location": PolygonField()
}
```

### Bed

```json
{
    "id": ObjectIdField(required=True),
    "plant": StringField(),
    "greenhouseId": EmbeddedDocumentField(Greenhouse, required=True),
    "sensors": EmbeddedDocumentListField(Sensor, required=True) 
}
```

### Sensor

```json
{
    "id": ObjectIdField(required=True),
    "type": StringField(),
    "bedId": EmbeddedDocumentField(Bed)

}
```

## Telemetrics

### Moisture

```json
{
    "id": ObjectIdField(required=True),
    "value": DecimalField(required=True),
    "sensorID": EmbeddedDocumentField(Sensor, required=True),
    "greenhouseID": EmbeddedDocumentField(Greenhouse),
    "date": DateTimeField(required=True)
}
```

### Humidity

```json
{
    "id": ObjectIdField(required=True),
    "value": DecimalField(required=True),
    "sensorID": EmbeddedDocumentField(Sensor, required=True),
    "greenhouseID": EmbeddedDocumentField(Greenhouse),
    "date": DateTimeField(required=True)
}
```

