# import hashlib  # Uncomment if using password hashing
from helpers.fileHelper import JsonFileHelper


class AuthManager:
    def __init__(self, userFile="data/users.json", sessionFile="data/session.json"):
        self.fileHelper = JsonFileHelper(userFile)
        self.sessionHelper = JsonFileHelper(sessionFile)
        self.users = self._loadUsers()

    def _loadUsers(self):
        data = self.fileHelper.read()
        # Ensure it's a list, not a dict
        return data if isinstance(data, list) else []

    def _saveUsers(self):
        self.fileHelper.write(self.users)

    # def _hashPassword(self, password):
    #     return hashlib.md5(password.encode()).hexdigest()

    def authenticate(self, username, password):
        # hashed = self._hashPassword(password)
        for user in self.users:
            # if user["username"] == username and user["password"] == hashed:
            if user["username"] == username and user["password"] == password:
                self._saveSession(user)
                return True
        return False

    def registerUser(self, username, password):
        if any(user["username"] == username for user in self.users):
            raise ValueError("Username already exists.")

        # hashed = self._hashPassword(password)
        newUser = {
            "id": self._generateId(),
            "name": username,
            "username": username,
            "password": password,  # or hashed
            "role": "user",
        }
        self.users.append(newUser)
        self._saveUsers()
        self._saveSession(newUser)

    def _generateId(self):
        if not self.users:
            return 1
        return max(user.get("id", 0) for user in self.users) + 1

    def _saveSession(self, userData):
        sessionData = {
            "id": userData["id"],
            "username": userData["username"],
            "name": userData["name"],
            "role": userData["role"],
        }
        self.sessionHelper.write(sessionData)

    def logout(self):
        self.sessionHelper.write({})

    def getLoggedInUser(self):
        return self.sessionHelper.read()
