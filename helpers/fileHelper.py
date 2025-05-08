import json
import os


class JsonFileHelper:
    def __init__(self, filePath):
        self.filePath = os.path.abspath(filePath)
        self._ensureFileExists()

    def _ensureFileExists(self):
        if not os.path.exists(self.filePath):
            with open(self.filePath, "w") as file:
                json.dump({}, file)

    def read(self):
        with open(self.filePath, "r") as file:
            return json.load(file)

    def write(self, data):
        with open(self.filePath, "w") as file:
            json.dump(data, file, indent=4)
