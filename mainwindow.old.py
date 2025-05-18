import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QLineEdit,
    QPushButton,
    QToolButton,
    QLabel,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from helpers.authManager import AuthManager
from controllers.bookManagement import BookManagementPageController
from customWidgets.bookCardList import BookCardList
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.authManager = AuthManager("data/users.json", "data/session.json")

        self.connectWidgets()
        self.setupIcons()

        # Book Management Controller Setup
        # self.bookManagementPageController = BookManagementPageController(self)

        # Static user data (simulating database response)
        self.users = [
            {"name": "Alice Evergarden", "role": "Administrator"},
            {"name": "Aldio Lisafron", "role": "Librarian"},
            {"name": "Arisu", "role": "User"},
        ]
        self.populateUserList(self.users)

    def connectWidgets(self):
        self.stack = self.findChild(QStackedWidget, "stackedWidget")
        self.startPage = self.findChild(QWidget, "startPage")
        self.mainPage = self.findChild(QWidget, "mainPage")
        self.loginPage = self.findChild(QWidget, "loginPage")
        self.bookManagementPage = self.findChild(QWidget, "bookManagementPage")
        self.userManagementPage = self.findChild(QWidget, "userManagementPage")

        self.mainButton = self.findChild(QPushButton, "mainButton")
        self.loginButton = self.findChild(QPushButton, "loginButton")
        self.mainButton.clicked.connect(self.goToMainPage)
        self.loginButton.clicked.connect(self.goToLoginPage)

        self.usernameInput = self.findChild(QLineEdit, "usernameInput")
        self.passwordInput = self.findChild(QLineEdit, "passwordInput")
        self.submitLoginButton = self.findChild(QPushButton, "submitLoginButton")
        self.submitLoginButton.clicked.connect(self.auth)

        self.greetingsLabel = self.findChild(QLabel, "greetingsLabel")
        self.roleLabel = self.findChild(QLabel, "roleLabel")

        self.bookManagementLinkButton = self.findChild(
            QToolButton, "bookManagementLinkButton"
        )
        self.userManagementLinkButton = self.findChild(
            QToolButton, "userManagementLinkButton"
        )
        self.historyLinkButton = self.findChild(QToolButton, "historyLinkButton")
        self.mainLogoutButton = self.findChild(QToolButton, "mainLogoutButton")

        self.bookManagementLinkButton.clicked.connect(self.goToBookManagementPage)
        self.userManagementLinkButton.clicked.connect(self.goToUserManagementPage)
        self.historyLinkButton.clicked.connect(self.goToMainPage)
        self.mainLogoutButton.clicked.connect(self.logoutAction)

        self.userListScrollArea = self.findChild(QWidget, "userListScrollArea")
        self.userListScrollContent = self.userListScrollArea.widget()
        self.userListScrollLayout = self.userListScrollContent.layout()
        self.searchUserInput = self.findChild(QLineEdit, "searchUserInput")
        self.searchUserInput.textChanged.connect(self.onSearchUserInputChanged)
        self.addUserButton = self.findChild(QToolButton, "addUserButton")

    def setupIcons(self):
        icons = {
            self.bookManagementLinkButton: ("assets/icons/book.svg", QSize(64, 64)),
            self.userManagementLinkButton: ("assets/icons/user.svg", QSize(64, 64)),
            self.historyLinkButton: ("assets/icons/exchange.svg", QSize(64, 64)),
            self.mainLogoutButton: ("assets/icons/logout.svg", QSize(20, 20)),
            self.addUserButton: ("assets/icons/plus.svg", QSize(20, 20)),
        }

        for btn, (icon_path, size) in icons.items():
            if btn:
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(size)

    def goToMainPage(self):
        self.stack.setCurrentWidget(self.mainPage)

    def goToLoginPage(self):
        self.stack.setCurrentWidget(self.loginPage)

    def goToBookManagementPage(self):
        self.setWindowTitle("Bookster - Book Management")
        self.stack.setCurrentWidget(self.bookManagementPage)

    def goToUserManagementPage(self):
        self.stack.setCurrentWidget(self.userManagementPage)

    def auth(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        self.authManager.authenticate(username, password)
        user = self.authManager.getLoggedInUser()

        if user:
            self.greetingsLabel.setText(f"Welcome {user['name']}!")
            self.roleLabel.setText(user["role"].capitalize())
            self.stack.setCurrentWidget(self.mainPage)
        else:
            print("Authentication failed")

        self.usernameInput.clear()
        self.passwordInput.clear()

    def onSearchUserInputChanged(self, text):
        filteredData = [
            user
            for user in self.users
            if text.lower() in user["name"].lower()
            or text.lower() in user["role"].lower()
        ]
        self.populateUserList(filteredData)

    def populateUserList(self, data):
        while self.userListScrollLayout.count():
            child = self.userListScrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for user in data:
            card = BookCardList(user["name"], user["role"])
            self.userListScrollLayout.addWidget(card)

        self.userListScrollLayout.addStretch()

    def logoutAction(self):
        self.authManager.logout()
        self.stack.setCurrentWidget(self.startPage)
        self.greetingsLabel.clear()
        self.roleLabel.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())