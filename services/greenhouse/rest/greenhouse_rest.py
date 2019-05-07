import cherrypy
from schemas import Greenhouse
import requests


class GreenhouseREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        # Find user greenhouse the required id
        try:
            gh = Greenhouse.objects.get(id=params['id'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Build data
        beds_data = list(map(lambda bed: {
            "uuid": str(bed.uuid),
            "plant": bed.plant,
            "sensors": list(map(lambda s: {
                "uuid": str(s.uuid),
                "telemetric": s.telemetric,
                "hardwareId": s.hardwareId
            }, bed.sensors))
        }, gh.beds))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "greenhouse": {
                    "id": str(gh.id),
                    "location": gh.location,
                    "beds": beds_data
                }
            }
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

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, **params):
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=params['id'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Update location
        if cherrypy.request.json.get('location') is not None:
            gh.location = cherrypy.request.json.get('location')

        # Update document on DB
        try:
            gh.save()
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Build data
        beds_data = list(map(lambda bed: {
            "uuid": str(bed.uuid),
            "plant": bed.plant,
            "sensors": list(map(lambda s: {
                "uuid": str(s.uuid),
                "telemetric": s.telemetric,
                "hardwareId": s.hardwareId
            }, bed.sensors))
        }, gh.beds))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "greenhouse": {
                    "id": str(gh.id),
                    "location": gh.location,
                    "beds": beds_data
                }
            }
        }

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        # Find user greenhouse the required id
        try:
            gh = Greenhouse.objects.get(id=params['id'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Delete greenhouse
        try:
            gh.delete()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        # TODO:
        # request the user service to delete the greenhouse entry if only one user has the greenhouse

        # Build data
        beds_data = list(map(lambda bed: {
            "uuid": str(bed.uuid),
            "plant": bed.plant,
            "sensors": list(map(lambda s: {
                "uuid": str(s.uuid),
                "telemetric": s.telemetric,
                "hardwareId": s.hardwareId
            }, bed.sensors))
        }, gh.beds))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "greenhouse": {
                    "id": str(gh.id),
                    "location": gh.location,
                    "beds": beds_data
                }
            }
        }
