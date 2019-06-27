from mqtt import Mqtt
import os

os.environ['HOST'] = 'localhost'
os.environ['PORT'] = '8080'
os.environ['KEY'] = '8hiuiFt1MZ469D0owBlaibkVcERscGyA'

if __name__ == '__main__':

    client = Mqtt(os.environ['HOST'],
                  os.environ['PORT'],
                  os.environ['KEY'])

    client.keygen('test/2/')
    client.publish('test/1/', "Message test")
    client.listen()
