# This Python file uses the following encoding: utf-8
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
from PySide6.QtCore import QSize, Qt
from helpers.authManager import AuthManager
from customWidgets.listView import ListView
from customWidgets.bookListItem import BookListItem
from customWidgets.bookCardList import BookCardList

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Access elements from the UI
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        # Pages
        self.startPage = self.findChild(QWidget, "startPage")
        self.mainPage = self.findChild(QWidget, "mainPage")
        self.loginPage = self.findChild(QWidget, "loginPage")
        self.bookManagementPage = self.findChild(QWidget, "bookManagementPage")
        self.userManagementPage = self.findChild(QWidget, "userManagementPage")

        # Set the initial page
        # self.stackedWidget.setCurrentWidget(self.startPage)

        # Start page
        self.stack = self.findChild(QStackedWidget, "stackedWidget")
        self.mainButton = self.findChild(QPushButton, "mainButton")
        self.loginButton = self.findChild(QPushButton, "loginButton")
        # Connect signals
        self.mainButton.clicked.connect(self.goToMainPage)
        self.loginButton.clicked.connect(self.goToLoginPage)

        # Login page
        self.usernameInput = self.findChild(QLineEdit, "usernameInput")
        self.passwordInput = self.findChild(QLineEdit, "passwordInput")
        self.submitLoginButton = self.findChild(QPushButton, "submitLoginButton")
        self.submitLoginButton.clicked.connect(self.auth)

        # Main page
        self.greetingsLabel = self.findChild(QLabel, "greetingsLabel")
        self.roleLabel = self.findChild(QLabel, "roleLabel")
        self.bookManagementLinkButton = self.findChild(QToolButton, "bookManagementLinkButton")
        self.userManagementLinkButton = self.findChild(QToolButton, "userManagementLinkButton")
        self.historyLinkButton = self.findChild(QToolButton, "historyLinkButton")
        self.mainLogoutButton = self.findChild(QToolButton, "mainLogoutButton")
        bookIcon = QIcon("assets/icons/book.svg")
        self.bookManagementLinkButton.setIcon(bookIcon)
        self.bookManagementLinkButton.setIconSize(QSize(64, 64))
        userIcon = QIcon("assets/icons/user.svg")
        self.userManagementLinkButton.setIcon(userIcon)
        self.userManagementLinkButton.setIconSize(QSize(64, 64))
        historyIcon = QIcon("assets/icons/exchange.svg")
        self.historyLinkButton.setIcon(historyIcon)
        self.historyLinkButton.setIconSize(QSize(64, 64))
        logoutIcon = QIcon("assets/icons/logout.svg")
        self.mainLogoutButton.setIcon(logoutIcon)
        self.mainLogoutButton.setIconSize(QSize(20, 20))
        # self.bookManagementLinkButton.setStyleSheet("QPushButton { background-color: transparent; }")
        # self.userManagementLinkButton.setStyleSheet("QPushButton { background-color: transparent; }")
        # self.historyLinkButton.setStyleSheet("QPushButton { background-color: transparent; }")
        # Connect signals
        self.bookManagementLinkButton.clicked.connect(self.goToBookManagementPage)
        self.userManagementLinkButton.clicked.connect(self.goToUserManagementPage)
        self.historyLinkButton.clicked.connect(self.goToMainPage)
        self.mainLogoutButton.clicked.connect(self.logoutAction)

        # Book management page
        self.bookListScrollArea = self.findChild(QWidget, "bookListScrollArea")
        self.bookListScrollContent = self.bookListScrollArea.widget()
        self.bookListScrollLayout = self.bookListScrollContent.layout()
        self.searchBookInput = self.findChild(QLineEdit, "searchBookInput")
        self.addBookButton = self.findChild(QToolButton, "addBookButton")
        plusIcon = QIcon("assets/icons/plus.svg")
        self.addBookButton.setIcon(plusIcon)
        self.addBookButton.setIconSize(QSize(20, 20))
        self.bookManagementBackButton = self.findChild(QToolButton, "bookManagementBackButton")
        backIcon = QIcon("assets/icons/arrow-narrow-left.svg")
        self.bookManagementBackButton.setIcon(backIcon)
        self.bookManagementBackButton.setIconSize(QSize(20, 20))

        self.books = [
            {"name": "Bumi Manusia", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Matahari", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Langit", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Bulan", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Laut Bercerita", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Pulang", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Bumi", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Cantik itu Luka", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Laskar Pelangi", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"name": "Perjalanan Menuju Pulang", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
        ]

        self.searchBookInput.textChanged.connect(self.onSearchBookInputChanged)
        self.populateBookList(self.books)

        # User management page
        self.userListScrollArea = self.findChild(QWidget, "userListScrollArea")
        self.userListScrollContent = self.userListScrollArea.widget()
        self.userListScrollLayout = self.userListScrollContent.layout()
        self.searchUserInput = self.findChild(QLineEdit, "searchUserInput")
        self.addUserButton = self.findChild(QToolButton, "addUserButton")
        plusIcon = QIcon("assets/icons/plus.svg")
        self.addUserButton.setIcon(plusIcon)
        self.addUserButton.setIconSize(QSize(20, 20))

        self.users = [
            {"name": "Alice Evergarden", "role": "Administrator"},
            {"name": "Aldio Lisafron", "role": "Librarian"},
            {"name": "Arisu", "role": "User"}
        ]

        self.searchUserInput.textChanged.connect(self.onSearchUserInputChanged)
        self.populateUserList(self.users)



        ## Debug, uncomment if need to print page names
        # print("mainPage:", self.mainPage)
        # for i in range(self.stackedWidget.count()):
        #     page = self.stackedWidget.widget(i)
        #     print(f"Page {i}: objectName = {page.objectName()}")

    def goToMainPage(self):
        self.stackedWidget.setCurrentWidget(self.mainPage)

    def goToLoginPage(self):
        self.stackedWidget.setCurrentWidget(self.loginPage)

    def goToBookManagementPage(self):
        self.setWindowTitle("Bookster - Book Management")

        self.stackedWidget.setCurrentWidget(self.bookManagementPage)

    def goToUserManagementPage(self):
        self.stackedWidget.setCurrentWidget(self.userManagementPage)

    def auth(self):
        print("Authentication process started")

        username = self.usernameInput.text()
        password = self.passwordInput.text()
        self.authManager = AuthManager("data/users.json", "data/session.json")

        self.authManager.authenticate(username, password)

        user = self.authManager.getLoggedInUser()

        if user:
            # For debug purpose only
            print("Authentication successful")
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Role: {user['role']}")
            print(f"User ID: {user['id']}")

            print("Authentication process finished")

            self.greetingsLabel.setText(f"Welcome {user['name']}!")
            self.roleLabel.setText(user['role'].capitalize())

            # Switch to main page
            self.stackedWidget.setCurrentWidget(self.mainPage)
        else:
            print("Authentication failed")
            # Optionally, show an error message to the user
            # self.errorLabel.setText("Invalid username or password")
            # self.errorLabel.show()
        # Clear the input fields
        self.usernameInput.clear()
        self.passwordInput.clear()
        # Optionally, hide the error message
        # self.errorLabel.hide()

    def onSearchBookInputChanged(self, text):
        # Case-insensitive filter
        filteredData = [
            book for book in self.books
            if text.lower() in book["name"].lower() or text.lower() in book["description"].lower()
        ]
        self.populateBookList(filteredData)

    def populateBookList(self, data):
        # Clear old widgets (optional if reloading)
        while self.bookListScrollLayout.count():
            child = self.bookListScrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add book cards
        for book in data:
            card = BookCardList(book["name"], book["description"])
            self.bookListScrollLayout.addWidget(card)

        # Add stretch at the end to push items to top
        self.bookListScrollLayout.addStretch()

    def onSearchUserInputChanged(self, text):
        # Case-insensitive filter
        filteredData = [
            user for user in self.users
            if text.lower() in user["name"].lower() or text.lower() in user["role"].lower()
        ]
        self.populateUserList(filteredData)

    def populateUserList(self, data):
        # Clear old widgets (optional if reloading)
        while self.userListScrollLayout.count():
            child = self.userListScrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add user cards
        for user in data:
            card = BookCardList(user["name"], user["role"])
            self.userListScrollLayout.addWidget(card)

        # Add stretch at the end to push items to top
        self.userListScrollLayout.addStretch()

    def logoutAction(self):
        # Clear session data
        self.authManager.logout()

        # Switch to login page
        self.stackedWidget.setCurrentWidget(self.startPage)

        # Clear the main page labels
        self.greetingsLabel.clear()
        self.roleLabel.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
