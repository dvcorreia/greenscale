#ifndef PUBLISHER_REST_H
#define PUBLISHER_REST_H

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

const size_t capacity = JSON_OBJECT_SIZE(2) + 70;

class PublisherREST
{

public:
    void begin(char *uuid, char *endpoint);
    void talk(uint8_t measurement);

private:
    StaticJsonDocument<capacity> doc;
    char *endpoint;
};

#endif