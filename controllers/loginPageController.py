# loginPageController.py
from PySide6.QtWidgets import QLineEdit, QPushButton, QLabel, QStackedWidget
from helpers.authManager import AuthManager


class LoginPageController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.setupUi()
        self.connectSignals()

    def setupUi(self):
        self.usernameInput = self.mainWindow.findChild(QLineEdit, "usernameInput")
        self.passwordInput = self.mainWindow.findChild(QLineEdit, "passwordInput")
        self.submitLoginButton = self.mainWindow.findChild(
            QPushButton, "submitLoginButton"
        )
        self.greetingsLabel = self.mainWindow.findChild(QLabel, "greetingsLabel")
        self.roleLabel = self.mainWindow.findChild(QLabel, "roleLabel")
        self.stackedWidget = self.mainWindow.findChild(QStackedWidget, "stackedWidget")

    def connectSignals(self):
        self.submitLoginButton.clicked.connect(self.auth)

    def auth(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        self.authManager = AuthManager("data/users.json", "data/session.json")
        self.authManager.authenticate(username, password)

        user = self.authManager.getLoggedInUser()

        if user:
            self.greetingsLabel.setText(f"Welcome {user['name']}!")
            self.roleLabel.setText(user["role"].capitalize())
            self.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)
        else:
            print("Authentication failed")

        self.usernameInput.clear()
        self.passwordInput.clear()
