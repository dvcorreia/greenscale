#include <Arduino.h>
#include <ESP8266WiFi.h>

#include <telemetric.h>
#include <publisher-rest.h>
#include <discover.h>
#include <config.h>



// Verification of configuration file
// And placeholders for the inexistence of such
#ifndef STASSID
  #define STASSID "your-ssid"
  #define STAPSK "your-password"
  #define USER "username"
  #define PLATFORM_HOST "http://localhost"
  #define PLATFORM_PORT 80
  #define MQTT_HOST "http://locahost"
  #define MQTT_PORT 1883
  #define MOISTURE false
  #define MOISTURE_UUID ""
  #define HUMIDITY false
  #define HUMIDITY_UUID ""
  #define DEBUGLEVEL 3
#endif

// Function initialization
void connect2Wifi();

char endpoint[80];
uint8_t v = 0;

// Gerate discover class
Discover discover = Discover();

// Generate the needed classes
#if MOISTURE == true
Telemetric moisture = Telemetric();
PublisherREST moisturePub = PublisherREST();
#endif

void setup(){
  Serial.begin(115200);

  // Connect to Wifi
  connect2Wifi();

  //Config discover
  sprintf(endpoint, "http://%s:%i/api/v1/discover/enroll", PLATFORM_HOST, PLATFORM_PORT);
  discover.begin(endpoint);

  #if MOISTURE == true
  // Send discover
  discover.pulse(MOISTURE_UUID, "moisture", USER);
  // Initialize moisture classes
  moisture.config(A0);
  sprintf(endpoint, "http://%s:%i/api/v1/moisture", PLATFORM_HOST, PLATFORM_PORT);
  moisturePub.begin(MOISTURE_UUID, endpoint);
  #endif
}

void loop(){
  if (WiFi.status() == WL_CONNECTED){
    #if MOISTURE == true
    v = moisture.measureFake();
    moisturePub.talk(v);
    #endif
  }else{
    connect2Wifi();
  }
  delay(3000);
}

// Fuction that connects to the wifi
void connect2Wifi(){
  // Connect to the Wifi network
  Serial.print("\nConnecting to ");
  Serial.println(STASSID);

  WiFi.mode(WIFI_STA); // Set the ESP8266 to be a WiFi-client
  WiFi.begin(STASSID, STAPSK);

  // Waiting for connectiong
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}