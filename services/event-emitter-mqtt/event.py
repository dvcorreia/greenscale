import paho.mqtt.client as mqtt
from time import sleep
from schema import Sensor, Event, eventTypeCatalog, eventVerificationCatalog
import json
import re
import os
import datetime
import threading


class eventClient(object):
    def __init__(self, host, port, channels):
        self.host = host
        self.port = port

        self.mqtt = mqtt.Client(str(datetime.datetime.now()))

        self.UUIDv4 = re.compile(
            r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

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
        topics = message.topic.split('/')

        # Verify if the channel topic has only telemetric/uuid
        if len(topics) > 3:
            return print("Error! " + message.topic +
                         " channel topic doesn't match the platform standard")

        if not self.UUIDv4.match(topics[-1]):
            return print("Error! uuid " + topics[-1] + " is not valid")

        data = json.loads(str(message.payload.decode("utf-8")))

        if topics[0] == "sensor":
            self.onMessageTelemetricProbe(message, topics, data)
        elif topics[0] == "event":
            self.onMessageEvent(message, topics, data)
        else:
            pass

    def onMessageEvent(self, message, topics, data):
        if topics[1] == "add":
            # Try grab the sensor from the DB
            try:
                sensor = Sensor.objects.get(sensor=topics[-1])
            except Exception as e:
                sensor = None

            if sensor is None:
                # Create sensor in event db and add event
                sensor = Sensor()
                sensor.sensor = topics[-1]

            event = Event()
            event.event_type = data['event-type']
            if data.get('target') is not None:
                event.target = data['target']
            event.logic = data['logic']
            event.logic_value = data['logic-value']
            if data.get('warning-message') is not None:
                event.warning_message = data['warning-message']
            if data.get('actuation-type') is not None:
                event.actuation_type = data['actuation-type']
            if data.get('actuation-state') is not None:
                event.actuation_state = data['actuation-state']
            if data.get('time') is not None:
                event.time = data['time']
            sensor.events.append(event)

            try:
                sensor.save()
            except Exception as e:
                return print("Couldn't save to event db: " + str(e))

            return print("Event saved to db")

        elif topics[1] == "delete":
            try:
                sensor = Sensor.objects.get(sensor=topics[-1])
            except Exception as e:
                sensor = None

            if sensor is None:
                # Create sensor in event db and add event
                return print("Sensor not found")

            notfound = True
            # Index the wanted event
            for idx, eventidx in enumerate(sensor.events):
                if str(eventidx['uuid']) == data['uuid']:
                    notfound = False
                    sensor.events.pop(idx)

            if notfound is True:
                return print("Event couldn't be deleted, not found")

            try:
                sensor.save()
            except Exception as e:
                return print("Error saving deletion to db" + str(e))

            return print("Event " + data['uuid'] + " deleted")
        else:
            return print("Channel " + message.topic + " not handled")

    def onMessageTelemetricProbe(self, message, topics, data):
        # Try to check if the sensor has an event associated
        try:
            sensor = Sensor.objects.get(sensor=topics[-1])
        except Exception as e:
            print("Couldn retrieve from db: " + str(e))
            return

        for idx, eventidx in enumerate(sensor.events):
            # Process events
            self.process_event(value=float(data['value']),
                               event=eventidx)
            sensor.events[idx].last_occurred = datetime.datetime.utcnow

        try:
            sensor.save()
        except Exception as e:
            return print("Couldn't update db: " + str(e))

    def process_event(self, value, event):
        # Process logic
        logicFlag = {
            eventVerificationCatalog[0]: value > event['logic_value'],
            eventVerificationCatalog[1]: value >= event['logic_value'],
            eventVerificationCatalog[2]: value < event['logic_value'],
            eventVerificationCatalog[3]: value <= event['logic_value'],
            eventVerificationCatalog[4]: value == event['logic_value']
        }.get(event['logic'], False)

        if logicFlag is False:
            return

        # Verify if target uuid is valid
        if not self.UUIDv4.match(str(event['target'])):
            return

        if event['event_type'] == 'actuator':
            # Check the time of actuation
            if event['actuation_type'] == 'momentary':
                self.publish(
                    "actuator/" + str(event['target']), {"value": "ON"})
                # Generate thread with the OFF switch
                # return threading.Timer(event['time'], self.publish("actuator/" + str(event['target']), {"value": "OFF"})).start()
                return threading.Timer(event['time'],
                                       lambda: eventClient(os.environ['HOST'],
                                                           int(os.environ['PORT']),
                                                           []).publish("actuator/" + str(event['target']), {"value": "OFF"})
                                       ).start()
            elif event['actuation_type'] == 'switch':
                return self.publish("actuator/" + str(event['target']), {"value": "SWITCH"})
            elif event['actuation_type'] == 'fixed':
                return self.publish("actuator/" + str(event['target']), {"value": event['actuation_state']})
            else:
                pass
        elif event['event_type'] == 'warning':
            if event['warning_message'] is None:
                return self.publish("warning/" + str(event['target']), {"message": "No warning message"})
            else:
                return self.publish("warning/" + str(event['target']), {"message": event['warning_message']})
        else:
            pass

        # publish on the event type with event not know
        return self.publish(event['event_type'] + "/" + str(event['target']), {"message": "Event type type not know"})
