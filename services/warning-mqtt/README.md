# Warning MQTT Service

This service handles the monitoring of warnings in the system that were activated through MQTT and saves the history to the events database.
The client was implemented using the [paho-mqtt](https://www.eclipse.org/paho/clients/python/docs/) python library. 

The client subscribes to `warning/#`. This will handle the published messages, verifying them and saving to the correspondent _database_.

The received information will follow the following schema: 

```json
{
    "value": "$message"
}
```

And will be saved as:

```json
{
    "target": "$target_uuid",
    "description": "$description",
    "date": "$data.now"
}
```

