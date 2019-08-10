import cherrypy
import os
from schema import Telemetric


class TelemetricREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        data = None
        if params['size'] is None:
            data = Telemetric.objects(sensor=params['uuid'])
        else:
            try:
                c = Telemetric.objects(sensor=params['uuid']).count()
                nquery = c - int(params['size'])
                if nquery < 0:
                    nquery = 0
                print(c)
                data = Telemetric.objects[nquery:](sensor=params['uuid'])
            except Exception as e:
                raise cherrypy.HTTPError(400, str(e))

        return {
            "sensorId": params['uuid'],
            "data": list(map(lambda d: {
                "v": str(d.value),
                "d": str(d.date)
            }, data))
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, **params):

        m = Telemetric()
        m.sensor = cherrypy.request.json.get('sensor')
        m.value = cherrypy.request.json.get('value')

        try:
            m.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 200
        return {
            "response": "Posted with the id"
        }
