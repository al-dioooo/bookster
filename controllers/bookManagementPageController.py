from pathlib import Path
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLineEdit, QToolButton, QWidget, QMessageBox

# helpers
from helpers.bookModel import BookModel
from helpers.stockModel import StockModel

# pages widgets & dialogs
from pages.bookManagement.bookFormDialog import BookFormDialog
from customWidgets.bookListItem import BookListItem


class BookManagementPageController:
    """
    Controller halaman Book-Management:
      • List + search
      • Create / Edit / Delete
      • Sinkron stok
    """

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        # model
        self.bookModel = BookModel("data/books.json")
        self.stockModel = StockModel("data/stocks.json")

        self.books = self.bookModel.getAll()

        self.setupUI()
        self.connectSignals()
        self.populateBookList(self.books)

    # ---------------- UI ----------------
    def setupUI(self):
        # grab widget dari UI utama
        self.bookListScrollArea = self._f(QWidget, "bookListScrollArea")
        self.bookListScrollContent = self.bookListScrollArea.widget()
        self.bookListScrollLayout = self.bookListScrollContent.layout()

        self.searchBookInput = self._f(QLineEdit, "searchBookInput")
        self.addBookButton = self._f(QToolButton, "addBookButton")
        self.backButton = self._f(QToolButton, "bookManagementBackButton")
        self.pageDescription = self._f(QWidget, "bookPageDescription")

        # icon
        self.addBookButton.setIcon(QIcon("assets/icons/plus.svg"))
        self.addBookButton.setIconSize(QSize(20, 20))
        self.backButton.setIcon(QIcon("assets/icons/arrow-narrow-left.svg"))
        self.backButton.setIconSize(QSize(20, 20))

    # ---------------- Signals ----------------
    def connectSignals(self):
        self.searchBookInput.textChanged.connect(self.filterBooks)
        self.backButton.clicked.connect(self._goBack)

        if self.mainWindow.currentRole == "librarian":
            self.addBookButton.clicked.connect(self.openCreateDialog)
        else:
            self.addBookButton.setVisible(False)

    def _goBack(self):
        self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.mainPage)
        self.mainWindow.setWindowTitle("Bookster - Dashboard")

    # ---------------- helpers ----------------
    def _f(self, typ, name):
        return self.mainWindow.findChild(typ, name)

    # ---------------- list & search ----------------
    def filterBooks(self, text: str):
        key = text.lower()
        self.populateBookList(
            [
                b
                for b in self.books
                if key in b["title"].lower()
                or key in b["author"].lower()
                or key in b["isbn"].lower()
            ]
        )

    def populateBookList(self, books):
        lay = self.bookListScrollLayout
        showCrud = self.mainWindow.currentRole == "librarian"
        while lay.count():
            itm = lay.takeAt(0)
            if itm.widget():
                itm.widget().deleteLater()

        for book in books:
            item = BookListItem(book, showCrud=showCrud)
            item.detailRequested.connect(self.openDetailDialog)
            item.editRequested.connect(self.openEditDialog)
            item.deleteRequested.connect(self.deleteBook)
            lay.addWidget(item)

        lay.addStretch()

        n = len(books)
        self.pageDescription.setText(
            "No Book Available"
            if n == 0
            else "1 Book Available" if n == 1 else f"{n} Books Available"
        )

    # ---------------- dialogs ----------------
    def openDetailDialog(self, book: dict):
        from pages.bookManagement.bookDetailDialog import BookDetailDialog

        dlg = BookDetailDialog(self.mainWindow, book=book)
        dlg.exec()

    def openCreateDialog(self):
        self._openDialog(mode="create")

    def openEditDialog(self, book: dict):
        self._openDialog(mode="edit", original=book)

    def _openDialog(self, mode: str, original: dict | None = None):
        dlg = (
            BookFormDialog(self.mainWindow, book=original)
            if mode == "edit"
            else BookFormDialog(self.mainWindow)
        )
        if not dlg.exec():
            return

        form = dlg.getFormData()
        isbn = form["isbn"]
        rows = form["stock"]

        # 1. stok
        self.stockModel.replace_for_isbn(isbn, rows)

        # 2. buku (stock = count saja)
        record = {k: v for k, v in form.items() if k != "stock"}
        record["stock"] = len(rows)
        self.bookModel.upsert(isbn, record)

        # 3. refresh
        self.books = self.bookModel.getAll()
        self.populateBookList(self.books)

    # ---------------- delete ----------------
    def deleteBook(self, book: dict):
        if (
            QMessageBox.question(
                self.mainWindow,
                "Confirm Delete",
                f'Delete "{book["title"]}"?',
                QMessageBox.Yes | QMessageBox.No,
            )
            == QMessageBox.No
        ):
            return

        isbn = book["isbn"]
        self.bookModel.delete(isbn)
        self.stockModel.replace_for_isbn(isbn, [])

        self.books = self.bookModel.getAll()
        self.populateBookList(self.books)

    def refreshRole(self):
        role = self.mainWindow.currentRole()
        # Add button
        self.addBookButton.setVisible(role == "librarian")
        # Re-render list (CRUD icons depend on role)
        self.populateBookList(self.books)
