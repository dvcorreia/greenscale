from warning_probe import warningProbeClient
from mongoengine import connect
import os

print("Connecting to the database ...")
connect("warning", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db-event" + ":" + str(27017) + '/?authSource=admin')
print("Connected to database!")

if __name__ == '__main__':
    channelEvent = ['warning/#']

    print("Creating MQTT client ...")

    warningProbeClient = warningProbeClient(os.environ['HOST'],
                                            int(os.environ['PORT']),
                                            channelEvent)

    print("Listening to channels!")
    warningProbeClient.listen(forever=False)
