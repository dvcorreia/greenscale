#ifndef DISCOVER_H
#define DISCOVER_H

#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

class Discover
{

public:
    boolean pulse(char *endpoint, char *uuid, char *telemetric, char *username);

private:
    char *endpoint;
    char buffer[140];
};

#endif