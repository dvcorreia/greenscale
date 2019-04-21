import cherrypy


class HumidityREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, humidity, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET request on Moisture service",
            "humidity": humidity,
            "param": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, humidity, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on the Moisture service",
            "humidity": humidity,
            "param": params
        }
