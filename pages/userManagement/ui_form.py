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
        UserFormDialog.resize(480, 551)
        font = QFont()
        font.setFamilies([u"Poppins"])
        UserFormDialog.setFont(font)
        self.dialogVerticalLayout = QVBoxLayout(UserFormDialog)
        self.dialogVerticalLayout.setObjectName(u"dialogVerticalLayout")
        self.dialogVerticalLayout.setContentsMargins(12, 12, 12, 12)
        self.frame_5 = QFrame(UserFormDialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame#frame_5 {\n"
"	background: #FFF;\n"
"	border-radius: 12px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dlgTitle = QLabel(self.frame_5)
        self.dlgTitle.setObjectName(u"dlgTitle")
        font1 = QFont()
        font1.setFamilies([u"Magic Retro"])
        font1.setPointSize(36)
        self.dlgTitle.setFont(font1)
        self.dlgTitle.setStyleSheet(u"QLabel {\n"
"	color:#3B82F6;\n"
"}")
        self.dlgTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.dlgTitle, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.nameInput = QLineEdit(self.frame)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy)
        self.nameInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")

        self.verticalLayout_4.addWidget(self.nameInput)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.usernameInput = QLineEdit(self.frame_2)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy)
        self.usernameInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")

        self.verticalLayout_3.addWidget(self.usernameInput)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.passwordInput = QLineEdit(self.frame_3)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        self.passwordInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.passwordInput)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.roleCombo = QComboBox(self.frame_4)
        self.roleCombo.addItem("")
        self.roleCombo.addItem("")
        self.roleCombo.addItem("")
        self.roleCombo.setObjectName(u"roleCombo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.roleCombo.sizePolicy().hasHeightForWidth())
        self.roleCombo.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.roleCombo)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frameButtons = QFrame(self.frame_5)
        self.frameButtons.setObjectName(u"frameButtons")
        self.buttonLayout = QHBoxLayout(self.frameButtons)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 12, 0, 0)
        self.hsp = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hsp)

        self.cancelUserButton = QPushButton(self.frameButtons)
        self.cancelUserButton.setObjectName(u"cancelUserButton")
        self.cancelUserButton.setMinimumSize(QSize(100, 0))
        self.cancelUserButton.setFont(font)
        self.cancelUserButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #E5E5E5; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(229,229,229,200); }\n"
"QPushButton:pressed { background: rgba(229,229,229,150); }")

        self.buttonLayout.addWidget(self.cancelUserButton)

        self.saveUserButton = QPushButton(self.frameButtons)
        self.saveUserButton.setObjectName(u"saveUserButton")
        self.saveUserButton.setMinimumSize(QSize(100, 0))
        self.saveUserButton.setFont(font)

        self.buttonLayout.addWidget(self.saveUserButton)


        self.verticalLayout_5.addWidget(self.frameButtons)


        self.dialogVerticalLayout.addWidget(self.frame_5)

        self.vsp2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dialogVerticalLayout.addItem(self.vsp2)


        self.retranslateUi(UserFormDialog)

        QMetaObject.connectSlotsByName(UserFormDialog)
    # setupUi

    def retranslateUi(self, UserFormDialog):
        UserFormDialog.setWindowTitle(QCoreApplication.translate("UserFormDialog", u"Create User", None))
        self.dlgTitle.setText(QCoreApplication.translate("UserFormDialog", u"Create User", None))
        self.label.setText(QCoreApplication.translate("UserFormDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("UserFormDialog", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("UserFormDialog", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("UserFormDialog", u"Role", None))
        self.roleCombo.setItemText(0, QCoreApplication.translate("UserFormDialog", u"Member", None))
        self.roleCombo.setItemText(1, QCoreApplication.translate("UserFormDialog", u"Librarian", None))
        self.roleCombo.setItemText(2, QCoreApplication.translate("UserFormDialog", u"Administrator", None))

        self.roleCombo.setCurrentText(QCoreApplication.translate("UserFormDialog", u"Member", None))
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

