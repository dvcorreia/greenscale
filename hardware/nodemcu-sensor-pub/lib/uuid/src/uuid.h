#ifndef UUID_H
#define UUID_H

#include <ESP8266WiFi.h>
#include <EEPROM.h>

uint16_t getUUID();
void saveUUID(char *uuid);

#endif