from bot import Bot
from config import Config

if __name__ == '__main__':
    Config()
    # Set unicity to True to generate only one greenhouse, bed and sensor
    bot1 = Bot(unicity=True)
    bot1.talk()
