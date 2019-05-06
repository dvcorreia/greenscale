import cherrypy
from schemas import Greenhouse, Bed, Sensor


class SensorREST(object):
    def __init__(self):
        pass

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, greenhouse, bed, sensor, **params):
        cherrypy.response.status = 200
        return {
            "status": 200,
            "data": "GET resquest on SensorREST",
            "greenhouse": greenhouse,
            "bed": bed,
            "sensor": sensor,
            "params": params
        }

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, greenhouse, bed, **params):
        # Find user greenhouse the required id
        try:
            gh = Greenhouse.objects.get(id=greenhouse)
        except Exception as e:
            raise cherrypy.HTTPError(404, str(e))

        sensor = Sensor(telemetric=cherrypy.request.json.get('telemetric'))

        # Index the wanted bedßß
        for idx, bedidx in enumerate(gh.beds):
            print(str(bedidx['uuid']))
            if str(bedidx['uuid']) == bed:
                print('found')
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
