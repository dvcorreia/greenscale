#ifndef DISCOVER_H
#define DISCOVER_H

#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

const size_t capacity = JSON_OBJECT_SIZE(3) + 70;

class Discover
{

public:
    void pulse(char *endpoint, char *uuid, char *description, char *username);

private:
    StaticJsonDocument<capacity> docDisc;
};

#endif