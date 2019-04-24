import cherrypy
from mongoengine import connect
import os
from schemas import User


class AddGreenhouseREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, **params):
        # Find user with the required username
        try:
            u = User.objects.get(username=params['username'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "greenhouses": u.greenhouses
            }
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, **params):

        # Try to grab user ID from the body
        userId = params['userId']
        # if there isn't one respond 400 Bad request
        if userId is None:
            raise cherrypy.HTTPError(400, 'User ID needed')

        # Try to grab it from the body
        greenhouses = cherrypy.request.json.get('greenhouses')
        # if there isn't one respond 400 Bad request
        if greenhouses is None:
            raise cherrypy.HTTPError(204, 'No greenhouse data passed')

        # Get user from DB
        try:
            u = User.objects.get(id=userId)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        for greenhouse in greenhouses:
            if greenhouse not in u.greenhouses:
                u.greenhouses.append(greenhouse)

        # Save and update document on DB
        try:
            u.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 201
        return {
            "status": 201,
            "data": {
                "id": str(u.id),
                "username": u.username,
                "greenhouses": u.greenhouses
            }
        }

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        # Find user with the required username
        try:
            u = User.objects.get(id=params['userId'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Delete greenhouse
        try:
            u.greenhouses.remove(params['greenhouseId'])
            u.save()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "description": "Greenhouse removed from User's greenhouses",
            "user": {
                "id": str(u.id),
                "username": u.username,
                "greenhouses": u.greenhouses
            }
        }
