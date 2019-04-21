import cherrypy


class GreenhouseREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, greenhouse, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET resquest on GreenhouseREST",
            "greenhouse": greenhouse,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on GreenhouseREST",
            "greenhouse": greenhouse,
            "params": params
        }
