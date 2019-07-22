from mqtt import Client
from mongoengine import connect
import os

print("Connecting to the database ...")
connect("moistures", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db-moisture:" + str(27017) + '/?authSource=admin')
print("Connected to database!")

if __name__ == '__main__':

    channels = ['test/#', 'moisture/']

    print("Creating MQTT client ...")
    client = Client(os.environ['HOST'],
                    int(os.environ['PORT']),
                    channels)

    print("Listening to channels!")
    client.listen(forever=False)
