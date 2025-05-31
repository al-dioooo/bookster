# startPageController.py
from PySide6.QtWidgets import QPushButton, QStackedWidget, QWidget


class StartPageController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.setupUi()
        self.connectSignals()

    def setupUi(self):
        self.stackedWidget = self.mainWindow.findChild(QStackedWidget, "stackedWidget")
        # self.mainButton = self.mainWindow.findChild(QPushButton, "mainButton")
        self.loginButton = self.mainWindow.findChild(QPushButton, "loginButton")

    def connectSignals(self):
        # self.mainButton.clicked.connect(self.goToMainPage)
        self.loginButton.clicked.connect(self.goToLoginPage)

    # def goToMainPage(self):
    #     self.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)

    def goToLoginPage(self):
        self.stackedWidget.setCurrentWidget(self.mainWindow.loginPage)
