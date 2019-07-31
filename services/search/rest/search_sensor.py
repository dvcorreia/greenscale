import cherrypy
from mongoengine import connect
import os
import json
import requests
from schemas import Greenhouse


class SearchSensorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        # Get greenhouses from user
        r = requests.get("http://user:5001/api/v1/user",
                         params={"username": params['username']},
                         headers={'Accept': 'application/json'})

        if r.status_code is not 200:
            raise cherrypy.HTTPError(
                r.status_code, "Was not possible to get the user information: " + r.reason)

        # Search for a sensor with the uuid provided
        data = json.loads(r.text)
        greenhouses = data['data']['greenhouses']

        for greenhouse in greenhouses:
            r1 = requests.get("http://greenhouse:5001/api/v1/greenhouse",
                              params={"id": greenhouse},
                              headers={'Accept': 'application/json'})

            if r1.status_code is not 200:
                raise cherrypy.HTTPError(
                    r1.status_code, "Was not possible to get the greenhouse information: " + r.reason)

            gdata = json.loads(r1.text)

            beds = gdata['data']['greenhouse']['beds']

            for bed in beds:
                for sensor in bed['sensors']:
                    if sensor['uuid'] == params['uuid']:
                        cherrypy.response.status = 200
                        return {
                            "status": 200,
                            "sensor": sensor
                        }

            cherrypy.response.status = 404
            return {
                "status": 404
            }
