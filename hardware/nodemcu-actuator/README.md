# Actuator Subscriber (NODEMCU3)

## Getting Started

First you need to create a file called `config.h` inside the `./src` directory. The `config.h` file should look something like this:

```cpp
// Update to fit your network configuration
#define STASSID "your-network-ssid"
#define STAPSK "your-network-password"

// Change to your username in the plarform
#define USER "your-username"

// Put to true the actuator you are using
#define ACTUATOR1 true
#define ACTUATOR1_UUID "9e13dd7f-2480-4b17-95b7-9407f17b5373"
#define ACTUATOR1PIN D0
#define ACTUATOR2 true
#define ACTUATOR2_UUID "9e13dd7f-2480-4b17-95b7-9407f17b5374"
#define ACTUATOR2PIN D1

// Platform host and port
#define PLATFORM_HOST "http://locahost"
#define PLATFORM_PORT 80

// MQTT broker host and port
#define MQTT_HOST "http://locahost"
#define MQTT_PORT 1883
```


## Description

This code enables the platform to actuate on actuators connected to this microcontroller.
It subscribes to `actuator/$ACTUATOR#_UUID` defined in the `config.h` file and puts to `HIGH` or `LOW` the correspondent `ACTUATOR#PIN` depending on the message received.