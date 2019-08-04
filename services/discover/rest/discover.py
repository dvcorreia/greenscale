import cherrypy
from mongoengine import connect
import os
import json
import requests
from schemas import Sensor


class DiscoverREST(object):
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

        # Check if is waiting for greenhouse assignment in the discovery database
        try:
            s = Sensor.objects.get(uuid=params['uuid'])
        except Exception as e:
            cherrypy.response.status = 404
            return {
                "status": 404,
                "message": str(e)
            }

        cherrypy.response.status = 200
        return {
            "uuid": str(s.uuid),
            "telemetric": s.telemetric,
            "user": ""
        }

    @cherrypy.tools.json_out()
    def POST(self, **params):
        s = Sensor(telemetric=params['telemetric'],
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

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        # Find sensor with the required uuid
        try:
            s = Sensor.objects.get(uuid=params['uuid'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Delete sensor
        try:
            s.delete()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "message": "Sensor removed"
        }
