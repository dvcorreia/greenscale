import cherrypy
from schemas import Greenhouse, Bed, Sensor


class SensorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, bed, **params):
        notfound = True

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
                notfound = False

        if notfound is True:
            raise cherrypy.HTTPError(
                404, 'Bed with the uuid ' + bed + ' was not found')

        try:
            gh.save()
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))

        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": {
                "greenhouse": {
                    "id": str(gh.id),
                    "location": gh.location,
                    "beds": {
                        "uuid": bed,
                        "sensor": {
                            "uuid": sensor.uuid,
                            "telemetric": sensor.telemetric,
                            "hardwareId": sensor.hardwareId
                        }
                    }
                }
            }
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, greenhouse, bed, **params):
        notfound_bed, notfound_sensor = True, True
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Index the wanted bed
        for idx1, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == bed:
                notfound_bed = False
                for idx2, sensoridx in enumerate(gh.beds[idx1].sensors):
                    if str(sensoridx['uuid']) == params['uuid']:
                        notfound_sensor = False
                        if cherrypy.request.json.get('telemetric') is not None:
                            gh.beds[idx1].sensors[idx2].telemetric = cherrypy.request.json.get(
                                'telemetric')

                        if cherrypy.request.json.get('hardwareId') is not None:
                            gh.beds[idx1].sensors[idx2].hardwareId = cherrypy.request.json.get(
                                'hardwareId')

        # Raise errors for not found ids
        if notfound_bed is True:
            raise cherrypy.HTTPError(
                404, 'Bed with the uuid ' + bed + ' was not found')

        if notfound_sensor is True:
            raise cherrypy.HTTPError(
                404, 'Sensor with the uuid ' + str(params['uuid']) + ' was not found')

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
        notfound_bed, notfound_sensor = True, True
        # Find greenhouse with the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        # Index the wanted bed
        for idx1, bedidx in enumerate(gh.beds):
            if str(bedidx['uuid']) == bed:
                notfound_bed = False
                for idx2, sensoridx in enumerate(gh.beds[idx1].sensors):
                    if str(sensoridx['uuid']) == params['uuid']:
                        notfound_sensor = False
                        gh.beds[idx1].sensors.pop(idx2)

        # Raise errors for not found ids
        if notfound_bed is True:
            raise cherrypy.HTTPError(
                404, 'Bed with the uuid ' + bed + ' was not found')

        if notfound_sensor is True:
            raise cherrypy.HTTPError(
                404, 'Sensor with the uuid ' + str(params['uuid']) + ' was not found')

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
