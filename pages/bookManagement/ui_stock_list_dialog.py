# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_list_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StockListDialog(object):
    def setupUi(self, StockListDialog):
        if not StockListDialog.objectName():
            StockListDialog.setObjectName(u"StockListDialog")
        StockListDialog.resize(720, 380)
        self.dialogVerticalLayout = QVBoxLayout(StockListDialog)
        self.dialogVerticalLayout.setObjectName(u"dialogVerticalLayout")
        self.stockTableWidget = QTableWidget(StockListDialog)
        if (self.stockTableWidget.columnCount() < 4):
            self.stockTableWidget.setColumnCount(4)
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.stockTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.stockTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.stockTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.stockTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.stockTableWidget.setObjectName(u"stockTableWidget")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        self.stockTableWidget.setFont(font1)
        self.stockTableWidget.setRowCount(0)
        self.stockTableWidget.setColumnCount(4)

        self.dialogVerticalLayout.addWidget(self.stockTableWidget)

        self.buttonBarFrame = QFrame(StockListDialog)
        self.buttonBarFrame.setObjectName(u"buttonBarFrame")
        self.buttonBarFrame.setFont(font1)
        self.buttonBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.buttonBarFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.addStockRowButton = QPushButton(self.buttonBarFrame)
        self.addStockRowButton.setObjectName(u"addStockRowButton")
        self.addStockRowButton.setMinimumSize(QSize(100, 0))
        self.addStockRowButton.setFont(font1)
        self.addStockRowButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #3B82F6; color: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(59,130,246,200); }\n"
"QPushButton:pressed { background: rgba(59,130,246,150); }")

        self.horizontalLayout.addWidget(self.addStockRowButton)

        self.editStockRowButton = QPushButton(self.buttonBarFrame)
        self.editStockRowButton.setObjectName(u"editStockRowButton")
        self.editStockRowButton.setMinimumSize(QSize(100, 0))
        self.editStockRowButton.setFont(font1)
        self.editStockRowButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(255,255,255,200); }\n"
"QPushButton:pressed { background: rgba(255,255,255,150); }")

        self.horizontalLayout.addWidget(self.editStockRowButton)

        self.deleteStockRowButton = QPushButton(self.buttonBarFrame)
        self.deleteStockRowButton.setObjectName(u"deleteStockRowButton")
        self.deleteStockRowButton.setMinimumSize(QSize(80, 0))
        self.deleteStockRowButton.setFont(font1)
        self.deleteStockRowButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(255,255,255,200); }\n"
"QPushButton:pressed { background: rgba(255,255,255,150); }")

        self.horizontalLayout.addWidget(self.deleteStockRowButton)

        self.hSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacer)

        self.cancelStockButton = QPushButton(self.buttonBarFrame)
        self.cancelStockButton.setObjectName(u"cancelStockButton")
        self.cancelStockButton.setMinimumSize(QSize(100, 0))
        self.cancelStockButton.setFont(font1)
        self.cancelStockButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(255,255,255,200); }\n"
"QPushButton:pressed { background: rgba(255,255,255,150); }")

        self.horizontalLayout.addWidget(self.cancelStockButton)

        self.saveStockButton = QPushButton(self.buttonBarFrame)
        self.saveStockButton.setObjectName(u"saveStockButton")
        self.saveStockButton.setMinimumSize(QSize(100, 0))
        self.saveStockButton.setFont(font1)
        self.saveStockButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #3B82F6; color: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(59,130,246,200); }\n"
"QPushButton:pressed { background: rgba(59,130,246,150); }")

        self.horizontalLayout.addWidget(self.saveStockButton)


        self.dialogVerticalLayout.addWidget(self.buttonBarFrame)


        self.retranslateUi(StockListDialog)

        QMetaObject.connectSlotsByName(StockListDialog)
    # setupUi

    def retranslateUi(self, StockListDialog):
        StockListDialog.setWindowTitle(QCoreApplication.translate("StockListDialog", u"Manage Stock", None))
        ___qtablewidgetitem = self.stockTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StockListDialog", u"SKU", None));
        ___qtablewidgetitem1 = self.stockTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StockListDialog", u"ISBN", None));
        ___qtablewidgetitem2 = self.stockTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StockListDialog", u"Status", None));
        ___qtablewidgetitem3 = self.stockTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StockListDialog", u"Location", None));
        self.addStockRowButton.setText(QCoreApplication.translate("StockListDialog", u"Add", None))
        self.editStockRowButton.setText(QCoreApplication.translate("StockListDialog", u"Edit", None))
        self.deleteStockRowButton.setText(QCoreApplication.translate("StockListDialog", u"Delete", None))
        self.cancelStockButton.setText(QCoreApplication.translate("StockListDialog", u"Cancel", None))
        self.saveStockButton.setText(QCoreApplication.translate("StockListDialog", u"Save", None))
    # retranslateUi

