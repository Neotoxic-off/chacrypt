import os

class Message:
    def __init__(self, path: str):
        self.path = path
        self.message = None

        self.__load__()

    def __load__(self):
        if (os.path.exists(self.path) == True):
            with open(self.path, 'r') as f:
                self.message = f.read().splitlines()
