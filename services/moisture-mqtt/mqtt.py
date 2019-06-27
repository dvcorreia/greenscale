from emitter import Client


class Mqtt(object):
    def __init__(self, host, port, key):
        self.host = host
        self.port = port
        self.key = key
        self.channel_keys = {}
        self.channel_key = 'geptuCiucW7pG9WhiGgwgDxFiC-Rv1yW'

        self.emitter = Client()

        # Callbacks configuration
        self.emitter.on_connect = self.onConnect()
        self.emitter.on_message = lambda m: self.onMessage(
            m.channel, m.as_string())
        self.emitter.on_keygen = lambda k: self.onKeygen(k)

        # Connect to the broker#
        self.emitter.connect(self.host, int(self.port), False, 30)

    def subscribe(self, channel):
        self.emitter.subscribe(self.channel_key,
                               channel,
                               options={Client.with_last(0)})
        print("Subscribed to channel " + channel)

    def publish(self, channel, message):
        self.emitter.publish(self.channel_key,
                             channel,
                             message,
                             {Client.with_ttl(86400), Client.without_echo()})
        print('Pub on channel ' + channel + ': ' + message)

    def keygen(self, channel):
        self.emitter.keygen(self.key, channel, "rw")

    def onKeygen(self, k):
        if k['status'] == 200:
            print("Generated keygen: " + str(k))
            self.channel_keys[k['channel']] = k['key']
        else:
            print("onKeygen error " + str(k['status']) + ': ' + k['message'])

    def listen(self):
        self.emitter.loop_start()
        while True:
            pass

    # Callbacks
    def onConnect(self):
        return print("Connected to the broker " + self.host + " on port " + self.port)

    def onMessage(self, channel, message):
        m = message[2:len(message)-1]
        return print("Message received on channel " + channel + " : " + m)
