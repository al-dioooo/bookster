# controllers/userManagementPageController.py
from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QToolButton, QMessageBox

from helpers.userModel import UserModel
from helpers.authManager import AuthManager
from pages.userManagement.userFormDialog import UserFormDialog
from pages.userManagement.userListItem import UserListItem


class UserManagementPageController:
    """Page controller for User CRUD (mirrors book page pattern)."""

    # ------------------------------------------------------------------
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.userModel = UserModel("data/users.json")
        self.authManager = AuthManager()
        self.users = self.userModel.all()

        self.setupUI()
        self.connectSignals()
        self.populateList(self.users)

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------
    def setupUI(self):
        self.listArea = self._f(QWidget, "userListScrollArea")
        self.listLayout = self.listArea.widget().layout()
        self.searchBox = self._f(QLineEdit, "searchUserInput")
        self.addBtn = self._f(QToolButton, "addUserButton")
        self.backButton = self._f(QToolButton, "userManagementBackButton")
        self.pageDescription = self._f(QWidget, "userPageDescription")

        self.addBtn.setIcon(QIcon("assets/icons/plus.svg"))
        self.addBtn.setIconSize(QSize(20, 20))
        self.backButton.setIcon(QIcon("assets/icons/arrow-narrow-left.svg"))
        self.backButton.setIconSize(QSize(20, 20))

    # ------------------------------------------------------------------
    # Signals
    # ------------------------------------------------------------------
    def connectSignals(self):
        self.searchBox.textChanged.connect(self.onSearch)
        self.backButton.clicked.connect(self._goBack)
        self.addBtn.clicked.connect(self.createUser)

    def _goBack(self):
        self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)
        self.mainWindow.setWindowTitle("Bookster - Dashboard")

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def _f(self, typ, name):
        return self.mainWindow.findChild(typ, name)

    # ------------------------------------------------------------------
    # listing / search
    # ------------------------------------------------------------------
    def onSearch(self, txt: str):
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

        n = len(users)
        self.pageDescription.setText(
            "No User Available"
            if n == 0
            else "1 User Available" if n == 1 else f"{n} Users Available"
        )

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------
    def _is_librarian(self) -> bool:
        return self.authManager.getLoggedInUser().get("role") == "librarian"

    # -------- CREATE --------
    def createUser(self):
        librarian_mode = self._is_librarian()

        dlg = UserFormDialog(
            self.mainWindow,
            hideRoleField=librarian_mode,  # hide role combo for librarians
        )
        if not dlg.exec():
            return

        data = dlg.data()
        data["id"] = self.userModel.next_id()

        # enforce member role if librarian
        if librarian_mode:
            data["role"] = "member"

        try:
            self.userModel.upsert(data)
        except ValueError as e:
            QMessageBox.warning(self.mainWindow, "", str(e))
            return

        self.users = self.userModel.all()
        self.populateList(self.users)

    # -------- EDIT --------
    def editUser(self, user: dict):
        librarian_mode = self._is_librarian()

        dlg = UserFormDialog(self.mainWindow, user=user, hideRoleField=librarian_mode)
        if not dlg.exec():
            return

        data = dlg.data()
        # ensure librarians cannot elevate roles while editing
        if librarian_mode:
            data["role"] = user.get("role", "member")

        self.userModel.upsert(data)
        self.users = self.userModel.all()
        self.populateList(self.users)

    # -------- DELETE --------
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
