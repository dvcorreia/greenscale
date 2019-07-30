#include <Arduino.h>
#include <ESP8266WiFi.h>

#define STASSID "your-ssid"
#define STAPSK "your-password"

#define LED_BUILTIN 2

const char *ssid = STASSID;
const char *password = STAPSK;

void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT); // Initialize the LED_BUILTIN pin as an output
}

// the loop function runs over and over again forever
void loop()
{
  Serial.println("Led down");
  digitalWrite(LED_BUILTIN, LOW); // Turn the LED on (Note that LOW is the voltage level
  // but actually the LED is on; this is because
  // it is active low on the ESP-01)
  delay(1000); // Wait for a second

  Serial.println("Led up");
  digitalWrite(LED_BUILTIN, HIGH); // Turn the LED off by making the voltage HIGH
  delay(2000);                     // Wait for two seconds (to demonstrate the active low LED)
}