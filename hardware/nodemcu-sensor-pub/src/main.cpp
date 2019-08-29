#include <Arduino.h>
#include <ESP8266WiFi.h>

#include <telemetric.h>
#include <publisher-rest.h>
#include <config.h>

// Verification of configuration file
// Wifi connection configuration
#ifndef STASSID
#define STASSID "your-ssid"
#endif
#ifndef STAPSK
#define STAPSK "your-password"
#endif

// Owner configuration
#ifndef USER
#define USER "username"
#endif

// Platform endpoint
#ifndef PLATFORM_HOST
#define PLATFORM_HOST "http://localhost"
#define PLATFORM_PORT 80
#endif

// MQTT broker endpoint
#ifndef MQTT_HOST
#define MQTT_HOST "http://locahost"
#define MQTT_PORT 1883
#endif

// Connected sensors configuration
#ifndef MOISTURE
#define MOISTURE false
#endif
#ifndef HUMIDITY
#define HUMIDITY false
#endif

// Function initialization
void connect2Wifi();

char *uuid = "33af2283-11c3-40c4-9468-2d2e1e1d4660";
char *endpoint = "http://192.168.1.127/api/v1/moisture";

// Generate the needed classes
Telemetric moisture = Telemetric(A0);
PublisherREST moisturePub = PublisherREST(uuid, endpoint);

void setup()
{
  Serial.begin(115200);
  // Connect to Wifi
  connect2Wifi();
}

void loop()
{
  if (WiFi.status() == WL_CONNECTED)
  {
    uint8_t v = moisture.measure();
    moisturePub.talk(v);
  }
  else
  {
    connect2Wifi();
  }
  delay(10000);
}

// Fuction that connects to the wifi
void connect2Wifi()
{
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