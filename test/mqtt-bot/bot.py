import requests
import json
from greenhouse import Greenhouse
import random
import os

names = [
    'allessandra',
    'alice',
    'arianna',
    'patrizio',
    'massimo',
    'donatello',
    'stefano',
    'gian'
]


class Bot(object):
    def __init__(self, unicity=False):
        self.username = random.choice(
            names) + str(random.randint(1, 999))   # Generate random name
        self.id = ''
        self.greenhouses = []
        self.unicity = unicity

        # Create user
        self.createUser()
        self.createGreenhouses()

    def createUser(self):
        try:
            r = requests.post(os.environ['URI'] + "/api/v1/user",
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"username": self.username})
        except Exception as e:
            print(e)

        data = json.loads(r.text)
        user = data['data']

        self.id = user['id']
        self.greenhouses = user['greenhouses']

    def createGreenhouses(self):
        if self.unicity:
            ngreenhouses = 2
        else:
            ngreenhouses = random.randint(1, 10)

        for i in range(1, ngreenhouses):
            self.greenhouses.append(Greenhouse(self.id, unicity=self.unicity))
            print('created greenhouse ' + str(i) +
                  ' for user ' + self.username)

    def talk(self):
        for g in self.greenhouses:
            g.talk()
