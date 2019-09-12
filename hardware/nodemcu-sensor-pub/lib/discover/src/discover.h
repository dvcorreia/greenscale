#ifndef DISCOVER_H
#define DISCOVER_H

#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

class Discover
{

public:
    void begin(char *endpoint);
    boolean pulse(char *uuid, char *telemetric, char *username);

private:
    char *endpoint;
    char buffer[128];
};

#endif