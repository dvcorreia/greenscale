import requests
import json
from config import Config
from bed import Bed
import random

locations = [
    'Torino',
    'Milan',
    'Padua',
    'Venice',
    'Rome',
]


class Greenhouse(object):
    def __init__(self, usedId):
        self.location = random.choice(locations)
        self.userId = usedId
        self.conf = Config()

        # Create Greenhouse
        try:
            r = requests.post(self.conf.uri + "/api/v1/greenhouse",
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"userId": self.userId, "location": self.location})
        except Exception as e:
            print(e)

        data = json.loads(r.text)
        greenhouse = data['data']['greenhouse']

        self.id = greenhouse['id']
        self.beds = greenhouse['beds']

        self.createBeds()

    def createBeds(self):
        nbeds = random.randint(2, 10)

        for i in range(1, nbeds):
            self.beds.append(Bed(greenhouseId=self.id))
            print('created bed ' + str(i) + ' for greenhouse ' + self.id)

    def talk(self):
        for b in self.beds:
            b.talk()
