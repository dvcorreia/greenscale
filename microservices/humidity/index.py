import markdown
import cherrypy
import json
import os


class Humidity(object):
    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri):
        if len(uri) == 0:
            with open(os.path.dirname(os.path.abspath(__file__)) + '/README.md', 'r') as markdown_file:
                content = markdown_file.read()
                return markdown.markdown(content)

        return json.dumps({"error": "route doesn't exist"})


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5002
    })
    cherrypy.tree.mount(Humidity(), '/api/v1/humidity', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
