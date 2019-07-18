import paho.mqtt.client as mqtt
from time import sleep
from schema import Moisture
import json


class Client(object):
    def __init__(self, host, port, channel):
        self.host = host
        self.port = port

        self.mqtt = mqtt.Client("id")

        # Callbacks configuration
        self.mqtt.on_connect = self.onConnect
        self.mqtt.on_message = lambda *_: print(
            "Message received on a non handled channel")
        # Channels callbacks
        self.mqtt.message_callback_add(channel, self.onMessage)

        sleep(1)

        # Connect to the broker
        self.mqtt.connect(self.host, self.port)

        sleep(1)

        self.mqtt.subscribe(channel)
        print("Subscribed to channel " + channel)

    def publish(self, channel, message):
        self.mqtt.publish(channel, json.dumps(message))
        print('Pub on channel ' + channel + ': ' + json.dumps(message))

    def listen(self, forever=False):
        try:
            if forever:
                print("Starting loop_forever thread ...", flush=True)
                self.mqtt.loop_forever()
            else:
                self.mqtt.loop_start()
                while True:
                    pass
        finally:
            print("\nClosing mqtt connect ...")
            self.mqtt.disconnect()
            if not forever:
                self.mqtt.loop_stop()
            print("Exited the connection safelly!")

    # Callbacks
    def onConnect(self, client, userdata, flags, rc):
        m = "Connected flags" + str(flags) + "result code " \
            + str(rc) + "client1_id " + str(client)
        print(m + "\nConnected to the broker " +
              self.host + " on port " + self.port)

    def onMessage(self, client, userdata, message):
        print(json.loads(str(message.payload.decode("utf-8"))), flush=True)

        #m = Moisture()
        #m.sensor = data['sensor']
        #m.value = data['value']

        # try:
        #    m.save()
        # except Exception as e:
        #    print("couldn't save received measurement on DB:\n" + str(e))
