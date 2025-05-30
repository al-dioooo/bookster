# controllers/bookLendHistoryPageController.py
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QToolButton, QMessageBox

from helpers.lendModel import LendModel
from helpers.bookModel import BookModel
from helpers.userModel import UserModel
from pages.bookLendHistory.lendFormDialog import LendFormDialog
from pages.bookLendHistory.lendListItem import LendListItem


class BookLendHistoryPageController(QWidget):
    """
    Controls the redesigned `bookLendHistoryPage`
    (now using the new object names you listed).
    """

    def __init__(self, mainWindow):
        super().__init__(mainWindow.bookLendHistoryPage)  # parent = existing page
        self.mainWindow = mainWindow

        # models
        self.lendModel = LendModel("data/lends.json")
        self.bookModel = BookModel("data/books.json")

        self.setupUI()
        self.connectSignals()
        self.populate(self.lendModel.all())

    # -------------------------------------------------- helpers
    def _f(self, typ, name):
        return self.mainWindow.bookLendHistoryPage.findChild(typ, name)

    # -------------------------------------------------- UI
    def setupUI(self):
        # renamed widgets
        self.searchField = self._f(QLineEdit, "searchBookLendHistoryInput")
        self.borrowButton = self._f(QToolButton, "borrowButton")
        self.backButton = self._f(QToolButton, "bookLendHistoryBackButton")

        # scroll-content widget (inside QScrollArea)
        self.scrollContent = self._f(
            QWidget, "bookLendHistoryListcrollAreaWidgetContents"
        )
        self.listLayout = self.scrollContent.layout()

        # icons
        self.borrowButton.setIcon(QIcon("assets/icons/plus.svg"))
        self.borrowButton.setIconSize(QSize(20, 20))
        self.backButton.setIcon(QIcon("assets/icons/arrow-narrow-left.svg"))
        self.backButton.setIconSize(QSize(20, 20))

    # -------------------------------------------------- Signals
    def connectSignals(self):
        self.searchField.textChanged.connect(self.filterList)
        self.borrowButton.clicked.connect(self.openBorrowDialog)
        self.backButton.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.mainPage
            )
        )

    # -------------------------------------------------- list helpers
    def populate(self, rows):
        lay = self.listLayout
        while lay.count():
            itm = lay.takeAt(0)
            if itm.widget():
                itm.widget().deleteLater()

        for r in rows:
            item = LendListItem(r)
            item.returnRequested.connect(self.confirmReturn)
            lay.addWidget(item)
        lay.addStretch()

    def filterList(self, txt):
        self.populate(self.lendModel.search(txt))

    # -------------------------------------------------- borrow dialog
    def openBorrowDialog(self):
        userNames = [u.get("name", str(u.get("id", ""))) for u in UserModel().all()]

        dlg = LendFormDialog("lend", parent=self.mainWindow, user_list=userNames)
        if not dlg.exec():
            return

        data = dlg.data()
        if not data["isbn"] or not data["sku"]:
            QMessageBox.warning(self.mainWindow, "", "ISBN & SKU required")
            return

        # enrich with book meta
        book = next(
            (b for b in self.bookModel.getAll() if b["isbn"] == data["isbn"]), None
        )
        data.update(
            title=book["title"] if book else "-",
            author=book["author"] if book else "-",
            cover=book.get("cover", "") if book else "",
        )

        try:
            self.lendModel.borrow(data)
        except ValueError as e:
            QMessageBox.warning(self.mainWindow, "", str(e))
            return

        self.populate(self.lendModel.all())

    # -------------------------------------------------- external return
    def returnBySku(self, sku: str):
        try:
            self.lendModel.return_book(sku)
            self.populate(self.lendModel.all())
        except KeyError:
            QMessageBox.warning(self.mainWindow, "", "Lend not found")

    def confirmReturn(self, rec: dict):
        from datetime import date

        if (
            QMessageBox.question(
                self.mainWindow,
                "Confirm Return",
                f'Return "{rec["title"]}" (SKU {rec["sku"]})?',
                QMessageBox.Yes | QMessageBox.No,
            )
            == QMessageBox.No
        ):
            return

        self.lendModel.return_book(rec["sku"], day=date.today().isoformat())
        self.populate(self.lendModel.all())
