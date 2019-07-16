from mqtt import Mqtt
import os

os.environ['HOST'] = 'localhost'
os.environ['PORT'] = '1883'

if __name__ == '__main__':

    client = Mqtt(os.environ['HOST'],
                  int(os.environ['PORT']))

    client.subscribe('test/1/')
    client.listen(forever=True)
