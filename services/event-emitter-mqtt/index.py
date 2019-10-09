#from telemetric_probe import telemetricProbeClient
from event import eventClient
from mongoengine import connect
import os

print("Connecting to the database ...")
connect("events", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db-event" + ":" + str(27017) + '/?authSource=admin')
print("Connected to database!")

if __name__ == '__main__':

    channelSensor = ['sensor/#']
    channelEvent = ['event/#']

    print("Creating MQTT client ...")
    # telemetricProbleClient = telemetricProbeClient(os.environ['HOST'],
    #                                               int(os.environ['PORT']),
    #                                               channelSensor)
    eventClient = eventClient(os.environ['HOST'],
                              int(os.environ['PORT']),
                              channelEvent)

    print("Listening to channels!")
    # telemetricProbleClient.listen(forever=True)
    eventClient.listen(forever=False)
