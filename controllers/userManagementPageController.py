from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QToolButton, QMessageBox

from helpers.userModel import UserModel
from pages.userManagement.userFormDialog import UserFormDialog
from pages.userManagement.userListItem import UserListItem


class UserManagementPageController:
    """Page controller for User CRUD (mirrors book page pattern)."""

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.userModel = UserModel("data/users.json")
        self.users = self.userModel.all()

        self.setupUI()
        self.connectSignals()
        self.populateList(self.users)

    # ---------- UI ----------
    def setupUI(self):
        self.listArea = self._f(QWidget, "userListScrollArea")
        self.listLayout = self.listArea.widget().layout()
        self.searchBox = self._f(QLineEdit, "searchUserInput")
        self.addBtn = self._f(QToolButton, "addUserButton")
        self.backButton = self._f(QToolButton, "userManagementBackButton")

        self.addBtn.setIcon(QIcon("assets/icons/plus.svg"))
        self.addBtn.setIconSize(QSize(20, 20))
        self.backButton.setIcon(QIcon("assets/icons/arrow-narrow-left.svg"))
        self.backButton.setIconSize(QSize(20, 20))

    # ---------- Signals ----------
    def connectSignals(self):
        self.searchBox.textChanged.connect(self.onSearch)
        self.backButton.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.mainPage
            )
        )
        self.addBtn.clicked.connect(self.createUser)

    # ---------- helpers ----------
    def _f(self, typ, name):
        return self.mainWindow.findChild(typ, name)

    # ---------- listing ----------
    def onSearch(self, txt):
        key = txt.lower()
        self.populateList(
            [
                u
                for u in self.users
                if key in u["name"].lower()
                or key in u["role"].lower()
                or key in u["username"].lower()
            ]
        )

    def populateList(self, users):
        while self.listLayout.count():
            w = self.listLayout.takeAt(0)
            if w.widget():
                w.widget().deleteLater()

        for u in users:
            item = UserListItem(u)
            item.editRequested.connect(self.editUser)
            item.deleteRequested.connect(self.deleteUser)
            self.listLayout.addWidget(item)

        self.listLayout.addStretch()

    # ---------- CRUD ----------
    def createUser(self):
        dlg = UserFormDialog(self.mainWindow)
        if not dlg.exec():
            return

        data = dlg.data()
        data["id"] = self.userModel.next_id()
        self.userModel.upsert(data)

        self.users = self.userModel.all()
        self.populateList(self.users)

    def editUser(self, user: dict):
        dlg = UserFormDialog(self.mainWindow, user)
        if not dlg.exec():
            return
        self.userModel.upsert(dlg.data())
        self.users = self.userModel.all()
        self.populateList(self.users)

    def deleteUser(self, user: dict):
        if (
            QMessageBox.question(
                self.mainWindow,
                "Confirm",
                f'Delete user "{user["name"]}"?',
                QMessageBox.Yes | QMessageBox.No,
            )
            == QMessageBox.No
        ):
            return
        self.userModel.delete(user["id"])
        self.users = self.userModel.all()
        self.populateList(self.users)
