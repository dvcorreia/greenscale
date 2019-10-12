import cherrypy
from mongoengine import connect
import os
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
        actuator.description = cherrypy.request.json.get('description')
        if cherrypy.request.json.get('time') is not None:
            actuator.time = cherrypy.request.json.get('time')
        if cherrypy.request.json.get('ip') is not None:
            actuator.ip = cherrypy.request.json.get('ip')

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
