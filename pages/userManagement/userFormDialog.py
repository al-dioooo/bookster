from PySide6.QtWidgets import QDialog, QMessageBox
from pages.userManagement.ui_form import Ui_UserFormDialog


class UserFormDialog(QDialog, Ui_UserFormDialog):
    """
    Dialog Create / Edit User — styled & wired like BookFormDialog
    """

    def __init__(self, parent=None, user: dict | None = None):
        super().__init__(parent)
        self.user = user or {}
        self.setupUI()
        self.connectSignals()

    # ---------- UI ----------
    def setupUI(self):
        self.setupUi(self)           # Qt-Designer widgets
        if self.user:
            self.setWindowTitle("Edit User")
            self.dlgTitle.setText("Edit User")
            self.nameInput.setText(self.user["name"])
            self.usernameInput.setText(self.user["username"])
            self.passwordInput.setText(self.user["password"])
            self.roleCombo.setCurrentText(self.user["role"])

    # ---------- Signals ----------
    def connectSignals(self):
        self.saveUserButton.clicked.connect(self._validateAndAccept)
        self.cancelUserButton.clicked.connect(self.reject)

    # ---------- helpers ----------
    def _validateAndAccept(self):
        if not self.nameInput.text().strip():
            QMessageBox.warning(self, "Warning", "Name is required"); return
        if not self.usernameInput.text().strip():
            QMessageBox.warning(self, "Warning", "Username is required"); return
        if not self.user and not self.passwordInput.text():
            QMessageBox.warning(self, "Warning", "Password is required"); return
        self.accept()

    def data(self) -> dict:
        d = dict(self.user)  # keep id if editing
        d.update(
            name=self.nameInput.text().strip(),
            username=self.usernameInput.text().strip(),
            password=self.passwordInput.text() or self.user.get("password", ""),
            role=self.roleCombo.currentText(),
        )
        return d
