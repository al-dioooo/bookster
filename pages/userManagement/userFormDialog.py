# pages/userManagement/userFormDialog.py
from __future__ import annotations

from PySide6.QtWidgets import QDialog, QMessageBox
from pages.userManagement.ui_form import Ui_UserFormDialog


class UserFormDialog(QDialog, Ui_UserFormDialog):
    """
    Create / Edit User dialog.

    Parameters
    ----------
    user           : existing record (None = create)
    hideRoleField  : True → hide the Role label & combo, force role='member'
    allowed_roles  : list[str] for the role combo (ignored if hideRoleField)
    """

    # ------------------------------------------------------------------
    def __init__(
        self,
        parent=None,
        user: dict | None = None,
        *,
        hideRoleField: bool = False,
        allowed_roles: list[str] | None = None,
    ):
        super().__init__(parent)
        self.user = user or {}
        self.hideRoleField = hideRoleField
        self.allowed_roles = allowed_roles or ["Administrator", "Librarian", "Member"]

        self.setupUI()
        self.connectSignals()

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------
    def setupUI(self):
        self.setupUi(self)  # widgets generated from .ui file

        # Role field handling -------------------------------------------------
        if self.hideRoleField:
            # hide both label and combo-box explicitly
            getattr(self, "label_4").setVisible(False)  # role label
            self.roleCombo.setVisible(False)
        else:
            self.roleCombo.clear()
            self.roleCombo.addItems(self.allowed_roles)

        # Editing mode -------------------------------------------------------
        if self.user:
            self.setWindowTitle("Edit User")
            self.dlgTitle.setText("Edit User")
            self.nameInput.setText(self.user["name"])
            self.usernameInput.setText(self.user["username"])
            # leave password blank for security
            self.roleCombo.setCurrentText(self.user.get("role", "member").capitalize())

    # ------------------------------------------------------------------
    # Signals
    # ------------------------------------------------------------------
    def connectSignals(self):
        self.saveUserButton.clicked.connect(self._validateAndAccept)
        self.cancelUserButton.clicked.connect(self.reject)

    # ------------------------------------------------------------------
    # validation
    # ------------------------------------------------------------------
    def _validateAndAccept(self):
        if not self.nameInput.text().strip():
            QMessageBox.warning(self, "Warning", "Name is required")
            return
        if not self.usernameInput.text().strip():
            QMessageBox.warning(self, "Warning", "Username is required")
            return
        if not self.user and not self.passwordInput.text():
            QMessageBox.warning(self, "Warning", "Password is required")
            return
        self.accept()

    # ------------------------------------------------------------------
    # expose data
    # ------------------------------------------------------------------
    def data(self) -> dict:
        role_value = (
            "member" if self.hideRoleField else self.roleCombo.currentText().lower()
        )

        record = dict(self.user)  # keep id when editing
        record.update(
            name=self.nameInput.text().strip(),
            username=self.usernameInput.text().strip(),
            password=self.passwordInput.text() or self.user.get("password", ""),
            role=role_value,
        )
        return record
