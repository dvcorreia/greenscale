# Telemetric MQTT Service

This service provides an __API__ to the `db-$telemetric` database through and __MQTT__ services.

The client was implemented using the [paho-mqtt](https://www.eclipse.org/paho/clients/python/docs/) python library. 

The client subscribes to `sensor/$telemetric/#`, were `$telemetric` is the available telemetrics. This will handle the published messages, verifying them and saving to the correspondent _database_.

CMD Line Publishing example:

```bash
mosquitto_pub -h localhost -t sensor/moisture/658c50b6-5c7e-4d77-82b3-d919e276ef28 -m "{\"sensor\": \"658c50b6-5c7e-4d77-82b3-d919e276ef28\",\"value\":50}"
```
