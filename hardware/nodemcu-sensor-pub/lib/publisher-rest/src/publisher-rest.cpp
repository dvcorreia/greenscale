#include <publisher-rest.h>

void PublisherREST::begin(char *uuid, char *endpoint)
{
    PublisherREST::doc["sensor"] = uuid; // Specify sensor uuid in json document
    Serial.printf("\nPublisher configured with uuid %s", uuid);
    PublisherREST::endpoint = endpoint;  // Specify endpoint
    Serial.printf("\nWill publish on %s\n", endpoint);
}

void PublisherREST::talk(uint8_t measurement)
{
    PublisherREST::doc["value"] = measurement;

    // Produce a minified JSON document
    char output[128];
    serializeJson(PublisherREST::doc, output);

    HTTPClient http;                                    // Send the request
    http.begin(endpoint);                               // Specify request destination
    http.addHeader("Content-Type", "application/json"); // Specify content-type header
    int httpCode = http.POST(output);                   // POST message
    http.end();                                         // Close connection

    // Print return code and published message
    Serial.printf("\nEndpoint: %s", PublisherREST::endpoint);
    Serial.printf("\nCode %d : %s", httpCode, output);
}
