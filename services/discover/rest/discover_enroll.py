import cherrypy
from mongoengine import connect
import os
import json
import requests
from schemas import Sensor


class DiscoverEnrollREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        # Ask if the username and uuid received are enrolled in the platform
        r = requests.get("http://search:5001/api/v1/search",
                         params={
                             "username": params['username'], "uuid": params['uuid']},
                         headers={'Accept': 'application/json'})

        data = json.loads(r.text)

        # If code 200, they are, then send back the sensor information
        if r.status_code is 200:
            cherrypy.response.status = 200
            return {
                "uuid": str(data['sensor']['uuid']),
                "telemetric": data['sensor']['telemetric'],
                "user": params['username']
            }

        enrolled = True

        # Check if is waiting for greenhouse assignment in the discovery database
        try:
            s = Sensor.objects.get(uuid=params['uuid'])
        except Exception as e:
            enrolled = False

        if enrolled is True:
            cherrypy.response.status = 200
            return {
                "uuid": str(s.uuid),
                "telemetric": s.telemetric,
                "user": ""
            }

        # Enroll sensor
        s = Sensor(uuid=params['uuid'],
                   telemetric=params['telemetric'],
                   username=params['username'])

        # Try to save the sensor document on DB
        try:
            s.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 200
        return {
            "uuid": str(s.uuid),
            "telemetric": s.telemetric,
            "user": s.username
        }
