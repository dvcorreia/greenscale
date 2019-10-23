import cherrypy
from mongoengine import connect
import os
import re
from schemas import Actuator


class ActuatorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        if params['uuid'] is None:
            raise cherrypy.HTTPError(400, str("UUID should be passed"))

        # Find actuator with the required uuid
        try:
            actuator = Actuator.objects.get(uuid=params['uuid'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": actuator.to_json()
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, **params):
        actuator = Actuator()

        print(cherrypy.request.json)

        if cherrypy.request.json.get("uuid") is not None:
            UUIDv4 = re.compile(
                r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

            if not UUIDv4.match(cherrypy.request.json.get('uuid')):
                return print("Error! uuid " + cherrypy.request.json.get('uuid') + " is not valid")

            actuator.uuid = cherrypy.request.json.get('uuid')

        if cherrypy.request.json.get('description') is not None:
            actuator.description = cherrypy.request.json.get('description')

        if cherrypy.request.json.get('username') is not None:
            actuator.username = cherrypy.request.json.get('username')

        try:
            actuator.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 201
        return {
            "status": 201,
            "data": actuator.to_json()
        }

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        try:
            actuator = Actuator.objects.get(uuid=params['uuid'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        try:
            actuator.delete()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "description": "Actuator deleted",
            "data": actuator.to_json()
        }
