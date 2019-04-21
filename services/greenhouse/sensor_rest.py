import cherrypy


class SensorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, greenhouse, bed, sensor, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET resquest on SensorREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "sensor": sensor,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, bed, sensor, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on SensorREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "sensor": sensor,
            "params": params
        }
