import cherrypy


@cherrypy.popargs('user')
class User(object):
    def __init__(self):
        self.greenhouse = Greenhouse()


@cherrypy.popargs('greenhouse')
class Greenhouse(object):
    def __init__(self):
        self.moisture = Moisture()


@cherrypy.popargs('moisture')
class Moisture(object):
    exposed = True

    def GET(self, user, greenhouse, moisture):
        return 'user: %s\ngreenhouse: %s\nmoisture: %s\n' % (user, greenhouse, moisture)


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5001
    })

    cherrypy.tree.mount(User(), '/api/v1', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
