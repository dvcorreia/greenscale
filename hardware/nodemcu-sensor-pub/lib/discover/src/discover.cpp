#include <discover.h>

void Discover::begin(char *endpoint){
    Discover::endpoint = endpoint; // Specify endpoint
    Serial.printf("\nDiscover on %s", endpoint);
}

boolean Discover::pulse(char *uuid, char *telemetric, char *username){
    Serial.printf("\nSending dicover request for %s", uuid);

    sprintf(Discover::buffer, "%s?uuid=%s&telemetric=%s&username=%s", Discover::endpoint, uuid, telemetric, username);
    
    HTTPClient http;                                    // Send the request
    http.begin(Discover::buffer);                                 // Specify request destination
    http.addHeader("Content-Type", "application/json"); // Specify content-type header
    int httpCode = http.GET();                    // POST message
    http.end();                                         // Close connection

    if(httpCode == HTTP_CODE_OK){
        return(true);
    }else{
        return(false);
    }
}