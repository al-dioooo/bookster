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
    """User CRUD page.  Librarian sees only *member* accounts."""

    pageTitle = "👥 User Management"

    # ------------------------------------------------------------------
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.userModel = UserModel("data/users.json")
        self.authManager = AuthManager()

        self.setupUI()
        self.connectSignals()

        self._reloadUsers()

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
    # signals
    # ------------------------------------------------------------------
    def connectSignals(self):
        self.searchBox.textChanged.connect(self._search)
        self.backButton.clicked.connect(self._goBack)
        self.addBtn.clicked.connect(self._createUser)

    # ------------------------------------------------------------------
    # navigation helpers
    # ------------------------------------------------------------------
    def _goBack(self):
        self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)
        self.mainWindow.setWindowTitle("Bookster - Dashboard")

    def _f(self, typ, name):
        return self.mainWindow.findChild(typ, name)

    # ------------------------------------------------------------------
    # role helper
    # ------------------------------------------------------------------
    def _is_librarian(self) -> bool:
        return self.authManager.getLoggedInUser().get("role") == "librarian"

    # ------------------------------------------------------------------
    # load + role-filter
    # ------------------------------------------------------------------
    def _reloadUsers(self):
        all_users = self.userModel.all()
        self.baseUsers = (
            [u for u in all_users if u["role"] == "member"]
            if self._is_librarian()
            else all_users
        )
        self._populate(self.baseUsers)

    # ------------------------------------------------------------------
    # listing / search
    # ------------------------------------------------------------------
    def _search(self, text: str):
        key = text.lower()
        filtered = [
            u
            for u in self.baseUsers
            if key in u["name"].lower()
            or key in u["role"].lower()
            or key in u["username"].lower()
        ]
        self._populate(filtered)

    def _populate(self, users):
        while self.listLayout.count():
            item = self.listLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for u in users:
            item = UserListItem(u)
            item.editRequested.connect(self._editUser)
            item.deleteRequested.connect(self._deleteUser)
            self.listLayout.addWidget(item)

        self.listLayout.addStretch()

        n = len(users)
        self.pageDescription.setText(
            "No User Available"
            if n == 0
            else "1 User Available" if n == 1 else f"{n} Users Available"
        )

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------
    def _createUser(self):
        librarian_mode = self._is_librarian()

        dlg = UserFormDialog(self.mainWindow, hideRoleField=librarian_mode)
        if not dlg.exec():
            return

        data = dlg.data()
        data["id"] = self.userModel.next_id()
        if librarian_mode:
            data["role"] = "member"

        try:
            self.userModel.upsert(data)
        except ValueError as e:
            QMessageBox.warning(self.mainWindow, "", str(e))
            return

        self._reloadUsers()

    def _editUser(self, user: dict):
        librarian_mode = self._is_librarian()

        dlg = UserFormDialog(self.mainWindow, user=user, hideRoleField=librarian_mode)
        if not dlg.exec():
            return

        data = dlg.data()
        if librarian_mode:
            data["role"] = user.get("role", "member")  # cannot elevate

        self.userModel.upsert(data)
        self._reloadUsers()

    def _deleteUser(self, user: dict):
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
        self._reloadUsers()
