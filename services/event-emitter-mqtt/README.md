# Event Emitter MQTT Service

This service handles the management of events and the generation of the same.
The service monitors the `sensor/$telemetric/#` channel. If there is an event registered under a certain sensor, is the necessary conditions are meet the event is generated. The event can be the type of warning on the `warning/$uuid` channel or an actuation on the `actuator/$uuid` channel.

The client was implemented using the [paho-mqtt](https://www.eclipse.org/paho/clients/python/docs/) python library. 

### Add events

Events can be _added_ through MQTT on the channel `actuator/add/$sensor_uuid` passing down json as the following schema:

```json
{
    "event_type": "warning || actuator",
    "target": "target_uuid",
    "logic": "(gt, gte, lt, lte, eq)",
    "logic_value": $decimal_value
}
```
The `logic` entry follow has:

- `gt`: greater than `$logic_value`
- `gte`: greater or equal than `$logic_value`
- `lt`: less than `$logic_value`
- `lte`: less or equal than `$logic_value`
- `eq`: equal to `$logic_value`

The `logic_value` decimal number will only retain 2 decimal places in the _database_.

### Delete

To delete events, it can be done through the channel `actuator/delete/$sensor_uuid` passing down the json data of the event `uuid` to be deleted as:

```json
{
    "uuid": "$event_uuid"
}
```

