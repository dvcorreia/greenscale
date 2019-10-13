import cherrypy
from mongoengine import connect
import os
from schemas import WarningSchema


class WarningREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        if params['uuid'] is None:
            raise cherrypy.HTTPError(400, str("UUID should be passed"))

        # Find warning with the required uuid
        try:
            warnings = WarningSchema.objects.get(target=params['target'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": warnings.to_json()
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, **params):
        warning = WarningSchema()
        warning.target = cherrypy.request.json.get('target')
        if cherrypy.request.json.get('description') is not None:
            warning.description = cherrypy.request.json.get('description')

        try:
            warning.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 201
        return {
            "status": 201,
            "data": warning.to_json()
        }

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        try:
            warning = WarningSchema.objects.get(target=params['target'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        try:
            for w in warning:
                w.delete()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "description": "Warnings deleted"
        }
