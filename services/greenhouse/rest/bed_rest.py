import cherrypy
from schemas import Greenhouse, Bed


class BedREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, greenhouse, bed, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET resquest on BedREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, **params):

        # Find user greenhouse the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        bed = Bed(plant=cherrypy.request.json.get('plant'))
        gh.beds.append(bed)

        try:
            gh.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        beds_data = list(map(lambda bed: {
            "uuid": str(bed.uuid),
            "plant": bed.plant
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
