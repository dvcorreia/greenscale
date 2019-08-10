#ifndef PUBLISHER_REST_H
#define PUBLISHER_REST_H

#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

class PublisherREST
{

public:
    PublisherREST();
    ~PublisherREST();
    void begin();
    void talk(int measurement);
};

#endif