import requests
import json
from config import Config
from sensor import Sensor
import random

plants = [
    'onions',
    'tomatos',
    'apples',
    'oranges',
    'cabbages',
    'cucumbers',
    'lettuce',
    'beans',
    'strawberries'
]


class Bed(object):
    def __init__(self, greenhouseId):
        self.plant = random.choice(plants)
        self.greenhouseId = greenhouseId
        self.conf = Config()

        # Create Bed
        try:
            r = requests.post(self.conf.uri + "/api/v1/greenhouse/" + greenhouseId + "/bed",
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"plant": self.plant})
        except Exception as e:
            print(e)

        data = json.loads(r.text)
        greenhouse = data['data']['greenhouse']

        self.uuid = greenhouse['bed']['uuid']
        self.sensors = greenhouse['bed']['sensors']

        self.createSensors()

    def createSensors(self):
        nsensors = random.randint(2, 5)

        for i in range(1, nsensors):
            self.sensors.append(
                Sensor(greenhouseId=self.greenhouseId, bedUuid=self.uuid))
            print('created sensor ' + str(i) + ' for bed ' + self.uuid)

    def talk(self):
        for s in self.sensors:
            s.talk()
