#include <discover.h>

boolean Discover::pulse(char *endpoint, char *uuid, char *telemetric, char *username)
{
    Discover::endpoint = endpoint; // Specify endpoint
    Serial.printf("\nDiscover on %s", endpoint);
    sprintf(Discover::buffer, "%s?uuid=%s&telemetric=%s&username=%s", Discover::endpoint, uuid, telemetric, username);
    Serial.printf("\nSending dicover request: \n\t%s", Discover::buffer);

    HTTPClient http;                                    // Send the request
    http.begin(Discover::buffer);                                 // Specify request destination
    http.addHeader("Content-Type", "application/json"); // Specify content-type header
    int httpCode = http.GET();                    // POST message
    http.end();                                         // Close connection

    Serial.printf("\nDiscover code %i on %s", httpCode, uuid);

    if(httpCode == HTTP_CODE_OK){   
        return(true);
    }else{
        return(false);
    }
}