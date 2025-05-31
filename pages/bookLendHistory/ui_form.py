# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LendFormDialog(object):
    def setupUi(self, LendFormDialog):
        if not LendFormDialog.objectName():
            LendFormDialog.setObjectName(u"LendFormDialog")
        LendFormDialog.resize(480, 480)
        self.rootLayout = QVBoxLayout(LendFormDialog)
        self.rootLayout.setObjectName(u"rootLayout")
        self.cardFrame = QFrame(LendFormDialog)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setStyleSheet(u"QFrame { background: #FFF; border-radius: 12px; }")
        self.cardLayout = QVBoxLayout(self.cardFrame)
        self.cardLayout.setSpacing(12)
        self.cardLayout.setObjectName(u"cardLayout")
        self.dialogTitle = QLabel(self.cardFrame)
        self.dialogTitle.setObjectName(u"dialogTitle")
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(36)
        self.dialogTitle.setFont(font)
        self.dialogTitle.setStyleSheet(u"color:#3B82F6;")

        self.cardLayout.addWidget(self.dialogTitle)

        self.skuFrame = QFrame(self.cardFrame)
        self.skuFrame.setObjectName(u"skuFrame")
        self.skuFrameLayout = QVBoxLayout(self.skuFrame)
        self.skuFrameLayout.setObjectName(u"skuFrameLayout")
        self.skuFrameLayout.setContentsMargins(0, -1, 0, -1)
        self.skuLabel = QLabel(self.skuFrame)
        self.skuLabel.setObjectName(u"skuLabel")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        self.skuLabel.setFont(font1)

        self.skuFrameLayout.addWidget(self.skuLabel)

        self.skuRow = QFrame(self.skuFrame)
        self.skuRow.setObjectName(u"skuRow")
        self.skuRowLayout = QHBoxLayout(self.skuRow)
        self.skuRowLayout.setObjectName(u"skuRowLayout")
        self.skuRowLayout.setContentsMargins(0, 0, 0, 0)
        self.skuLineEdit = QLineEdit(self.skuRow)
        self.skuLineEdit.setObjectName(u"skuLineEdit")
        self.skuLineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")

        self.skuRowLayout.addWidget(self.skuLineEdit)

        self.checkSkuButton = QPushButton(self.skuRow)
        self.checkSkuButton.setObjectName(u"checkSkuButton")
        self.checkSkuButton.setMinimumSize(QSize(100, 0))
        self.checkSkuButton.setFont(font1)
        self.checkSkuButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #3B82F6; color: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(59,130,246,200); }\n"
"QPushButton:pressed { background: rgba(59,130,246,150); }")

        self.skuRowLayout.addWidget(self.checkSkuButton)


        self.skuFrameLayout.addWidget(self.skuRow)


        self.cardLayout.addWidget(self.skuFrame)

        self.userFrame = QFrame(self.cardFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrameLayout = QVBoxLayout(self.userFrame)
        self.userFrameLayout.setObjectName(u"userFrameLayout")
        self.userFrameLayout.setContentsMargins(0, -1, 0, -1)
        self.userLabel = QLabel(self.userFrame)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font1)

        self.userFrameLayout.addWidget(self.userLabel)

        self.userComboBox = QComboBox(self.userFrame)
        self.userComboBox.setObjectName(u"userComboBox")

        self.userFrameLayout.addWidget(self.userComboBox)


        self.cardLayout.addWidget(self.userFrame)

        self.dueFrame = QFrame(self.cardFrame)
        self.dueFrame.setObjectName(u"dueFrame")
        self.dueFrameLayout = QVBoxLayout(self.dueFrame)
        self.dueFrameLayout.setObjectName(u"dueFrameLayout")
        self.dueFrameLayout.setContentsMargins(0, -1, 0, -1)
        self.dueLabel = QLabel(self.dueFrame)
        self.dueLabel.setObjectName(u"dueLabel")

        self.dueFrameLayout.addWidget(self.dueLabel)

        self.dueDateEdit = QDateEdit(self.dueFrame)
        self.dueDateEdit.setObjectName(u"dueDateEdit")
        self.dueDateEdit.setCalendarPopup(True)

        self.dueFrameLayout.addWidget(self.dueDateEdit)


        self.cardLayout.addWidget(self.dueFrame)

        self.coverPreview = QLabel(self.cardFrame)
        self.coverPreview.setObjectName(u"coverPreview")
        self.coverPreview.setVisible(False)
        self.coverPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.coverPreview)

        self.buttonBar = QFrame(self.cardFrame)
        self.buttonBar.setObjectName(u"buttonBar")
        self.buttonBarLayout = QHBoxLayout(self.buttonBar)
        self.buttonBarLayout.setObjectName(u"buttonBarLayout")
        self.buttonBarLayout.setContentsMargins(0, -1, 0, -1)
        self.buttonSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBarLayout.addItem(self.buttonSpacer)

        self.cancelBtn = QPushButton(self.buttonBar)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #E5E5E5; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(229,229,229,200); }\n"
"QPushButton:pressed { background: rgba(229,229,229,150); }")

        self.buttonBarLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(self.buttonBar)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setFont(font1)
        self.saveBtn.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #3B82F6; color: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(59,130,246,200); }\n"
"QPushButton:pressed { background: rgba(59,130,246,150); }")

        self.buttonBarLayout.addWidget(self.saveBtn)


        self.cardLayout.addWidget(self.buttonBar)


        self.rootLayout.addWidget(self.cardFrame)


        self.retranslateUi(LendFormDialog)

        QMetaObject.connectSlotsByName(LendFormDialog)
    # setupUi

    def retranslateUi(self, LendFormDialog):
        LendFormDialog.setWindowTitle(QCoreApplication.translate("LendFormDialog", u"Borrow Book", None))
        self.dialogTitle.setText(QCoreApplication.translate("LendFormDialog", u"Borrow Book", None))
        self.skuLabel.setText(QCoreApplication.translate("LendFormDialog", u"SKU", None))
        self.checkSkuButton.setText(QCoreApplication.translate("LendFormDialog", u"Check", None))
        self.userLabel.setText(QCoreApplication.translate("LendFormDialog", u"User", None))
        self.dueLabel.setText(QCoreApplication.translate("LendFormDialog", u"Due date", None))
        self.cancelBtn.setText(QCoreApplication.translate("LendFormDialog", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("LendFormDialog", u"Save", None))
    # retranslateUi

