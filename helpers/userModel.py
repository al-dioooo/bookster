from fileHelper import JsonFileHelper


class UserModel:
    def __init__(self, jsonPath="data/users.json"):
        self.file = JsonFileHelper(jsonPath)
        self.users = []
        self.load()

    def load(self):
        data = self.file.read()
        # If empty JSON object {}, convert to empty list []
        self.users = data if isinstance(data, list) else []

    def save(self):
        self.file.write(self.users)

    def getAll(self):
        return self.users

    def getById(self, userId):
        return next((user for user in self.users if user["id"] == userId), None)

    def add(self, userData):
        userData["id"] = self._generateId()
        self.users.append(userData)
        self.save()
        return userData

    def update(self, userId, newData):
        for user in self.users:
            if user["id"] == userId:
                user.update(newData)
                self.save()
                return user
        return None

    def delete(self, userId):
        originalLen = len(self.users)
        self.users = [user for user in self.users if user["id"] != userId]
        if len(self.users) < originalLen:
            self.save()
            return True
        return False

    def _generateId(self):
        existing_ids = [user.get("id", 0) for user in self.users]
        return max(existing_ids, default=0) + 1
