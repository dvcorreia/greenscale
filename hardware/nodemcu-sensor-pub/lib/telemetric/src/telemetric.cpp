#include <telemetric.h>

void Telemetric::config(uint8_t pin)
{
    Telemetric::pin = pin;
    randomSeed(analogRead(0));
    //Serial.printf("\nTelemetric measuring on pin %X", pin);
}

uint8_t Telemetric::measure()
{
    Telemetric::sensorValue = 0;
    for (uint8_t i = 0; i <= 10; i++)
    {
        Telemetric::sensorValue += analogRead(Telemetric::pin);
        delay(1);
    }
    Telemetric::sensorValue = Telemetric::sensorValue / 10;

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

    Serial.printf("\nTelemetric measurement: %d", Telemetric::sensorValue);
    return ((uint8_t)Telemetric::sensorValue);
}

uint8_t Telemetric::measureFake(){
    long randNumber = 50 + random(0, 20) - 10;
    uint8_t measure = (uint8_t)randNumber;
    Serial.printf("\nTelemetric measurement: %d", measure);
    return (measure);
}
