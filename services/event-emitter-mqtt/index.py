from event import eventClient
from mongoengine import connect
import os

print("Connecting to the database ...")
connect("events", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db-event" + ":" + str(27017) + '/?authSource=admin')
print("Connected to database!")

if __name__ == '__main__':
    channelEvent = ['event/#', 'sensor/#']

    print("Creating MQTT client ...")

    eventClient = eventClient(os.environ['HOST'],
                              int(os.environ['PORT']),
                              channelEvent)

    print("Listening to channels!")
    eventClient.listen(forever=False)
