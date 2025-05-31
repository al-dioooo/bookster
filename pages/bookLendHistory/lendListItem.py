from pathlib import Path
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QToolButton,
)

PLACEHOLDER = "assets/images/placeholder.png"
THUMB = QSize(75, 100)


class LendListItem(QWidget):
    """
    Row widget for a lend record.

    Signals
    -------
    returnRequested(dict lend_record)
    """

    returnRequested = Signal(dict)

    def __init__(self, rec: dict, *, showReturn: bool, parent=None):
        super().__init__(parent)
        self.rec = rec
        self._showReturn = showReturn
        self.setupUI()
        self.connectSignals()

    # ---------- UI ----------
    def setupUI(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(8, 4, 8, 4)
        root.setSpacing(10)

        # Thumbnail
        cover = QLabel()
        cover.setFixedSize(THUMB)
        cover.setStyleSheet("border:3px solid #F5F5F5;border-radius:12px;")
        path = self.rec.get("cover") or PLACEHOLDER
        cover.setPixmap(
            QPixmap(path).scaled(
                THUMB, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
        )
        root.addWidget(cover)

        # Text Block
        vbox = QVBoxLayout()
        vbox.setSpacing(1)
        fBig = QFont("Poppins", 16, QFont.DemiBold)
        fSmall = QFont("Poppins", 12)

        vbox.addWidget(self._lbl(self.rec["title"], fBig))
        vbox.addWidget(
            self._lbl(f'ISBN {self.rec["isbn"]} • SKU {self.rec["sku"]}', fSmall)
        )
        vbox.addWidget(
            self._lbl(
                f'{self.rec["borrowed"]} ➜ {self.rec.get("returned","—")}  • {self.rec["status"]}',
                fSmall,
            )
        )
        vbox.addWidget(self._lbl(f'User: {self.rec.get("user","-")}', fSmall))

        box = QWidget()
        box.setLayout(vbox)
        root.addWidget(box)

        root.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Return button (only show if still borrowed)
        if self._showReturn and self.rec["status"] == "borrowed":
            self.btnReturn = QToolButton()
            self.btnReturn.setIcon(QIcon("assets/icons/arrow-back.svg"))
            self.btnReturn.setIconSize(QSize(16, 16))
            self.btnReturn.setMinimumSize(QSize(36, 36))
            self.btnReturn.setCursor(Qt.PointingHandCursor)
            self.btnReturn.setToolTip("Return book")
            self.btnReturn.setStyleSheet(
                "QToolButton {background:#34D399;color:#FFF;border-radius:12px;"
                "border:3px solid #DCFCE7;padding:3px 3px 3px 6px;}"
                "QToolButton:hover {background:rgba(52,211,153,200);}"
                "QToolButton:pressed {background:rgba(52,211,153,150);}"
            )
            root.addWidget(self.btnReturn)

    # ---------- Signals ----------
    def connectSignals(self):
        if hasattr(self, "btnReturn"):
            self.btnReturn.clicked.connect(lambda: self.returnRequested.emit(self.rec))

    # ---------- helper ----------
    @staticmethod
    def _lbl(text, font):
        l = QLabel(text)
        l.setFont(font)
        # l.setStyleSheet("color:#6B7280")
        return l
