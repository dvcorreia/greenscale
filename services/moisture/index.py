import cherrypy
import json
from moisture_rest import MoistureREST


class Dispatcher(object):
    def __init__(self):
        pass

    def _cp_dispatch(self, vpath):
        # Handle /api/v1/moisture
        if len(vpath) == 1:
            if vpath[0] != 'moisture':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['moisture'] = None
            return MoistureREST()

        # Handle /api/v1/moisture/<uuid>
        if len(vpath) == 2:
            if vpath[0] != 'moisture':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['moisture'] = vpath.pop(0)
            return MoistureREST()

        return vpath


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
