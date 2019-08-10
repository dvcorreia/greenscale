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