#include <telemetric.h>

// Construstor
Telemetric::Telemetric(uint8_t pin)
{
    Telemetric::pin = pin;
}

// Destructor
Telemetric::~Telemetric()
{
}

uint8_t Telemetric::measure()
{
    Telemetric::sensorValue = 0;
    for (uint8_t i = 0; i <= 10; i++)
    {
        Telemetric::sensorValue += analogRead(Telemetric::pin);
        delay(1);
    }
    Telemetric::sensorValue = Telemetric::sensorValue / 10.0;

    // Adaptative Limits
    if (Telemetric::minValue > Telemetric::sensorValue)
        Telemetric::minValue = Telemetric::sensorValue;
    if (Telemetric::maxValue < Telemetric::sensorValue)
        Telemetric::maxValue = Telemetric::sensorValue;

    // Convert to percentage
    Telemetric::sensorValue = map(Telemetric::sensorValue, Telemetric::minValue, Telemetric::maxValue, 0, 100);

    // Percentage overflow protection
    if (Telemetric::sensorValue < 0)
        Telemetric::sensorValue = 0;
    if (Telemetric::sensorValue > 100)
        Telemetric::sensorValue = 100;

    delay(30);

    return ((uint8_t)Telemetric::sensorValue);
}
