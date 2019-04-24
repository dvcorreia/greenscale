import cherrypy
from schemas import Greenhouse
import requests


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
        # Try to grab user ID from the body
        userId = cherrypy.request.json.get('userId')
        # if there isn't one respond 400 Bad request
        if userId is None:
            raise cherrypy.HTTPError(400, 'User ID needed')

        # create greenhouse
        gh = Greenhouse()
        gh.location = cherrypy.request.json.get('location')

        # checks if mongoengine raises an exception like
        try:
            gh.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))
        else:
            r = requests.post("http://user:5001/api/v1/user/greenhouse",
                              params={"userId": userId},
                              headers={'Content-type': 'application/json',
                                       'Accept': 'application/json'},
                              json={"greenhouses": [str(gh.id)]})

        if r.status_code is not 201:
            gh.delete()
            raise cherrypy.HTTPError(
                r.status_code, "Was not possible to update the user: " + r.reason)

        cherrypy.response.status = 201
        return {
            "status": 201,
            "data": {
                "userId": userId,
                "greenhouse": {
                    "id": str(gh.id),
                    "location": gh.location,
                    "beds": gh.beds
                }
            }
        }
