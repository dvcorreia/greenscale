#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#include <config.h>

// Function initialization
void connect2Wifi();
void processActuator(byte actuatorPin, const char *value);

#if ACTUATOR1 == true
  char endpoint1[128];
#endif

#if ACTUATOR2 == true
  char endpoint2[128];
#endif

const size_t capacity = JSON_OBJECT_SIZE(2) + 70;

WiFiClient espClient;
PubSubClient client(espClient);
StaticJsonDocument<capacity> doc;

void callback(char *topic, byte *payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (uint i = 0; i < length; i++)
  {
    Serial.print((char)payload[i]);
  }
  Serial.print("\n");

  // Convert to json
  DeserializationError err = deserializeJson(doc, payload);
  if (err)
  {
    Serial.print(F("deserializeJson() failed with code "));
    Serial.println(err.c_str());
  }

  auto value = doc["value"].as<char*>();
  #if ACTUATOR1 == true
  if (strcmp(topic, endpoint1) == 0)
    processActuator(ACTUATOR1PIN, value);
  #endif
  #if ACTUATOR2 == true
  if (strcmp(topic, endpoint2) == 0)
    processActuator(ACTUATOR2PIN, value);
  #endif
}

void reconnect()
{
  // Loop until we're reconnected
  while (!client.connected())
  {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str()))
    {
      Serial.println("connected");
      #if ACTUATOR1 == true
      client.subscribe(endpoint1);
      #endif
      #if ACTUATOR2 == true
      client.subscribe(endpoint2);
      #endif
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup(){
  Serial.begin(115200);

  // Connect to Wifi
  connect2Wifi();

  client.setServer(MQTT_HOST, MQTT_PORT);
  client.setCallback(callback);

#if ACTUATOR1 == true
  pinMode(ACTUATOR1PIN, OUTPUT);
  digitalWrite(ACTUATOR1PIN, LOW);
  sprintf(endpoint1, "actuator/%s", ACTUATOR1_UUID);
#endif
#if ACTUATOR2 == true
  pinMode(ACTUATOR2PIN, OUTPUT);
  digitalWrite(ACTUATOR2PIN, LOW);
  sprintf(endpoint2, "actuator/%s", ACTUATOR2_UUID);
#endif
}

void loop(){
  if (WiFi.status() == WL_CONNECTED){
    if (!client.connected())
      reconnect();
    
    client.loop();
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

void processActuator(byte actuatorPin, const char *value){
  Serial.print("Actuation: ");
  Serial.print(value);
  Serial.print(" on pin ");
  Serial.println(actuatorPin);
  if (strcmp(value, "SWITCH") == 0)
  {
    digitalWrite(actuatorPin, !digitalRead(actuatorPin));
  }
  else if (strcmp(value, "ON") == 0)
  {
    digitalWrite(actuatorPin, HIGH);
  }
  else if (strcmp(value, "OFF") == 0)
  {
    digitalWrite(actuatorPin, LOW);
  }else{
    Serial.print("Value [");
    Serial.print(value);
    Serial.print("] didn't match any actuation action\n");
  }
}