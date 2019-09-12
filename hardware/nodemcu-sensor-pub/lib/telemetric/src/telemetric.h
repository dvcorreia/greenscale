#ifndef TELEMETRIC_H
#define TELEMETRIC_H

#include <Arduino.h>

class Telemetric
{

public:
    void config(uint8_t pin);
    uint8_t pin;
    uint8_t measure();
    uint8_t measureFake();

private:
    uint16_t sensorValue = 0;
    uint16_t maxValue = 1100;
    uint16_t minValue = 480;
};

#endif