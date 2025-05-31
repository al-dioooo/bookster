# pages/bookLendHistory/lendFormDialog.py
from __future__ import annotations

from datetime import date
from pathlib import Path

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)

from pages.bookLendHistory.ui_form import Ui_LendFormDialog
from helpers.stockModel import StockModel
from helpers.bookModel import BookModel
from helpers.lendModel import LendModel

PLACEHOLDER = "assets/images/placeholder.png"


class LendFormDialog(QDialog, Ui_LendFormDialog):
    """
    Borrow / Return dialog with User-form styling.

    Parameters
    ----------
    mode : "lend" or "return"
    sku  : pre-filled SKU when returning
    user_list : list[str]  — names / IDs for the combo box
    """

    def __init__(self, mode: str = "lend", sku: str = "", parent=None, user_list=None):
        super().__init__(parent)
        self.mode = mode
        self.initialSku = sku
        self.user_list = user_list or []
        self._setupUI()
        self._connectSignals()

    # ------------------------------------------------------------------
    # UI helpers
    # ------------------------------------------------------------------
    def _setupUI(self):
        self.setupUi(self)  # comes from .ui file

        # ── common tweaks ──
        self.coverPreview.setVisible(False)
        self.userComboBox.addItems(self.user_list)
        self.dueDateEdit.setDate(QDate.currentDate().addDays(7))
        self.skuLineEdit.setText(self.initialSku)

        if self.mode == "return":
            # hide borrow-only widgets
            for w in (self.skuFrame, self.userFrame, self.dueFrame, self.coverPreview):
                w.setVisible(False)
            self.dialogTitle.setText("Return Book")
            self.saveBtn.setText("Return")
        else:  # borrow
            self.dialogTitle.setText("Borrow Book")
            self.saveBtn.setText("Save")

    def _connectSignals(self):
        self.cancelBtn.clicked.connect(self.reject)

        if self.mode == "lend":
            self.checkSkuButton.clicked.connect(self._checkSku)
            self.saveBtn.clicked.connect(self._guardAndAccept)
        else:  # return
            self.saveBtn.clicked.connect(self.accept)

    # ------------------------------------------------------------------
    # SKU validation + preview
    # ------------------------------------------------------------------
    def _checkSku(self):
        sku = self.skuLineEdit.text().strip()
        if not sku:
            QMessageBox.warning(self, "", "Enter SKU first.")
            return

        # 1. look up stock
        stock_row = next(
            (r for r in StockModel("data/stocks.json").all() if r["sku"] == sku), None
        )
        if not stock_row:
            QMessageBox.warning(self, "", "SKU not found in stock.")
            return

        # 2. already borrowed?
        if LendModel("data/lends.json")._index.get(sku, {}).get("status") == "borrowed":
            QMessageBox.warning(self, "", "This SKU is already borrowed.")
            return

        # 3. fetch book meta
        book = next(
            (
                b
                for b in BookModel("data/books.json").getAll()
                if b["isbn"] == stock_row["isbn"]
            ),
            None,
        )
        if not book:
            QMessageBox.information(self, "", "Book metadata not found.")
            self.coverPreview.setVisible(False)
            return

        # 4. show thumbnail
        cover = book.get("cover", "") or PLACEHOLDER
        pix = QPixmap(cover) if Path(cover).exists() else QPixmap(PLACEHOLDER)
        self.coverPreview.setPixmap(
            pix.scaled(120, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        )
        self.coverPreview.setToolTip(f"{book['title']}\nby {book['author']}")
        self.coverPreview.setVisible(True)

        # 5. store for later
        self._stockRow = stock_row
        self._selectedBook = book

    # ------------------------------------------------------------------
    # Guard: make sure SKU has been validated
    # ------------------------------------------------------------------
    def _guardAndAccept(self):
        if not hasattr(self, "_stockRow"):
            QMessageBox.warning(self, "", "Please press “Check” to validate the SKU.")
            return
        self.accept()

    # ------------------------------------------------------------------
    # Data extractor
    # ------------------------------------------------------------------
    def data(self) -> dict:
        """
        Returns full lend record (for mode 'lend'),
        or {} for mode 'return'.
        """
        if self.mode == "lend":
            return {
                "isbn": self._stockRow["isbn"],
                "sku": self.skuLineEdit.text().strip(),
                "user": self.userComboBox.currentText().strip(),
                "borrowed": date.today().isoformat(),
                "due": self.dueDateEdit.date().toString("yyyy-MM-dd"),
                "status": "borrowed",
                "title": self._selectedBook["title"],
                "author": self._selectedBook["author"],
                "cover": self._selectedBook.get("cover", ""),
            }
        return {}  # return dialog doesn’t need extra data
