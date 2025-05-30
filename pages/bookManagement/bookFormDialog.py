# helpers/bookFormDialog.py
from __future__ import annotations
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from uuid import uuid4

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QDialog,
    QMessageBox,
)

from helpers.dataReader import DataReader
from pages.bookManagement.ui_form import Ui_Dialog  # compiled from add_book_dialog.ui
from pages.bookManagement.stockListDialog import StockListDialog  # stock dialog


IMAGES_DIR = Path("data/images/books")  # target folder
IMAGES_DIR.mkdir(parents=True, exist_ok=True)  # ensure exists


class BookFormDialog(QDialog, Ui_Dialog):
    """Add / Edit Book dialog with working cover-image upload."""

    def __init__(self, parent=None, book: Optional[Dict] = None):
        super().__init__(parent)
        self.book = book or {}
        self.stockReader = DataReader("data/stocks.json")
        self._rows: List[Dict] = self._loadRows()
        self._coverPath: str = self.book.get("cover", "")
        self.setupUI()
        self.connectSignals()

    # ---------- UI ----------
    def setupUI(self):
        self.setupUi(self)

        self.setWindowTitle("Edit Book" if self.book else "Create Book")
        self.bookFormDialogTitle.setText("Edit Book" if self.book else "Create Book")

        if self.book:
            self.bookTitleInput.setText(self.book.get("title", ""))
            self.bookDescriptionInput.setText(self.book.get("description", ""))
            self.bookAuthorInput.setText(self.book.get("author", ""))
            self.bookPublisherInput.setText(self.book.get("publisher", ""))
            self.bookYearInput.setText(str(self.book.get("year", "")))
            self.bookIsbnInput.setText(self.book.get("isbn", ""))
            self.bookGenreInput.setText(self.book.get("genre", ""))
            self.bookLanguageInput.setText(self.book.get("language", ""))

        self._renderCover(self._coverPath)

    # ---------- Signals ----------
    def connectSignals(self):
        self.createBookButton.clicked.connect(self.accept)
        self.cancelBookButton.clicked.connect(self.reject)
        self.stockListButton.clicked.connect(self.openStockDialog)
        self.toolButton.clicked.connect(self.uploadCover)  # ← upload image

    # ---------- Image upload ----------
    def uploadCover(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Choose Cover Image", "", "Images (*.png *.jpg *.jpeg *.webp *.bmp)"
        )
        if not file:
            return

        src = Path(file)
        ext = src.suffix.lower()
        target_name = f"{uuid4()}{ext}"
        target_path = IMAGES_DIR / target_name

        try:
            shutil.copyfile(src, target_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to copy image:\n{e}")
            return

        self._coverPath = str(target_path)
        self._renderCover(self._coverPath)

    def _renderCover(self, path: str):
        pixmap = (
            QPixmap(path)
            if path and Path(path).exists()
            else QPixmap("assets/images/placeholder.png")
        )
        self.bookCoverPlaceholder.setPixmap(pixmap)

    # ---------- Stock helpers ----------
    def _loadRows(self) -> List[Dict]:
        isbn = self.book.get("isbn", "")
        return [dict(r) for r in self.stockReader.get() if r["isbn"] == isbn]

    def openStockDialog(self):
        isbn = self.bookIsbnInput.text().strip()
        if not isbn:
            QMessageBox.warning(self, "Warning", "ISBN must be filled first.")
            return
        for r in self._rows:
            r["isbn"] = isbn

        dlg = StockListDialog(self, isbn, self._rows)
        if dlg.exec():
            self._rows = dlg.stocks
            for r in self._rows:
                r["isbn"] = isbn

    # ---------- Public ----------
    def getFormData(self) -> Dict:
        return {
            "title": self.bookTitleInput.text(),
            "description": (
                self.bookDescriptionInput.toPlainText()
                if hasattr(self.bookDescriptionInput, "toPlainText")
                else self.bookDescriptionInput.text()
            ),
            "author": self.bookAuthorInput.text(),
            "publisher": self.bookPublisherInput.text(),
            "year": self.bookYearInput.text(),
            "isbn": self.bookIsbnInput.text(),
            "genre": self.bookGenreInput.text(),
            "language": self.bookLanguageInput.text(),
            "cover": self._coverPath,  # <- saved path
            "stock": self._rows,
        }


# Stand-alone test
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dlg = BookFormDialog()
    if dlg.exec():
        print(dlg.getFormData())
    sys.exit()
