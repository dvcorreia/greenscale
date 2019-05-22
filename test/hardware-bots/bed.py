import requests
import json
from config import Config
import random


class Bed(object):
    def __init__(self, plant, greenhouseId):
        self.plant = plant
        self.greenhouseId = greenhouseId
        self.conf = Config()

        # Create Bed
        try:
            r = requests.post(self.conf.uri + "/api/v1/greenhouse/${greenhouseId}/bed",
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"plant": self.plant})
        except Exception as e:
            print(e)

        data = json.loads(r.text)
        greenhouse = data['data']['greenhouse']

        self.id = greenhouse['id']
        self.beds = greenhouse['beds']
