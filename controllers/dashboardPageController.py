from PySide6.QtWidgets import QLabel, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class DashboardPageController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self._setupUi()
        self._connectSignals()

    def _find(self, widgetType, name):
        return self.mainWindow.findChild(widgetType, name)

    def _setupUi(self):
        self.greetingsLabel = self._find(QLabel, "greetingsLabel")
        self.roleLabel = self._find(QLabel, "roleLabel")
        self.bookManagementLinkButton = self._find(
            QToolButton, "bookManagementLinkButton"
        )
        self.userManagementLinkButton = self._find(
            QToolButton, "userManagementLinkButton"
        )
        self.bookLendHistoryLinkButton = self._find(QToolButton, "bookLendHistoryLinkButton")
        self.mainLogoutButton = self._find(QToolButton, "mainLogoutButton")

        self.bookManagementLinkButton.setIcon(QIcon("assets/icons/book.svg"))
        self.bookManagementLinkButton.setIconSize(QSize(64, 64))
        self.userManagementLinkButton.setIcon(QIcon("assets/icons/user.svg"))
        self.userManagementLinkButton.setIconSize(QSize(64, 64))
        self.bookLendHistoryLinkButton.setIcon(QIcon("assets/icons/exchange.svg"))
        self.bookLendHistoryLinkButton.setIconSize(QSize(64, 64))
        self.mainLogoutButton.setIcon(QIcon("assets/icons/logout.svg"))
        self.mainLogoutButton.setIconSize(QSize(20, 20))

    def _connectSignals(self):
        self.bookManagementLinkButton.clicked.connect(self.goToBookManagementPage)
        self.userManagementLinkButton.clicked.connect(self.goToUserManagementPage)
        self.bookLendHistoryLinkButton.clicked.connect(self.goToBookLendHistoryPage)
        self.mainLogoutButton.clicked.connect(self.logout)

    def updateUserInfo(self, user):
        self.greetingsLabel.setText(f"Welcome {user['name']}!")
        self.roleLabel.setText(user["role"].capitalize())

    def clearUserInfo(self):
        self.greetingsLabel.clear()
        self.roleLabel.clear()

    def goToMainPage(self):
        self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)

    def goToBookManagementPage(self):
        self.mainWindow.setWindowTitle("Bookster - Book Management")
        self.mainWindow.stackedWidget.setCurrentWidget(
            self.mainWindow.bookManagementPage
        )

    def goToUserManagementPage(self):
        self.mainWindow.setWindowTitle("Bookster - User Management")
        self.mainWindow.stackedWidget.setCurrentWidget(
            self.mainWindow.userManagementPage
        )

    def goToBookLendHistoryPage(self):
        self.mainWindow.setWindowTitle("Bookster - Book Lend History")
        self.mainWindow.stackedWidget.setCurrentWidget(
            self.mainWindow.bookLendHistoryPage
        )

    def logout(self):
        self.mainWindow.authManager.logout()
        self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.startPage)
        self.clearUserInfo()
