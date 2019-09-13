# Telemetric publisher (NODEMCU3)

## Getting Started

First you need to create a file called `config.h` inside the `./src` directory. The `config.h` file should look something like this:

```cpp
// Update to fit your network configuration
#define STASSID "your-network-ssid"
#define STAPSK "your-network-password"

// Change to your username in the plarform
#define USER "your-username"

// Put to true the sensors you are using
#define MOISTURE false
#define MOISTURE_UUID "9e13dd7f-2480-4b17-95b7-9407f17b5373"
#define HUMIDITY true
#define HUMIDITY_UUID "92931640-a133-4c63-aac6-41ec5ec59635"

// Platform host and port
#define PLATFORM_HOST "http://locahost"
#define PLATFORM_PORT 80

// MQTT broker host and port
#define MQTT_HOST "http://locahost"
#define MQTT_PORT 1883
```

## Roadmap

The nodemcu code is not ready for production. There are a number of features that need to be added in order to make the deployment had easy as possible like python build pipeline for automatic code generation and registration on the platform.

### Current state

In the current state the nodemcu is tasked to do the following steps:

- Connect to Wifi
- Grab uuid and username from EEPROM
- Send request to discovery service and check for enrollment state
- Gathers data from the sensors and send them by polling

If the nodemcu disconnects from the Wifi, wait 3 seconds and reset the mcu.

### Planned production state

The future, full fledge production ready nodemcu should handle the following steps:

- Connect to Wifi
- Grab uuid and username from EEPROM
- Send request to discovery service and check for enrollment state
- If enrolled in the platform start gathering data on the selected sensors and send
- If not enrolled in the platform, send request to enroll
- After that, gather data of sensors and send with timer interrupts

If the nodemcu disconnects from the Wifi, wait 3 seconds and reset the mcu.