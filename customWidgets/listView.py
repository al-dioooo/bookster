from PySide6.QtWidgets import QWidget, QListView, QStackedWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel


class ListView(QWidget):
    def __init__(self, stackedWidget: QStackedWidget, parent=None):
        super().__init__(parent)

        self.stackedWidget = stackedWidget
        # self.detailPage = stackedWidget.findChild(QWidget, "pageDetail")
        # self.labelDetail = self.detailPage.findChild(QLabel, "labelUserDetail")

        # List view setup
        self.listView = self.findChild(QListView, "listViewUsers")
        if not self.listView:
            # If not using .ui file, create manually
            layout = QVBoxLayout(self)
            self.listView = QListView()
            layout.addWidget(self.listView)

        self.users = [
            {"name": "Alice", "desc": "Frontend Developer"},
            {"name": "Bob", "desc": "Backend Developer"},
            {"name": "Charlie", "desc": "UI/UX Designer"},
        ]

        self.setupModel()
        self.listView.clicked.connect(self.onItemClicked)

    def setupModel(self):
        model = QStandardItemModel()
        for user in self.users:
            item = QStandardItem(f"{user['name']}\n{user['desc']}")
            font = QFont()
            font.setPointSize(10)
            item.setFont(font)
            item.setEditable(False)
            model.appendRow(item)
        self.listView.setModel(model)

    def onItemClicked(self, index: QModelIndex):
        user = self.users[index.row()]
        # self.labelDetail.setText(f"Welcome {user['name']}!\nRole: {user['desc']}")
        # self.stackedWidget.setCurrentWidget(self.detailPage)
