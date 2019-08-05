# Testing

Has the platform started to grow in complexity there was a need to optimize testing and generation of data. With this the tools bellow were created.

## MQTT-bot

### Overview

The `mqtt-bot` is a python3 tool created to simulate users in the platform. 

It creates a fixed number of users that will each one generate between 1 and 10 greenhouses, each greenhouse generating between 1 and 10 beds, and each bed containing 2 to 5 sensors. Each sensor will publish every 5 to 30 seconds through MQTT messages. This allows to simulate a real world scenario.

The tool also have a flag that can be activated, `-u --unicity`, that on spawns only one user, with only one greenhouse, one bed and one sensor. The sensor will publish faster, 1 to 5 times a second. This is used to make a narrow test.

### Usability

To run the tool make sure that the platform is running and have a mqtt bot configuration file ready _(you can use the default one `mqtt_conf.json`)_.

```bash
python bot.py -e <http://uri:port> -b <numberbots> -m mqtt_conf.json
```

The tool option are:

        -h ; --help       : Help
        -u ; --unicity    : Runs only one bot with one greenhouse, a bed, a plant and sensor
        -e ; --endpoint   : REST Host and port (default: http://localhost:80)
        -t ; --telemetric : In case unicity is True lets you chose the sensor telemetric
        -b ; --bots       : Number of bots (default: 1)
        -m ; --mqtt       : MQTT configuration file

## REST-bot

### Overview

The `rest-bot` is a python3 tool created to simulate users in the platform. 

It creates a fixed number of users that will each one generate between 1 and 10 greenhouses, each greenhouse generating between 1 and 10 beds, and each bed containing 2 to 5 sensors. Each sensor will publish every 5 to 30 seconds through REST requests. This allows to simulate a real world scenario.

The tool also have a flag that can be activated, `-u --unicity`, that on spawns only one user, with only one greenhouse, one bed and one sensor. The sensor will publish faster, 1 to 5 times a second. This is used to make a narrow test.

### Usability

To run the tool make sure that the platform is running.

```bash
python bot.py -e <http://uri:port> -b <numberbots>
```

The tool option are:

        -h ; --help       : Help
        -u ; --unicity    : Runs only one bot with one greenhouse, a bed, a plant and sensor
        -e ; --endpoint   : REST Host and port (default: http://localhost:80)
        -t ; --telemetric : In case unicity is True lets you chose the sensor telemetric
        -b ; --bots       : Number of bots (default: 1)