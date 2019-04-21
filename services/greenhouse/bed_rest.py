import cherrypy


class BedREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, greenhouse, bed, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET resquest on BedREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, bed, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on BedREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "params": params
        }
