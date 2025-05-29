from __future__ import annotations
from typing import Dict, List, Optional

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTableWidgetItem,
    QVBoxLayout,
)

from pages.bookManagement.ui_stock_list_dialog import Ui_StockListDialog


# ───────────────── StockEntryDialog ─────────────────
class StockEntryDialog(QDialog):
    def __init__(self, parent=None, row: Optional[Dict] = None):
        super().__init__(parent)
        self.row = row or {}
        self.setupUI()
        self.connectSignals()

    def setupUI(self):
        self.setWindowTitle("Add Stock" if not self.row else "Edit Stock")
        self.skuEdit = QLineEdit()
        self.skuEdit.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^[A-Za-z0-9\-]+$"))
        )
        self.locationEdit = QLineEdit()

        if self.row:
            self.skuEdit.setText(self.row["sku"])
            self.locationEdit.setText(self.row["location"])

        lay = QVBoxLayout(self)
        lay.addWidget(QLabel("SKU:"))
        lay.addWidget(self.skuEdit)
        lay.addWidget(QLabel("Location:"))
        lay.addWidget(self.locationEdit)

        from PySide6.QtWidgets import QDialogButtonBox

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        lay.addWidget(self.buttons)

    def connectSignals(self):
        self.buttons.accepted.connect(self._ok)
        self.buttons.rejected.connect(self.reject)

    def _ok(self):
        if not self.skuEdit.text().strip():
            QMessageBox.warning(self, "", "SKU cannot be empty.")
            return
        self.accept()

    def data(self) -> Dict:
        return {
            "sku": self.skuEdit.text().strip(),
            "location": self.locationEdit.text().strip(),
        }


# ───────────────── StockListDialog ─────────────────
class StockListDialog(QDialog, Ui_StockListDialog):
    """Editable table; rows kept only when Save pressed."""

    def __init__(self, parent, isbn: str, rows: List[Dict]):
        super().__init__(parent)
        self._isbn = isbn
        self._rows = [dict(r) for r in rows]  # working copy
        self.setupUI()
        self.connectSignals()
        self.refreshTable()

    # ----- UI -----
    def setupUI(self):
        self.setupUi(self)
        tbl = self.stockTableWidget
        tbl.setColumnCount(4)
        tbl.setHorizontalHeaderLabels(["SKU", "ISBN", "Status", "Location"])
        tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

    # ----- Signals -----
    def connectSignals(self):
        self.addStockRowButton.clicked.connect(self.addRow)
        self.editStockRowButton.clicked.connect(self.editRow)
        self.deleteStockRowButton.clicked.connect(self.deleteRow)
        self.saveStockButton.clicked.connect(self.accept)  # Save → accept()
        self.cancelStockButton.clicked.connect(self.reject)  # Cancel → reject()

    # ----- helpers -----
    def refreshTable(self):
        tbl = self.stockTableWidget
        tbl.setRowCount(len(self._rows))
        for r, row in enumerate(self._rows):
            tbl.setItem(r, 0, QTableWidgetItem(row["sku"]))
            tbl.setItem(r, 1, QTableWidgetItem(row["isbn"]))
            tbl.setItem(r, 2, QTableWidgetItem(row["status"]))
            tbl.setItem(r, 3, QTableWidgetItem(row["location"]))
        tbl.resizeColumnsToContents()

    def _selected(self) -> int:
        idx = {i.row() for i in self.stockTableWidget.selectedIndexes()}
        return next(iter(idx), -1)

    # ----- CRUD -----
    def addRow(self):
        dlg = StockEntryDialog(self)
        if dlg.exec():
            d = dlg.data()
            if any(r["sku"] == d["sku"] for r in self._rows):
                QMessageBox.warning(self, "", "SKU already exists.")
                return
            d.update({"isbn": self._isbn, "status": "available"})
            self._rows.append(d)
            self.refreshTable()

    def editRow(self):
        i = self._selected()
        if i == -1:
            return
        current = self._rows[i]
        dlg = StockEntryDialog(self, current)
        if dlg.exec():
            d = dlg.data()
            if any(r["sku"] == d["sku"] and r is not current for r in self._rows):
                QMessageBox.warning(self, "", "SKU already exists.")
                return
            current.update(d)
            self.refreshTable()

    def deleteRow(self):
        i = self._selected()
        if i == -1:
            return
        if (
            QMessageBox.question(
                self, "Confirm", "Delete row?", QMessageBox.Yes | QMessageBox.No
            )
            == QMessageBox.Yes
        ):
            self._rows.pop(i)
            self.refreshTable()

    # ----- public -----
    @property
    def stocks(self) -> List[Dict]:
        return [dict(r) for r in self._rows]  # deep copy
