import requests
import json
from config import Config


class Bot(object):
    def __init__(self, username):
        self.conf = Config()
        self.username = username
        self.id = ''
        self.greenhouses = []

        # Create user
        self.createUser()

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

    def printBot(self):
        print('username: ' + self.username)
        print('id: ' + self.id)
        print('greenhouses:')
        print(self.greenhouses)
