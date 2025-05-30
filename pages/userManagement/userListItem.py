from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QToolButton,
    QSpacerItem,
    QSizePolicy,
)


class UserListItem(QWidget):
    editRequested = Signal(dict)
    deleteRequested = Signal(dict)

    def __init__(self, user: dict, parent=None):
        super().__init__(parent)
        self.user = user
        self.setupUI()
        self.connectSignals()

    # ---------- UI ----------
    def setupUI(self):
        lay = QHBoxLayout(self)
        lay.setContentsMargins(8, 4, 8, 4)

        lblName = QLabel(self.user["name"])
        lblName.setFont(QFont("Poppins", 16, QFont.DemiBold))
        lblRole = QLabel(f'({self.user["role"].capitalize()})')
        lblRole.setFont(QFont("Poppins", 12))
        lblRole.setStyleSheet("color: gray")

        info = QWidget()
        infoLay = QHBoxLayout(info)
        infoLay.setContentsMargins(0, 0, 0, 0)
        infoLay.addWidget(lblName)
        infoLay.addWidget(lblRole)

        spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btnEdit = QToolButton()
        self.btnEdit.setIcon(QIcon("assets/icons/edit.svg"))
        self.btnEdit.setIconSize(QSize(16, 16))
        self.btnEdit.setMinimumSize(QSize(36, 36))
        self.btnEdit.setCursor(Qt.PointingHandCursor)
        self.btnEdit.setStyleSheet(
            "QToolButton {background:#93C5FD;color:#FFF;border-radius:12px;"
            "border:3px solid #DBEAFE;padding:3px 3px 3px 6px;}"
            "QToolButton:hover {background:rgba(147,197,253,200);}"
            "QToolButton:pressed {background:rgba(147,197,253,150);}"
        )

        self.btnDelete = QToolButton()
        self.btnDelete.setIcon(QIcon("assets/icons/trash.svg"))
        self.btnDelete.setIconSize(QSize(16, 16))
        self.btnDelete.setMinimumSize(QSize(36, 36))
        self.btnDelete.setCursor(Qt.PointingHandCursor)
        self.btnDelete.setStyleSheet(
            "QToolButton {background:#F87171;color:#FFF;border-radius:12px;"
            "border:3px solid #FEE2E2;padding:3px 3px 3px 6px;}"
            "QToolButton:hover {background:rgba(248,113,113,200);}"
            "QToolButton:pressed {background:rgba(248,113,113,150);}"
        )

        lay.addWidget(info)
        lay.addItem(spacer)
        lay.addWidget(self.btnEdit)
        lay.addWidget(self.btnDelete)

    def connectSignals(self):
        self.btnEdit.clicked.connect(lambda: self.editRequested.emit(self.user))
        self.btnDelete.clicked.connect(lambda: self.deleteRequested.emit(self.user))
