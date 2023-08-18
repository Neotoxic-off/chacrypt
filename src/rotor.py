from src.config import Config

class Rotor:
    def __init__(self, name):
        self.config = Config(f"configuration/{name}.json")
        self.minimum = 32
        self.maximum = 126
        self.rotation = self.config.config["default"]

    def get(self, character):
        return (self.__rotate__(character))

    def __rotate__(self, character):
        if ((self.minimum + self.rotation) > self.maximum):
            self.rotation = self.minimum
        else:
            self.rotation += 1

        return (chr(self.minimum + self.rotation))
