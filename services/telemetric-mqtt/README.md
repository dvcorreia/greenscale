# Moisture MQTT Service

This service provides an __API__ to the moisture database through and __MQTT__ services.

The client was implemented using the [paho-mqtt](https://www.eclipse.org/paho/clients/python/docs/) python library. 

The client subscribes to `sensor/$telemetric/#`, were `$telemetric` is the available telemetrics. This will handle the published messages, verifying them and saving to the correspondent _database_.