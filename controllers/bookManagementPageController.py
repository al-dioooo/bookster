# bookManagement.py
from PySide6.QtWidgets import QWidget, QLineEdit, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from customWidgets.bookCardList import BookCardList


class BookManagementPageController:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.books = [
            {"name": "Bumi Manusia", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Matahari", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Langit", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Bulan", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Laut Bercerita", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Pulang", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Bumi", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Cantik itu Luka", "description": "Lorem ipsum dolor sit amet."},
            {"name": "Laskar Pelangi", "description": "Lorem ipsum dolor sit amet."},
            {
                "name": "Perjalanan Menuju Pulang",
                "description": "Lorem ipsum dolor sit amet.",
            },
        ]

        self.setupUi()
        self.connectSignals()
        self.populateBookList(self.books)

    def setupUi(self):
        self.bookListScrollArea = self.getBookListScrollArea()
        self.bookListScrollContent = self.bookListScrollArea.widget()
        self.bookListScrollLayout = self.bookListScrollContent.layout()
        self.searchBookInput = self.getSearchBookInput()
        self.addBookButton = self.getAddBookButton()
        self.bookManagementBackButton = self.getBackButton()

        plusIcon = QIcon("assets/icons/plus.svg")
        self.addBookButton.setIcon(plusIcon)
        self.addBookButton.setIconSize(QSize(20, 20))

        backIcon = QIcon("assets/icons/arrow-narrow-left.svg")
        self.bookManagementBackButton.setIcon(backIcon)
        self.bookManagementBackButton.setIconSize(QSize(20, 20))

    def connectSignals(self):
        self.searchBookInput.textChanged.connect(self.onSearchBookInputChanged)
        self.bookManagementBackButton.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.mainPage
            )
        )

    def getBookListScrollArea(self):
        return self.mainWindow.findChild(QWidget, "bookListScrollArea")

    def getSearchBookInput(self):
        return self.mainWindow.findChild(QLineEdit, "searchBookInput")

    def getAddBookButton(self):
        return self.mainWindow.findChild(QToolButton, "addBookButton")

    def getBackButton(self):
        return self.mainWindow.findChild(QToolButton, "bookManagementBackButton")

    def onSearchBookInputChanged(self, text):
        filteredBooks = [
            book
            for book in self.books
            if text.lower() in book["name"].lower()
            or text.lower() in book["description"].lower()
        ]
        self.populateBookList(filteredBooks)

    def populateBookList(self, books):
        while self.bookListScrollLayout.count():
            child = self.bookListScrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for book in books:
            card = BookCardList(book["name"], book["description"])
            self.bookListScrollLayout.addWidget(card)

        self.bookListScrollLayout.addStretch()
