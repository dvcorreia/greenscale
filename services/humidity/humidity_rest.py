import cherrypy
from schema import Humidity


class HumidityREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        if params['size'] is None:
            data = Humidity.objects(sensor=params['uuid'])
        else:
            try:
                data = Humidity.objects[:int(params['size'])](
                    sensor=params['uuid'])
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

        h = Humidity()
        h.sensor = cherrypy.request.json.get('sensor')
        h.value = cherrypy.request.json.get('value')

        try:
            h.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 200
        return {
            "response": "Posted with the id"
        }
