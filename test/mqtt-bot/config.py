import os


class Config(object):
    def __init__(self):
        os.environ['URI'] = "http://localhost:80"

        os.environ['HOST'] = "localhost"
        os.environ['PORT'] = "8080"
        os.environ['CHANNEL_KEY'] = "ea2oE_cLeqzsXNafzhAoIpfewZlx3VeI"
        os.environ['CHANNEL'] = "sensor/moisture/"

        # If unicity is True select the telemetric you want ot test
        os.environ['TELEMETRIC'] = 'moisture'
