import cherrypy
import json
from rest.discover import DiscoverREST

import os
from mongoengine import connect

connect("discover", host="mongodb://" + os.environ.get('MONGO_USERNAME') +
        ":" + os.environ.get('MONGO_PASSWORD') +
        "@db:" + str(27017) + '/?authSource=admin')


def json_error(status, message, traceback, version):
    cherrypy.response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'message': message})


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.gzip.on': True,
            'error_page.default': json_error
        }
    }

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5001
    })

    cherrypy.tree.mount(DiscoverREST(), '/api/v1/discover', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
