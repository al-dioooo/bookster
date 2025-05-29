from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QToolButton,
    QSpacerItem,
    QSizePolicy,
)


class BookListItem(QWidget):
    """
    Kartu buku satu baris + tombol Edit & Delete.
    Emit:
        editRequested(dict book)
        deleteRequested(dict book)
    """

    editRequested = Signal(dict)
    deleteRequested = Signal(dict)

    def __init__(self, book: dict, parent=None):
        super().__init__(parent)
        self.book = book
        self.setupUI()
        self.connectSignals()

    # ---------- UI ----------
    def setupUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)

        # judul + penulis
        lblTitle = QLabel(self.book["title"])
        font = QFont("Poppins", 12, QFont.Bold)
        lblTitle.setFont(font)

        lblAuthor = QLabel(f'by {self.book["author"]}')
        lblAuthor.setStyleSheet("color: gray")

        vboxInfo = QWidget()
        vLayout = QHBoxLayout(vboxInfo)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.addWidget(lblTitle)
        vLayout.addWidget(lblAuthor)

        # spacer
        spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # tombol Edit
        self.btnEdit = QToolButton()
        self.btnEdit.setIcon(QIcon("assets/icons/edit.svg"))
        self.btnEdit.setToolTip("Edit book")
        self.btnEdit.setCursor(Qt.PointingHandCursor)

        # tombol Delete
        self.btnDelete = QToolButton()
        self.btnDelete.setIcon(QIcon("assets/icons/trash.svg"))
        self.btnDelete.setToolTip("Delete book")
        self.btnDelete.setCursor(Qt.PointingHandCursor)

        # urutkan
        layout.addWidget(vboxInfo)
        layout.addItem(spacer)
        layout.addWidget(self.btnEdit)
        layout.addWidget(self.btnDelete)

    # ---------- Signals ----------
    def connectSignals(self):
        self.btnEdit.clicked.connect(lambda: self.editRequested.emit(self.book))
        self.btnDelete.clicked.connect(lambda: self.deleteRequested.emit(self.book))
