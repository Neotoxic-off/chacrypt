import os
import json

class Config:
    def __init__(self, path: str):
        self.path = path
        self.config = None

        self.__load__()

    def __load__(self):
        if (os.path.exists(self.path) == True):
            with open(self.path, 'r') as f:
                self.config = json.load(f)
