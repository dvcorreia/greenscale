# Event Emitter MQTT Service

This service handles the management of events and the generation of the same.
The service monitors the `sensor/$telemetric/#` channel. If there's an event registered under a certain sensor, is the necessary conditions are meet the event is generated. 

The event can be the type: 

- __warning__ on the `warning/$uuid` channel: `{"message":"$warning_message"}`
- __actuation__ on the `actuator/$uuid` channel: `{"value": "ON" | "OFF" | "SWITCH"}`

The client was implemented using the [paho-mqtt](https://www.eclipse.org/paho/clients/python/docs/) python library. 

### Add events

Events can be _added_ through MQTT on the channel `event/add/$sensor_uuid`.
The basic schema that has to be passed is the following:

```json
{
    "event-type": "warning || actuator",
    "target": "$uuid",  // target uuid
    "logic": "(gt, gte, lt, lte, eq)",
    "logic-value": $decimal_value,
```
The `logic` entry follow has:

- `gt`: greater than `$logic_value`
- `gte`: greater or equal than `$logic_value`
- `lt`: less than `$logic_value`
- `lte`: less or equal than `$logic_value`
- `eq`: equal to `$logic_value`

The `logic_value` decimal number will only retain 2 decimal places in the _database_.

#### Add warning

To add a warning the extra entries on the schema must be added

```json
{
    "warning-message": "String"
}
```

CMD _Warning_ Line test example:

```bash
mosquitto_pub -h localhost -t event/add/658c50b6-5c7e-4d77-82b3-d919e276ef28 -m "{\"event-type\": \"warning\",\"target\":\"e898784b-cd54-4584-b67b-1ae5019b6a51\",\"logic\":\"gte\",\"logic-value\":90,\"warning-message\":\"Water tank almost full\"}"
```

#### Add actuation [fixed]

To add a actuation of type fixed the extra entries on the schema must be added:

```json
{
    "actuation-type": "fixed",
    "actuation-state": "ON" || "OFF"
}
```

CMD _Actuator_ Line test example:

```bash
mosquitto_pub -h localhost -t event/add/658c50b6-5c7e-4d77-82b3-d919e276ef28 -m "{\"event-type\": \"actuator\",\"target\":\"e898784b-cd54-4584-b67b-1ae5019b6a51\",\"logic\":\"lt\",\"logic-value\":10,\"actuation-type\":\"fixed\",\"actuation-state\":\"ON\"}"
```

#### Add actuation [momentary]

To add a actuation of type momentary the extra entries on the schema must be added:

```json
{
    "actuation-type": "fixed",
    "time": $integer_in_seconds
}
```

CMD _Actuator_ Line test example:

```bash
mosquitto_pub -h localhost -t event/add/658c50b6-5c7e-4d77-82b3-d919e276ef28 -m "{\"event-type\": \"actuator\",\"target\":\"e898784b-cd54-4584-b67b-1ae5019b6a51\",\"logic\":\"lt\",\"logic-value\":10,\"actuation-type\":\"momentary\",\"time\":3}"
```

#### Add actuation [switch]

To add a actuation of type switch the extra entries on the schema must be added:

```json
{
    "actuation-type": "switch"
}
```

CMD _Actuator_ Line test example:

```bash
mosquitto_pub -h localhost -t event/add/658c50b6-5c7e-4d77-82b3-d919e276ef28 -m "{\"event-type\": \"actuator\",\"target\":\"e898784b-cd54-4584-b67b-1ae5019b6a51\",\"logic\":\"lt\",\"logic-value\":10,\"actuation-type\":\"switch\"}"
```

### Delete

To delete events, it can be done through the channel `event/delete/$sensor_uuid` passing down the json data of the event `uuid` to be deleted as:

```json
{
    "uuid": "$event_uuid"
}
```

