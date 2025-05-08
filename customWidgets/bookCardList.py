# user_card.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont


class BookCardList(QWidget):
    def __init__(self, name, role, parent=None):
        super().__init__(parent)

        self.name = name
        self.role = role

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        # layout.setContentsMargins(12, 12, 1, 0)

        # Title (name)
        title = QLabel(self.name)
        titleFont = QFont()
        titleFont.setPointSize(16)
        titleFont.setFamilies([u"Poppins"])
        title.setFont(titleFont)

        # Subtitle (role)
        subtitle = QLabel(self.role)
        subtitle.setStyleSheet("color: gray")
        subtitleFont = QFont()
        subtitleFont.setPointSize(14)
        subtitleFont.setFamilies([u"Poppins"])

        layout.addWidget(title)
        layout.addWidget(subtitle)
