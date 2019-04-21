import cherrypy
import json


class Dispatcher(object):
    def __init__(self):
        pass

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            # Verify is the uri is correct
            if vpath[0] != 'user':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['user'] = None
            cherrypy.request.params['greenhouse'] = False
            return UserREST()

        if len(vpath) == 2:
            if vpath[0] != 'user':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['user'] = vpath.pop(0)
            cherrypy.request.params['greenhouse'] = False
            return UserREST()

        if len(vpath) == 3:
            vpath.pop(0)
            cherrypy.request.params['user'] = vpath.pop(0)

            if vpath[0] == 'greenhouse':
                cherrypy.request.params['greenhouse'] = True
            else:
                cherrypy.request.params['greenhouse'] = False

            vpath.pop(0)
            return UserREST()

        return vpath


class UserREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, user, greenhouse, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET request on USER service",
            "user": user,
            "greenhouse": greenhouse,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, user, greenhouse, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "POST request on USER service",
            "user": user,
            "greenhouse": greenhouse,
            "params": params
        }


def json_error(status, message, traceback, version):
    cherrypy.response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'message': message})


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5001
    })

    cherrypy.tree.mount(Dispatcher(), '/api/v1', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.gzip.on': True,
            'error_page.default': json_error
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
