# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_BookDetailDialog(object):
    def setupUi(self, BookDetailDialog):
        if not BookDetailDialog.objectName():
            BookDetailDialog.setObjectName(u"BookDetailDialog")
        BookDetailDialog.resize(480, 720)
        self.verticalLayout_3 = QVBoxLayout(BookDetailDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(BookDetailDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 478, 718))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame#frame_3 {\n"
"	background: #FFF;\n"
"	border-radius: 12px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bookDetailTitleLabel = QLabel(self.frame_3)
        self.bookDetailTitleLabel.setObjectName(u"bookDetailTitleLabel")
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(48)
        self.bookDetailTitleLabel.setFont(font)
        self.bookDetailTitleLabel.setStyleSheet(u"QLabel { color: #3B82F6; }")

        self.verticalLayout_2.addWidget(self.bookDetailTitleLabel)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bookCoverLabel = QLabel(self.frame_2)
        self.bookCoverLabel.setObjectName(u"bookCoverLabel")
        self.bookCoverLabel.setMinimumSize(QSize(140, 180))
        self.bookCoverLabel.setStyleSheet(u"image: url(:/assets/images/placeholder.png);\n"
"QLabel {\n"
"  border-radius: 12px;\n"
"  border: 3px solid #F5F5F5;\n"
"}")

        self.horizontalLayout.addWidget(self.bookCoverLabel)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(14)
        self.frame.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.frame)
        self.titleLabel.setObjectName(u"titleLabel")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(18)
        font2.setWeight(QFont.DemiBold)
        self.titleLabel.setFont(font2)

        self.verticalLayout.addWidget(self.titleLabel)

        self.authorLabel = QLabel(self.frame)
        self.authorLabel.setObjectName(u"authorLabel")

        self.verticalLayout.addWidget(self.authorLabel)

        self.publisherLabel = QLabel(self.frame)
        self.publisherLabel.setObjectName(u"publisherLabel")

        self.verticalLayout.addWidget(self.publisherLabel)

        self.yearLabel = QLabel(self.frame)
        self.yearLabel.setObjectName(u"yearLabel")

        self.verticalLayout.addWidget(self.yearLabel)

        self.genreLabel = QLabel(self.frame)
        self.genreLabel.setObjectName(u"genreLabel")

        self.verticalLayout.addWidget(self.genreLabel)

        self.languageLabel = QLabel(self.frame)
        self.languageLabel.setObjectName(u"languageLabel")

        self.verticalLayout.addWidget(self.languageLabel)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.descriptionLabel = QLabel(self.frame_3)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        self.descriptionLabel.setFont(font3)

        self.verticalLayout_2.addWidget(self.descriptionLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.stockListButton = QPushButton(self.frame_4)
        self.stockListButton.setObjectName(u"stockListButton")
        self.stockListButton.setMinimumSize(QSize(100, 0))
        self.stockListButton.setFont(font3)
        self.stockListButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #E5E5E5; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(229,229,229,200); }\n"
"QPushButton:pressed { background: rgba(229,229,229,150); }")

        self.horizontalLayout_2.addWidget(self.stockListButton)

        self.closeButton = QPushButton(self.frame_4)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(100, 0))
        self.closeButton.setFont(font3)
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"  border-radius: 12px; background: #E5E5E5; padding: 6px;\n"
"}\n"
"QPushButton:hover   { background: rgba(229,229,229,200); }\n"
"QPushButton:pressed { background: rgba(229,229,229,150); }")

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(BookDetailDialog)

        QMetaObject.connectSlotsByName(BookDetailDialog)
    # setupUi

    def retranslateUi(self, BookDetailDialog):
        BookDetailDialog.setWindowTitle(QCoreApplication.translate("BookDetailDialog", u"Book Detail", None))
        self.bookDetailTitleLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Book Detail", None))
        self.bookCoverLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Book Title", None))
        self.authorLabel.setText(QCoreApplication.translate("BookDetailDialog", u"by Author", None))
        self.publisherLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Publisher", None))
        self.yearLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Year", None))
        self.genreLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Genre", None))
        self.languageLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Language", None))
        self.descriptionLabel.setText(QCoreApplication.translate("BookDetailDialog", u"Description", None))
        self.stockListButton.setText(QCoreApplication.translate("BookDetailDialog", u"Stock List", None))
        self.closeButton.setText(QCoreApplication.translate("BookDetailDialog", u"Close", None))
    # retranslateUi

