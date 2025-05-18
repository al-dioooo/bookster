from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from helpers.bookModel import BookModel

from PySide6.QtWidgets import QLineEdit, QPushButton


class AddBookDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load .ui file
        loader = QUiLoader()
        uiFile = QFile("form.ui")
        uiFile.open(QFile.ReadOnly)
        self.ui = loader.load(uiFile, self)
        uiFile.close()

        # Connect buttons and fields
        self.bookModel = BookModel()

        self.titleInput = self.ui.findChild(QLineEdit, "titleInput")
        self.authorInput = self.ui.findChild(QLineEdit, "authorInput")
        self.saveButton = self.ui.findChild(QPushButton, "saveButton")
        self.cancelButton = self.ui.findChild(QPushButton, "cancelButton")

        self.saveButton.clicked.connect(self.saveBook)
        self.cancelButton.clicked.connect(self.reject)

    def saveBook(self):
        title = self.titleInput.text().strip()
        author = self.authorInput.text().strip()

        if not title or not author:
            return  # You can show an error message

        self.bookModel.add({"title": title, "author": author})
        self.accept()  # Close dialog
