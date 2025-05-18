# userManagement.py
from PySide6.QtWidgets import QWidget, QLineEdit, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from customWidgets.bookCardList import BookCardList


class UserManagementPageController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.users = [
            {"name": "Alice Evergarden", "role": "Administrator"},
            {"name": "Aldio Lisafron", "role": "Librarian"},
            {"name": "Arisu", "role": "User"},
        ]

        self.setupUi()
        self.connectSignals()
        self.populateUserList(self.users)

    def setupUi(self):
        self.userListScrollArea = self.getUserListScrollArea()
        self.userListScrollContent = self.userListScrollArea.widget()
        self.userListScrollLayout = self.userListScrollContent.layout()
        self.searchUserInput = self.getSearchUserInput()
        self.addUserButton = self.getAddUserButton()

        plusIcon = QIcon("assets/icons/plus.svg")
        self.addUserButton.setIcon(plusIcon)
        self.addUserButton.setIconSize(QSize(20, 20))

    def connectSignals(self):
        self.searchUserInput.textChanged.connect(self.onSearchUserInputChanged)

    def getUserListScrollArea(self):
        return self.mainWindow.findChild(QWidget, "userListScrollArea")

    def getSearchUserInput(self):
        return self.mainWindow.findChild(QLineEdit, "searchUserInput")

    def getAddUserButton(self):
        return self.mainWindow.findChild(QToolButton, "addUserButton")

    def onSearchUserInputChanged(self, text):
        filteredUsers = [
            user
            for user in self.users
            if text.lower() in user["name"].lower()
            or text.lower() in user["role"].lower()
        ]
        self.populateUserList(filteredUsers)

    def populateUserList(self, users):
        while self.userListScrollLayout.count():
            child = self.userListScrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for user in users:
            card = BookCardList(user["name"], user["role"])
            self.userListScrollLayout.addWidget(card)

        self.userListScrollLayout.addStretch()
