#include <Arduino.h>
#include <ESP8266WiFi.h>

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

#define LED_BUILTIN 2

// Function initialization
void connect2Wifi();

PublisherREST pub;

void setup()
{
  Serial.begin(115200);
  // Connect to Wifi
  connect2Wifi();
  // Grab uuid and username from EEPROM
  // Send request to discovery service and check for state
  // If enrolled in the platform start gathering data on the selected sensors and send
  // If not enrolled in the platform, send request to enroll
  // After that gathering data on the selected sensors and send
}

void loop()
{
  pub.talk(12);
}

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