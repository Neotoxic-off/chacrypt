from src.rotor import Rotor
from src.message import Message

class Core:
    def __init__(self):
        self.rotors = [
            Rotor("r0"),
            Rotor("r1"),
            Rotor("r2")
        ]

        self.message = Message("message.txt")

        self.run()

    def run(self):
        for line in self.message.message:
            print(f"{line} => {self.__encrypt__(line)}")

    def __encrypt__(self, line: str):
        sentense = []
        selection = 0

        for index, character in enumerate(line):
            sentense.append(self.rotors[selection].get(character))
            selection += 1

            if (selection >= len(self.rotors)):
                selection = 0

        return ("".join(sentense))