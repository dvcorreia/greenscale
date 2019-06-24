from bot import Bot
import os

os.environ['URI'] = 'http://localhost:80'
# If unicity is True select the telemetric you want ot test
os.environ['TELEMETRIC'] = 'moisture'

if __name__ == '__main__':
    # Set unicity to True to generate only one greenhouse, bed and sensor
    bot1 = Bot(unicity=True)
    bot1.talk()
