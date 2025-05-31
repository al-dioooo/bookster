from pathlib import Path
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QToolButton
)

PLACEHOLDER = "assets/images/placeholder.png"
THUMB_SIZE = QSize(75, 100)  # 3 : 4 thumbnail
EYE_ICON = "assets/icons/eye.svg"


class BookListItem(QWidget):
    """
    Row widget with:
      • cover thumbnail (3:4, border-radius)
      • title & author (first line)
      • ISBN & stock count (second line, smaller)
      • Edit / Delete buttons

    Signals:
      editRequested(dict book)
      deleteRequested(dict book)
    """

    detailRequested = Signal(dict)
    editRequested = Signal(dict)
    deleteRequested = Signal(dict)

    def __init__(self, book: dict, *, showCrud: bool, parent=None):
        super().__init__(parent)
        self.book = book
        self._showCrud = showCrud
        self.setupUI()
        self.connectSignals()

    # ---------- UI ------------------------------------------------------
    def setupUI(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(8, 4, 8, 4)
        root.setSpacing(10)

        # ── Cover thumbnail ────────────────────────────────────────────
        coverLabel = QLabel()
        coverLabel.setFixedSize(THUMB_SIZE)
        coverLabel.setAlignment(Qt.AlignCenter)
        coverLabel.setStyleSheet("border:3px solid #F5F5F5;border-radius:12px;")

        cover_path = self.book.get("cover", "")
        pix = (
            QPixmap(cover_path)
            if cover_path and Path(cover_path).exists()
            else QPixmap(PLACEHOLDER)
        )
        coverLabel.setPixmap(
            pix.scaled(
                THUMB_SIZE, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
        )

        # ── Text block ─────────────────────────────────────────────────
        # Fonts
        fTitle = QFont("Poppins", 16, QFont.DemiBold)
        fAuthor = QFont("Poppins", 12)
        fDetail = QFont("Poppins", 11)

        # Line-1: Title + Author
        lblTitle = QLabel(self.book["title"])
        lblTitle.setFont(fTitle)

        lblAuthor = QLabel(f'by {self.book["author"]}')
        lblAuthor.setFont(fAuthor)
        lblAuthor.setStyleSheet("color: gray")

        line1 = QWidget()
        l1 = QHBoxLayout(line1)
        l1.setContentsMargins(0, 0, 0, 0)
        l1.setSpacing(4)
        l1.addWidget(lblTitle)
        l1.addWidget(lblAuthor)

        # Line-2: ISBN + Stock
        isbnText = self.book.get("isbn", "—")
        stockCount = self.book.get("stock", 0)
        lblIsbn = QLabel(f"ISBN: {isbnText}")
        lblIsbn.setFont(fDetail)
        lblIsbn.setStyleSheet("color: #6B7280")  # gray-500

        lblStock = QLabel(f"Stock: {stockCount}")
        lblStock.setFont(fDetail)
        lblStock.setStyleSheet("color: #6B7280")

        line2 = QWidget()
        l2 = QHBoxLayout(line2)
        l2.setContentsMargins(0, 0, 0, 0)
        l2.setSpacing(12)
        l2.addWidget(lblIsbn)
        l2.addWidget(lblStock)

        infoBox = QWidget()
        v = QVBoxLayout(infoBox)
        v.setContentsMargins(0, 0, 0, 0)
        v.setSpacing(2)
        v.addWidget(line1)
        v.addWidget(line2)

        # spacer
        spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # ── Buttons ────────────────────────────────────────────────────
        self.btnDetail = QToolButton()
        self.btnDetail.setIcon(QIcon(EYE_ICON))
        self.btnDetail.setIconSize(QSize(16, 16))
        self.btnDetail.setMinimumSize(QSize(36, 36))
        self.btnDetail.setCursor(Qt.PointingHandCursor)
        self.btnDetail.setToolTip("View details")
        self.btnDetail.setStyleSheet(
            "QToolButton {background:#FCD34D;color:#FFF;border-radius:12px;"
            "border:3px solid #FEF3C7;padding:3px 3px 3px 6px;}"
            "QToolButton:hover {background:rgba(252,211,77,200);}"
            "QToolButton:pressed {background:rgba(252,211,77,150);}"
        )

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

        # ── Assemble root layout ───────────────────────────────────────
        root.addWidget(coverLabel)
        root.addWidget(infoBox)
        root.addItem(spacer)
        root.addWidget(self.btnDetail)
        
        if self._showCrud:
            root.addWidget(self.btnEdit)
            root.addWidget(self.btnDelete)

    # ---------- Signals -------------------------------------------------
    def connectSignals(self):
        self.btnDetail.clicked.connect(lambda: self.detailRequested.emit(self.book))
        
        if hasattr(self, 'btnEdit'):
            self.btnEdit.clicked.connect(lambda: self.editRequested.emit(self.book))
        if hasattr(self, 'btnDelete'):
            self.btnDelete.clicked.connect(lambda: self.deleteRequested.emit(self.book))
