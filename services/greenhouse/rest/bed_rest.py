import cherrypy
from schemas import Greenhouse, Bed


class BedREST(object):
    def __init__(self):
        pass

    exposed = True

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

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, greenhouse, **params):
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Update plant type
        if cherrypy.request.json.get('plant') is not None:
            # Index the wanted bed
            for idx, bedidx in enumerate(gh.beds):
                if str(bedidx['uuid']) == params['uuid']:
                    gh.beds[idx].plant = cherrypy.request.json.get('plant')

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
    def DELETE(self, greenhouse, **params):
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Index the wanted bed
        for idx, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == params['uuid']:
                gh.beds.pop(idx)

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
