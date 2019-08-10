#include <publisher-rest.h>

// Construstor
PublisherREST::PublisherREST()
{
}

// Destructor
PublisherREST::~PublisherREST()
{
}

void PublisherREST::begin()
{
    Serial.println("Publishing here");
}

void PublisherREST::talk(int measurement)
{
    Serial.println(measurement);
}
