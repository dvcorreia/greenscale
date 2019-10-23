#include <discover.h>

void Discover::pulse(char *endpoint, char *uuid, char *description, char *username)
{
    Serial.printf("\nEnroll on %s", endpoint);

    Discover::docDisc["description"] = description;
    Discover::docDisc["uuid"] = uuid;
    Discover::docDisc["username"] = username;
    Serial.printf("\nActuator configured with uuid %s", uuid);

    char output[128];
    serializeJson(Discover::docDisc, output);

    HTTPClient http;                                    // Send the request
    http.begin(endpoint);                               // Specify request destination
    http.addHeader("Content-Type", "application/json"); // Specify content-type header
    int httpCode = http.POST(output);                   // POST message
    http.end();                                         // Close connection

    Serial.printf("\nDiscover code %i on %s", httpCode, uuid);
}