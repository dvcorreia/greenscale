import cherrypy
import os
from mongoengine import *
import datetime
import json


class MoistureDBSchema(Document):
    sensor = StringField(required=True)
    value = DecimalField(required=True)
    date = DateTimeField(default=datetime.datetime.utcnow)


class Dispatcher(object):
    def __init__(self):
        self.moistureREST = MoistureREST()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 4:
            cherrypy.request.params['user'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['moisture'] = ''
            return self.moistureREST

        if len(vpath) == 5:
            cherrypy.request.params['user'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['moisture'] = vpath.pop(0)
            return self.moistureREST

        return vpath


class MoistureREST(object):
    def __init__(self):
        username = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
        password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
        connect("moistures_db", host="mongodb://" + username + ":" + password +
                "@db-moisture:" + str(27017) + '/?authSource=admin')

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, user, greenhouse, moisture, **params):

        cherrypy.response.status = 200

        data = []

        for measures in MoistureDBSchema.objects():
            data.append({
                "sensor": measures.sensor,
                "value": str(measures.value),
                "date": str(measures.date)
            })

        return {
            "status": 200,
            "data": data
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, user, greenhouse, moisture, **params):

        cherrypy.response.status = 200

        telemetric = MoistureDBSchema()
        telemetric.sensor = cherrypy.request.json.get('sensorId')
        telemetric.value = cherrypy.request.json.get('value')
        telemetric.save()

        return {
            "status": 200
        }


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5001
    })

    cherrypy.tree.mount(Dispatcher(), '/api/v1', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.gzip.on': True
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
