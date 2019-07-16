import paho.mqtt.client as mqtt
from time import sleep


class Mqtt(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.mqtt = mqtt.Client("id")

        # Callbacks configuration
        self.mqtt.on_connect = self.onConnect
        self.mqtt.on_message = self.onMessage

        sleep(1)

        # Connect to the broker
        self.mqtt.connect(self.host, self.port)

    def subscribe(self, channel):
        self.mqtt.subscribe(channel)
        self.mqtt.message_callback_add(channel, self.onMessage)
        print("Subscribed to channel " + channel)

    def publish(self, channel, message):
        self.mqtt.publish(channel, message)
        print('Pub on channel ' + channel + ': ' + message)

    def listen(self, forever=False):
        try:
            if forever:
                self.mqtt.loop_forever()
            else:
                self.mqtt.loop_start()
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
        print(str(message.payload.decode("utf-8")))
