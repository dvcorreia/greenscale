import requests
import json
import random
import numpy as np
import threading
from emitter import Client
import os

sensors = [
    'moisture',
    'humidity'
]


class Sensor(object):
    def __init__(self, greenhouseId, bedUuid, unicity=False):
        self.greenhouseId = greenhouseId
        self.bedUuid = bedUuid

        if unicity:
            self.telemetric = os.environ['TELEMETRIC']
        else:
            self.telemetric = random.choice(sensors)

        self.unicity = unicity

        # Create Sensor
        try:
            r = requests.post(os.environ['URI'] + "/api/v1/greenhouse/" + self.greenhouseId + "/bed/" + self.bedUuid + "/sensor",
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"telemetric": self.telemetric})
        except Exception as e:
            print(e)

        data = json.loads(r.text)
        sensor = data['data']['greenhouse']['beds']['sensor']

        self.uuid = sensor['uuid']
        self.hardwareId = sensor['hardwareId']

        self.broker = Client()
        self.broker.on_connect = lambda: print("Connected to the broker")
        self.broker.connect(os.environ['HOST'], int(
            os.environ['PORT']), False, 30)

    def talk(self):
        # Post dummy data
        try:
            self.broker.publish(os.environ['CHANNEL_KEY'],
                                os.environ['CHANNEL'] + self.uuid,
                                json.dumps({
                                    "sensor": self.uuid,
                                    "value": str(np.random.normal(10, 0.7))
                                }),
                                {Client.with_at_least_once(), Client.with_ttl(60), Client.without_echo()})
        except Exception as e:
            print(e)

        print("Pub sensor" + self.uuid + "data")

        if self.unicity:
            threading.Timer(random.randint(1, 5), self.talk).start()
        else:
            threading.Timer(random.randint(5, 30), self.talk).start()
