import requests
import json
from config import Config
import random
import numpy as np
import threading

sensors = [
    'moisture',
    'humidity'
]


class Sensor(object):
    def __init__(self, greenhouseId, bedUuid):
        self.greenhouseId = greenhouseId
        self.bedUuid = bedUuid
        self.telemetric = random.choice(sensors)
        self.conf = Config()

        # Create Sensor
        try:
            r = requests.post(self.conf.uri + "/api/v1/greenhouse/" + self.greenhouseId + "/bed/" + self.bedUuid + "/sensor",
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
            requests.post(self.conf.uri + "/api/v1/" + self.telemetric,
                          headers={'Content-type': 'application/json',
                                   'Accept': 'application/json'},
                          json={
                              "sensor": self.uuid,
                              "value": str(np.random.normal(10, 0.7))
                          })
        except Exception as e:
            print(e)

        print('Sensor ' + self.uuid + ' Posted')
        threading.Timer(random.randint(5, 50), self.talk).start()
