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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_UserFormDialog(object):
    def setupUi(self, UserFormDialog):
        if not UserFormDialog.objectName():
            UserFormDialog.setObjectName(u"UserFormDialog")
        UserFormDialog.resize(400, 340)
        self.dialogVerticalLayout = QVBoxLayout(UserFormDialog)
        self.dialogVerticalLayout.setObjectName(u"dialogVerticalLayout")
        self.dlgTitle = QLabel(UserFormDialog)
        self.dlgTitle.setObjectName(u"dlgTitle")
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(36)
        self.dlgTitle.setFont(font)
        self.dlgTitle.setStyleSheet(u"QLabel {\n"
"	color:#3B82F6;\n"
"}")
        self.dlgTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.dialogVerticalLayout.addWidget(self.dlgTitle, 0, Qt.AlignmentFlag.AlignLeft)

        self.vsp1 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dialogVerticalLayout.addItem(self.vsp1)

        self.nameInput = QLineEdit(UserFormDialog)
        self.nameInput.setObjectName(u"nameInput")

        self.dialogVerticalLayout.addWidget(self.nameInput)

        self.usernameInput = QLineEdit(UserFormDialog)
        self.usernameInput.setObjectName(u"usernameInput")

        self.dialogVerticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(UserFormDialog)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.dialogVerticalLayout.addWidget(self.passwordInput)

        self.roleCombo = QComboBox(UserFormDialog)
        self.roleCombo.addItem("")
        self.roleCombo.addItem("")
        self.roleCombo.addItem("")
        self.roleCombo.setObjectName(u"roleCombo")

        self.dialogVerticalLayout.addWidget(self.roleCombo)

        self.vsp2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dialogVerticalLayout.addItem(self.vsp2)

        self.frameButtons = QFrame(UserFormDialog)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonLayout = QHBoxLayout(self.frameButtons)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(-1, -1, -1, 0)
        self.hsp = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hsp)

        self.cancelUserButton = QPushButton(self.frameButtons)
        self.cancelUserButton.setObjectName(u"cancelUserButton")
        self.cancelUserButton.setMinimumSize(QSize(100, 0))

        self.buttonLayout.addWidget(self.cancelUserButton)

        self.saveUserButton = QPushButton(self.frameButtons)
        self.saveUserButton.setObjectName(u"saveUserButton")
        self.saveUserButton.setMinimumSize(QSize(100, 0))

        self.buttonLayout.addWidget(self.saveUserButton)


        self.dialogVerticalLayout.addWidget(self.frameButtons)


        self.retranslateUi(UserFormDialog)

        QMetaObject.connectSlotsByName(UserFormDialog)
    # setupUi

    def retranslateUi(self, UserFormDialog):
        UserFormDialog.setWindowTitle(QCoreApplication.translate("UserFormDialog", u"Create User", None))
        self.dlgTitle.setText(QCoreApplication.translate("UserFormDialog", u"Create User", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Name *", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Username *", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("UserFormDialog", u"Password *", None))
        self.roleCombo.setItemText(0, QCoreApplication.translate("UserFormDialog", u"administrator", None))
        self.roleCombo.setItemText(1, QCoreApplication.translate("UserFormDialog", u"librarian", None))
        self.roleCombo.setItemText(2, QCoreApplication.translate("UserFormDialog", u"user", None))

        self.cancelUserButton.setStyleSheet(QCoreApplication.translate("UserFormDialog", u"\n"
"QPushButton {\n"
"  border-radius:12px;\n"
"  background:#FFF;\n"
"  padding:6px;\n"
"}\n"
"QPushButton:hover  {background:rgba(255,255,255,200);}\n"
"QPushButton:pressed{background:rgba(255,255,255,150);}\n"
"", None))
        self.cancelUserButton.setText(QCoreApplication.translate("UserFormDialog", u"Cancel", None))
        self.saveUserButton.setStyleSheet(QCoreApplication.translate("UserFormDialog", u"\n"
"QPushButton {\n"
"  border-radius:12px;\n"
"  background:#3B82F6;\n"
"  color:white;\n"
"  padding:6px;\n"
"}\n"
"QPushButton:hover  {background:rgba(59,130,246,200);}\n"
"QPushButton:pressed{background:rgba(59,130,246,150);}\n"
"", None))
        self.saveUserButton.setText(QCoreApplication.translate("UserFormDialog", u"Save", None))
    # retranslateUi

