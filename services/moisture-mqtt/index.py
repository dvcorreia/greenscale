import json
from mongoengine import connect
import os

connect("moistures", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db-moisture:" + str(27017) + '/?authSource=admin')

if __name__ == '__main__':
    print('Hello moistures MQTT!')
