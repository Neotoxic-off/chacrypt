import sys
import random

from src.rotor import Rotor
from src.config import Config
from src.message import Message

class Core:
    def __init__(self):
        self.size = 64
        self.key = []
        self.rotors = []
        self.message = None

        self.__setup__()
        self.__load__()
        self.__run__()

    def __setup__(self):
        self.message = Message("message.txt")

        for i in range(0, self.size):
            self.key.append(chr(random.randint(32, 126)))

    def __load__(self):
        print("adding {} rotors".format(self.size))

        for c in self.key:
            self.rotors.append(Rotor(ord(c)))

        if (len(self.rotors) == self.size):
            print(f"{self.size} rotors added")

    def __run__(self):
        sentense = []
        selection = 0

        print("key: '{}'".format("".join(self.key)))

        for index, character in enumerate(self.message.message):
            sentense.append(self.rotors[selection].get(character))
            selection += 1

            if (selection >= len(self.rotors)):
                selection = 0

        self.__dump__(sentense)

    def __dump__(self, data: list):
        result = "".join(data)
        
        print("dumping {} bytes".format(sys.getsizeof(result)))
        with open("result.txt", "w+") as f:
            f.write("".join(data))
        print("dumped")

        