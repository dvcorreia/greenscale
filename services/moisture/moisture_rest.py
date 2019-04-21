import cherrypy


class MoistureREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, moisture, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET request on Moisture service",
            "moisture": moisture,
            "param": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, moisture, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on the Moisture service",
            "moisture": moisture,
            "param": params
        }
