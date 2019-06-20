import requests
import json
from config import Config
from greenhouse import Greenhouse
import random

names = [
    'Diogo',
    'Joao',
    'Alfredo',
    'Joana',
    'Romeu',
]


class Bot(object):
    def __init__(self):
        # Configuration object
        self.conf = Config()
        self.username = random.choice(
            names) + str(random.randint(1, 999))   # Generate random name
        self.id = ''
        self.greenhouses = []

        # Create user
        self.createUser()
        self.createGreenhouses()

    def createUser(self):
        try:
            r = requests.post(self.conf.uri + "/api/v1/user",
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
        ngreenhouses = random.randint(1, 10)

        for i in range(1, ngreenhouses):
            self.greenhouses.append(Greenhouse(self.id))
            print('created greenhouse ' + str(i) +
                  ' for user ' + self.username)

    def talk(self):
        for g in self.greenhouses:
            g.talk()
