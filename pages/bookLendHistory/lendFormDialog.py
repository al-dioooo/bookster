from datetime import date
from pathlib import Path
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QDateEdit,
    QDialogButtonBox,
    QMessageBox,
)


class LendFormDialog(QDialog):
    """
    mode='lend'  : borrow book
    mode='return': confirm return
    """

    def __init__(self, mode="lend", sku="", parent=None, user_list=None):
        super().__init__(parent)
        self.mode = mode
        self.initialSku = sku
        self.user_list = user_list or []
        self.setupUI()
        self.connectSignals()

    # ---------------- UI ----------------
    def setupUI(self):
        self.setWindowTitle("Borrow Book" if self.mode == "lend" else "Return Book")
        lay = QVBoxLayout(self)

        if self.mode == "lend":
            # SKU + Check button row
            skuRow = QHBoxLayout()
            self.skuEdit = QLineEdit(self.initialSku)
            self.skuEdit.setPlaceholderText("SKU")
            self.btnCheck = QPushButton("Check")
            skuRow.addWidget(QLabel("SKU:"))
            skuRow.addWidget(self.skuEdit)
            skuRow.addWidget(self.btnCheck)
            lay.addLayout(skuRow)

            # User combo (editable search)
            lay.addWidget(QLabel("User:"))
            self.userCombo = QComboBox()
            self.userCombo.setEditable(True)
            self.userCombo.addItems(self.user_list)
            self.userCombo.setInsertPolicy(QComboBox.NoInsert)
            lay.addWidget(self.userCombo)

            # Due date
            lay.addWidget(QLabel("Due date:"))
            self.dueEdit = QDateEdit()
            self.dueEdit.setCalendarPopup(True)
            self.dueEdit.setDate(QDate.currentDate().addDays(7))
            lay.addWidget(self.dueEdit)

            # book preview (hidden until SKU checked)
            self.preview = QLabel(alignment=Qt.AlignCenter)
            self.preview.setVisible(False)
            lay.addWidget(self.preview)

        else:  # return dialog
            lay.addWidget(QLabel(f"Return SKU {self.initialSku}?"))

        # OK/Cancel
        self.btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        lay.addWidget(self.btnBox)

    # ---------------- Signals ----------------
    def connectSignals(self):
        self.btnBox.accepted.connect(self.accept)
        self.btnBox.rejected.connect(self.reject)
        if self.mode == "lend":
            self.btnCheck.clicked.connect(self.checkSku)

    # ---------------- SKU check ----------------
    def checkSku(self):
        sku = self.skuEdit.text().strip()
        if not sku:
            QMessageBox.warning(self, "", "Enter SKU first")
            return

        # look up book via SKU
        from helpers.stockModel import StockModel
        from helpers.bookModel import BookModel
        from helpers.lendModel import LendModel

        stockModel = StockModel("data/stocks.json")
        row = next((r for r in stockModel.all() if r["sku"] == sku), None)
        if not row:
            QMessageBox.warning(self, "", "SKU not found in stock")
            return

        # already borrowed?
        if LendModel("data/lends.json")._index.get(sku, {}).get("status") == "borrowed":
            QMessageBox.warning(self, "", "This SKU is already borrowed")
            return

        # fetch book meta
        bm = BookModel("data/books.json")
        book = next((b for b in bm.getAll() if b["isbn"] == row["isbn"]), None)
        if not book:
            QMessageBox.information(self, "", "Book meta not found")
            self.preview.setVisible(False)
            return

        # show thumbnail + info
        cover = book.get("cover", "")
        pix = (
            QPixmap(cover)
            if cover and Path(cover).exists()
            else QPixmap("assets/images/placeholder.png")
        )
        self.preview.setPixmap(
            pix.scaled(120, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        )
        self.preview.setToolTip(f"{book['title']}\nby {book['author']}")
        self.preview.setVisible(True)

        # store for accept()
        self._selectedBook = book
        self._stockRow = row

    # ---------------- form data ----------------
    def data(self):
        if self.mode == "lend":
            return {
                "isbn": self._stockRow["isbn"],  # from check
                "sku": self.skuEdit.text().strip(),
                "user": self.userCombo.currentText().strip(),
                "borrowed": date.today().isoformat(),
                "due": self.dueEdit.date().toString("yyyy-MM-dd"),
                "status": "borrowed",
                "title": self._selectedBook["title"],
                "author": self._selectedBook["author"],
                "cover": self._selectedBook.get("cover", ""),
            }
        return {}

    # ---------------- accept override ----------------
    def accept(self):
        """Block OK if SKU hasn’t been validated."""
        if self.mode == "lend" and not hasattr(self, "_stockRow"):
            QMessageBox.warning(
                self, "", "Please press “Check” to validate the SKU first."
            )
            return
        super().accept()
