from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt


class BookListItem(QWidget):
    def __init__(self, book: dict, parent=None):
        super().__init__(parent)
        self.book = book
        self.layout = QVBoxLayout(self)
        self.labelTitle = QLabel(self.book["title"])
        self.labelAuthor = QLabel(self.book["author"])
        self.buttonDetails = QToolButton()
        self.buttonDetails.setText("Details")

        # Add widgets to layout
        self.layout.addWidget(self.labelTitle)
        self.layout.addWidget(self.labelAuthor)
        self.layout.addWidget(self.buttonDetails)

        # Set layout
        self.setLayout(self.layout)
        # self.buttonDetails.clicked.connect(self.showDetails)
        self.buttonDetails.setStyleSheet("background-color: lightblue;")
        self.buttonDetails.setFixedSize(100, 30)
        self.buttonDetails.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.buttonDetails.setIconSize(QSize(16, 16))
        self.buttonDetails.setIcon(QIcon("assets/icons/details.svg"))
        self.buttonDetails.setAutoRaise(True)
        self.buttonDetails.setStyleSheet("QToolButton { background-color: lightblue; }")
        self.buttonDetails.setCursor(Qt.PointingHandCursor)
