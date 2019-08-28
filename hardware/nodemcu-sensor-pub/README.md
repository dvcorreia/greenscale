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
#define HUMIDITY true

// Platform host and port
#define PLATFORM_HOST "http://locahost"
#define PLATFORM_PORT 80

// MQTT broker host and port
#define MQTT_HOST "http://locahost"
#define MQTT_PORT 1883
```

## Roadmap

The nodemcu code is not ready for production. There are a number of features that need to be added in order to make the deployment had easy as possible. The backend server already supports all the needed features, so is a matter or adding then.

### Current state

In the current state the nodemcu is tasked to do the following steps:

- Connect to the Wifi
- Send measurements to the server by polling

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
It is good practice to avoid any float numerical operations, it slows down your code.
The final version must avoid using the `String` class since it can cause memory leaks.