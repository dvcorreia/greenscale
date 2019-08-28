#include <publisher-rest.h>

// Construstor
PublisherREST::PublisherREST(char *uuid, char *endpoint)
{
    PublisherREST::doc["uuid"] = uuid;  // Specify uuid in json document
    PublisherREST::endpoint = endpoint; // Specify endpoint
}

// Destructor
PublisherREST::~PublisherREST()
{
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
    Serial.print("Code ");
    Serial.print(httpCode);
    Serial.print(" : ");
    Serial.println(output);
}
