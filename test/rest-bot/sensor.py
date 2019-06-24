import requests
import json
import os
import random
import numpy as np
import threading
import os

sensors = [
    'moisture',
    'humidity'
]


class Sensor(object):
    def __init__(self, greenhouseId, bedUuid, unicity=False):
        self.greenhouseId = greenhouseId

        if unicity:
            self.telemetric = os.environ['TELEMETRIC']
        else:
            self.telemetric = random.choice(sensors)

        self.bedUuid = bedUuid
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

    def talk(self):
        # Post dummy data
        try:
            requests.post(os.environ['URI'] + "/api/v1/" + self.telemetric,
                          headers={'Content-type': 'application/json',
                                   'Accept': 'application/json'},
                          json={
                              "sensor": self.uuid,
                              "value": str(np.random.normal(10, 0.7))
            })
        except Exception as e:
            print(e)

        print('Sensor ' + self.uuid + ' Posted')

        if self.unicity:
            threading.Timer(random.randint(1, 5), self.talk).start()
        else:
            threading.Timer(random.randint(5, 30), self.talk).start()
