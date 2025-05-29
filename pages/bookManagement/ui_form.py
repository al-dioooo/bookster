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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        self.dialogVerticalLayout = QVBoxLayout(Dialog)
        self.dialogVerticalLayout.setObjectName(u"dialogVerticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 694, 903))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.bookFormDialogTitle = QLabel(self.scrollAreaWidgetContents)
        self.bookFormDialogTitle.setObjectName(u"bookFormDialogTitle")
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(36)
        self.bookFormDialogTitle.setFont(font)
        self.bookFormDialogTitle.setStyleSheet(u"QLabel { color: #3B82F6; }")

        self.verticalLayout_12.addWidget(self.bookFormDialogTitle)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookCoverPlaceholder = QLabel(self.frame_9)
        self.bookCoverPlaceholder.setObjectName(u"bookCoverPlaceholder")
        self.bookCoverPlaceholder.setMinimumSize(QSize(140, 180))
        self.bookCoverPlaceholder.setMaximumSize(QSize(140, 180))
        self.bookCoverPlaceholder.setStyleSheet(u"image: url(:/assets/images/placeholder.png);\n"
"QLabel {\n"
"  border-radius: 12px;\n"
"  border: 3px solid #DBEAFE;\n"
"}")
        self.bookCoverPlaceholder.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.bookCoverPlaceholder)

        self.toolButton = QToolButton(self.frame_9)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(36, 36))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(16)
        self.toolButton.setFont(font1)
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"  background: #93C5FD; color: #FFF;\n"
"  border-radius: 12px; border: 3px solid #DBEAFE;\n"
"  padding: 3px 3px 3px 6px;\n"
"}\n"
"QToolButton:hover   { background: rgba(147,197,253,200); }\n"
"QToolButton:pressed { background: rgba(147,197,253,150); }\n"
"QToolButton QLabel  { margin-left: 6px; }")
        self.toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_11.addWidget(self.toolButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_9)

        self.groupBox = QGroupBox(self.frame_10)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        self.groupBox.setFont(font2)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookIsbnInput = QLineEdit(self.frame)
        self.bookIsbnInput.setObjectName(u"bookIsbnInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookIsbnInput.sizePolicy().hasHeightForWidth())
        self.bookIsbnInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.bookIsbnInput)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookTitleInput = QLineEdit(self.frame_2)
        self.bookTitleInput.setObjectName(u"bookTitleInput")
        sizePolicy.setHeightForWidth(self.bookTitleInput.sizePolicy().hasHeightForWidth())
        self.bookTitleInput.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.bookTitleInput)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookAuthorInput = QLineEdit(self.frame_3)
        self.bookAuthorInput.setObjectName(u"bookAuthorInput")
        sizePolicy.setHeightForWidth(self.bookAuthorInput.sizePolicy().hasHeightForWidth())
        self.bookAuthorInput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.bookAuthorInput)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookPublisherInput = QLineEdit(self.frame_4)
        self.bookPublisherInput.setObjectName(u"bookPublisherInput")
        sizePolicy.setHeightForWidth(self.bookPublisherInput.sizePolicy().hasHeightForWidth())
        self.bookPublisherInput.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.bookPublisherInput)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookYearInput = QLineEdit(self.frame_5)
        self.bookYearInput.setObjectName(u"bookYearInput")
        sizePolicy.setHeightForWidth(self.bookYearInput.sizePolicy().hasHeightForWidth())
        self.bookYearInput.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.bookYearInput)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 80))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookGenreInput = QLineEdit(self.frame_6)
        self.bookGenreInput.setObjectName(u"bookGenreInput")
        sizePolicy.setHeightForWidth(self.bookGenreInput.sizePolicy().hasHeightForWidth())
        self.bookGenreInput.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.bookGenreInput)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.groupBox_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 80))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookLanguageInput = QLineEdit(self.frame_7)
        self.bookLanguageInput.setObjectName(u"bookLanguageInput")
        sizePolicy.setHeightForWidth(self.bookLanguageInput.sizePolicy().hasHeightForWidth())
        self.bookLanguageInput.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.bookLanguageInput)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.groupBox_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 80))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignBottom)

        self.bookDescriptionInput = QLineEdit(self.frame_8)
        self.bookDescriptionInput.setObjectName(u"bookDescriptionInput")
        sizePolicy.setHeightForWidth(self.bookDescriptionInput.sizePolicy().hasHeightForWidth())
        self.bookDescriptionInput.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.bookDescriptionInput)


        self.verticalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_12.addWidget(self.groupBox_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(0, 60))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBookButton = QPushButton(self.frame_11)
        self.cancelBookButton.setObjectName(u"cancelBookButton")
        self.cancelBookButton.setMinimumSize(QSize(100, 0))
        self.cancelBookButton.setFont(font2)
        self.cancelBookButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(255,255,255,200); }\n"
"QPushButton:pressed { background: rgba(255,255,255,150); }")

        self.horizontalLayout_2.addWidget(self.cancelBookButton)

        self.addStockButton = QPushButton(self.frame_11)
        self.addStockButton.setObjectName(u"addStockButton")
        self.addStockButton.setMinimumSize(QSize(100, 0))
        self.addStockButton.setFont(font2)
        self.addStockButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(255,255,255,200); }\n"
"QPushButton:pressed { background: rgba(255,255,255,150); }")

        self.horizontalLayout_2.addWidget(self.addStockButton)

        self.createBookButton = QPushButton(self.frame_11)
        self.createBookButton.setObjectName(u"createBookButton")
        self.createBookButton.setMinimumSize(QSize(100, 0))
        self.createBookButton.setFont(font2)
        self.createBookButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #3B82F6; color: #FFF; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(59,130,246,200); }\n"
"QPushButton:pressed { background: rgba(59,130,246,150); }")

        self.horizontalLayout_2.addWidget(self.createBookButton)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.dialogVerticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Book", None))
        self.bookFormDialogTitle.setText(QCoreApplication.translate("Dialog", u"Create Book", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Cover", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"Upload Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Required", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ISBN", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Publisher", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Additional Information", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Publication Year", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Genre", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Language", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.cancelBookButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.addStockButton.setText(QCoreApplication.translate("Dialog", u"Add Stock", None))
        self.createBookButton.setText(QCoreApplication.translate("Dialog", u"Create", None))
    # retranslateUi

