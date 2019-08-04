import cherrypy
from mongoengine import connect
import os
import json
import requests
from schemas import Sensor


class DiscoverAllREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        # Check if is waiting for greenhouse assignment in the discovery database
        try:
            sensors = Sensor.objects(username=params['username'])
        except Exception as e:
            cherrypy.response.status = 404
            return {
                "status": 404,
                "message": str(e)
            }

        cherrypy.response.status = 200
        return {
            "status": 200,
            "sensors": list(map(lambda s: {
                "uuid": str(s.uuid),
                "telemetric": s.telemetric
            }, sensors))
        }
