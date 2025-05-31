from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from helpers.stockModel import StockModel

from pages.bookManagement.ui_detail import Ui_BookDetailDialog
from pages.bookManagement.stockListDialog import (
    StockListDialog,
)  # already in your project

PLACEHOLDER = "assets/images/placeholder.png"


class BookDetailDialog(QDialog, Ui_BookDetailDialog):
    """
    Show detailed information for a single book.
    """

    def __init__(self, parent=None, book: dict | None = None):
        super().__init__(parent)
        self.book = book or {}
        self.setupUi(self)  # from ui_detail.py
        self._populate()
        self._connectSignals()

    # ------------------------------------------------------------------
    def _populate(self):
        # title at top
        self.bookDetailTitleLabel.setText("Book Detail")
        self.titleLabel.setText(self.book.get("title", "-"))
        self.authorLabel.setText(f"by {self.book.get('author', '-')}")
        self.publisherLabel.setText(f"Publisher: {self.book.get('publisher', '-')}")
        self.yearLabel.setText(f"Year: {self.book.get('year', '-')}")
        self.genreLabel.setText(f"Genre: {self.book.get('genre', '-')}")
        self.languageLabel.setText(f"Language: {self.book.get('language', '-')}")
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setText(self.book.get("description", "-"))

        # cover
        cover_path = self.book.get("cover", "")
        pix = (
            QPixmap(cover_path)
            if cover_path and Path(cover_path).exists()
            else QPixmap(PLACEHOLDER)
        )
        self.bookCoverLabel.setPixmap(
            pix.scaled(
                self.bookCoverLabel.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation,
            )
        )

    # ------------------------------------------------------------------
    def _connectSignals(self):
        self.closeButton.clicked.connect(self.accept)
        self.stockListButton.clicked.connect(self._openStocks)

    def _openStocks(self):
        # 1. gather all stock rows for this ISBN
        rows = [
            dict(r)
            for r in StockModel("data/stocks.json").all()
            if r["isbn"] == self.book["isbn"]
        ]

        # 2. create the dialog
        dlg = StockListDialog(self, isbn=self.book["isbn"], rows=rows)

        # 3. hide CRUD controls to make it read-only
        for w in (
            dlg.addStockRowButton,
            dlg.editStockRowButton,
            dlg.deleteStockRowButton,
            dlg.saveStockButton,
        ):
            w.setVisible(False)

        dlg.exec()
