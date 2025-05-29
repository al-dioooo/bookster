from helpers.fileHelper import JsonFileHelper


class DataReader:
    def __init__(self, jsonPath="data/books.json"):
        self.fileHelper = JsonFileHelper(jsonPath)
        self.data = self._loadData()

    def _loadData(self):
        data = self.fileHelper.read()
        return data if isinstance(data, list) else []

    def saveData(self):
        self.fileHelper.write(self.data)

    def addItem(self, item):
        self.data.append(item)
        self.saveData()

    def get(self):
        return self.data

    def clearData(self):
        self.data = []
        self.saveData()
