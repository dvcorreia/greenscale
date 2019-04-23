import cherrypy
from mongoengine import connect
import os
from schemas import User


class UserREST(object):
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
                "id": str(u.id),
                "username": u.username,
                "greenhouses": u.greenhouses
            }
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, **params):

        # Try to grab it from the body
        user = cherrypy.request.json.get('username')
        # if there isn't one respond 400 Bad request
        if user is None:
            raise cherrypy.HTTPError(400, 'Username needed')

        u = User()
        u.username = user

        # checks if mongoengine raises an exception like:
        #   - user already exist
        #   - username to long
        try:
            u.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 201
        return {
            "status": 201,
            "data": {
                "id": str(u.id),
                "username": u.username
            }
        }

    @cherrypy.tools.json_out()
    def DELETE(self, **params):
        # Find user with the required username
        try:
            u = User.objects.get(id=params['id'])
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Delete user
        try:
            u.delete()
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "description": "User deleted",
            "user": {
                "id": str(u.id),
                "username": u.username
            }
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, **params):

        # Grab user id from body
        userid = cherrypy.request.json.get('id')
        if userid is None:
            raise cherrypy.HTTPError(400, 'User ID should be provided')

        # Find user with the required username
        try:
            u = User.objects.get(id=userid)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Update username
        if cherrypy.request.json.get('username') is not None:
            u.username = cherrypy.request.json.get('username')

        # Update document on DB
        try:
            res = u.save()
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "id": str(res.id),
                "username": res.username,
                "greenhouses": res.greenhouses
            }
        }
