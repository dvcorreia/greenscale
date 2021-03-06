import paho.mqtt.client as mqtt
from time import sleep
from schema import WarningSchema
import json
import re
import os
import datetime


class warningProbeClient(object):
    def __init__(self, host, port, channels):
        self.host = host
        self.port = port

        self.UUIDv4 = re.compile(
            r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

        self.mqtt = mqtt.Client(str(datetime.datetime.now()))

        # Callbacks configuration
        self.mqtt.on_connect = self.onConnect
        self.mqtt.on_message = lambda *_: print(
            "Message received on a non handled channel")
        # Channels callbacks
        for channel in channels:
            self.mqtt.message_callback_add(channel, self.onMessage)

        sleep(1)

        # Connect to the broker
        self.mqtt.connect(self.host, self.port)

        sleep(1)

        for channel in channels:
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
        print("Message received!", flush=True)
        topics = message.topic.split('/')

        # Verify if the channel topic has only telemetric/uuid
        if len(topics) > 2:
            return print("Error! " + message.topic +
                         " channel topic doesn't match the platform standard")

        if not self.UUIDv4.match(topics[-1]):
            return print("Error! uuid " + topics[-1] + " is not valid")

        data = json.loads(str(message.payload.decode("utf-8")))

        warning = WarningSchema()
        warning.target = topics[-1]
        warning.description = data['value']

        try:
            warning.save()
        except Exception as e:
            return print("Couldn't update db: " + str(e))
