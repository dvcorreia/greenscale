import cherrypy
from schemas import Greenhouse, Bed, Sensor


class SensorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, bed, **params):
        # Find user greenhouse the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        sensor = Sensor(telemetric=cherrypy.request.json.get('telemetric'))

        # Index the wanted bed
        for idx, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == bed:
                gh.beds[idx].sensors.append(sensor)

        try:
            gh.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

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
    def PUT(self, greenhouse, bed, **params):
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Index the wanted bed
        for idx1, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == bed:
                for idx2, sensoridx in enumerate(gh.beds[idx1].sensors):
                    if str(sensoridx['uuid']) == params['uuid']:
                        if cherrypy.request.json.get('telemetric') is not None:
                            gh.beds[idx1].sensors[idx2].telemetric = cherrypy.request.json.get(
                                'telemetric')

                        if cherrypy.request.json.get('hardwareId') is not None:
                            gh.beds[idx1].sensors[idx2].hardwareId = cherrypy.request.json.get(
                                'hardwareId')

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
    def DELETE(self, greenhouse, bed, **params):
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Index the wanted bed
        for idx1, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == bed:
                for idx2, sensoridx in enumerate(gh.beds[idx1].sensors):
                    if str(sensoridx['uuid']) == params['uuid']:
                        gh.beds[idx1].sensors.pop(idx2)

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
