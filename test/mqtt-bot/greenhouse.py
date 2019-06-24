import requests
import json
from bed import Bed
import random
import os

locations = [
    'Torino',
    'Milan',
    'Padua',
    'Venice',
    'Rome',
]


class Greenhouse(object):
    def __init__(self, usedId, unicity=False):
        self.location = random.choice(locations)
        self.userId = usedId
        self.unicity = unicity

        # Create Greenhouse
        try:
            r = requests.post(os.environ['URI'] + "/api/v1/greenhouse",
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
        if self.unicity:
            nbeds = 2
        else:
            nbeds = random.randint(2, 10)

        for i in range(1, nbeds):
            self.beds.append(Bed(greenhouseId=self.id, unicity=self.unicity))
            print('created bed ' + str(i) + ' for greenhouse ' + self.id)

    def talk(self):
        for b in self.beds:
            b.talk()
