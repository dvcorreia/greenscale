import cherrypy
import os


class Dispatcher(object):
    def __init__(self):
        self.moisture = Moisture()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 4:
            cherrypy.request.params['user'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['moisture'] = ''
            return self.moisture

        if len(vpath) == 5:
            cherrypy.request.params['user'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['moisture'] = vpath.pop(0)
            return self.moisture

        return vpath


class Moisture(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, user, greenhouse, moisture, **params):

        cherrypy.response.status = 200

        return {
            "user": user,
            "greenhouse": greenhouse,
            "moisture": moisture,
            "params": params
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
