#include <uuid.h>

uint16_t getUUID()
{
    EEPROM.begin(16);
    for (int i = 0; i < 16; i++)
    {
        EEPROM.write(i, i);
    }
    EEPROM.commit();
    delay(1000);
    Serial.println("Getting uuid...");
    uint8_t UUID[16];
    for (int i = 0; i < 16; i++)
    {
        UUID[i] = EEPROM.read(i);
    }

    for (int i = 0; i < 16; i++)
    {
        Serial.println(UUID[i]);
    }

    return (12);
}

void saveUUID(char *uuid)
{
    // Remove '-'
    Serial.println(uuid);
    char *uuidParsed;
    uint8_t j = 0;
    for (uint8_t i = 0; i < strlen; i++)
    {
        if (uuid[i] == '-')
            break;
        uuidParsed[j] = uuid[i];
        j++;
    }
    Serial.println(uuidParsed);
}