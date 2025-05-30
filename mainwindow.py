# mainwindow.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from ui_form import Ui_MainWindow

# Page Controllers
from controllers.startPageController import StartPageController
from controllers.loginPageController import LoginPageController
from controllers.dashboardPageController import DashboardPageController
from controllers.bookManagementPageController import BookManagementPageController
from controllers.userManagementPageController import UserManagementPageController
from controllers.bookLendHistoryPageController import BookLendHistoryPageController


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Reference to stacked widget and pages
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.startPage = self.findChild(QWidget, "startPage")
        self.loginPage = self.findChild(QWidget, "loginPage")
        self.mainPage = self.findChild(QWidget, "mainPage")
        self.bookManagementPage = self.findChild(QWidget, "bookManagementPage")
        self.userManagementPage = self.findChild(QWidget, "userManagementPage")
        self.bookLendHistoryPage = self.findChild(QWidget, "bookLendHistoryPage")

        # Controllers
        self.startPageController = StartPageController(self)
        self.loginPageController = LoginPageController(self)
        self.dashboardPageController = DashboardPageController(self)
        self.bookManagementPageController = BookManagementPageController(self)
        self.userManagementPageController = UserManagementPageController(self)
        self.bookLendHistoryPageController = BookLendHistoryPageController(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())