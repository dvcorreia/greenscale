import json
from mongoengine import connect
from emitter import Client
import os

# connect("moistures", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
#        ":" + os.environ.get('MONGO_PASSWORD') +
#        "@db-moisture:" + str(27017) + '/?authSource=admin')


if __name__ == '__main__':
    emitter = Client()
    emitter.connect(host="http://localhost", port=8080,
                    secure=True, keepalive=30)
