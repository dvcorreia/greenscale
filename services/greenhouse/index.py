import cherrypy
import json
from greenhouse_rest import GreenhouseREST
from bed_rest import BedREST
from sensor_rest import SensorREST


class Dispatcher(object):
    def __init__(self):
        GreenhouseREST()

    def _cp_dispatch(self, vpath):
        # Handle /api/v1/greenhouse
        if len(vpath) == 1:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = None
            return GreenhouseREST()

        # Handle /api/v1/greenhouse/<id>
        if len(vpath) == 2:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            return GreenhouseREST()

        # Handle /api/v1/greenhouse/<id>/bed
        if len(vpath) == 3:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            if vpath[0] != 'bed':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['bed'] = None
            return BedREST()

        # Handle /api/v1/greenhouse/<id>/bed/<id>
        if len(vpath) == 4:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            if vpath[0] != 'bed':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['bed'] = vpath.pop(0)
            return BedREST()

        # Handle /api/v1/greenhouse/<id>/bed/<id>/sensor
        if len(vpath) == 5:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            if vpath[0] != 'bed':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['bed'] = vpath.pop(0)
            if vpath[0] != 'sensor':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['sensor'] = None
            return SensorREST()

        # Handle /api/v1/greenhouse/<id>/bed/<id>/sensor/<uuid>
        if len(vpath) == 6:
            if vpath[0] != 'greenhouse':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['greenhouse'] = vpath.pop(0)
            if vpath[0] != 'bed':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['bed'] = vpath.pop(0)
            if vpath[0] != 'sensor':
                return vpath
            vpath.pop(0)
            cherrypy.request.params['sensor'] = vpath.pop(0)
            return SensorREST()

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
