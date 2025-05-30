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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(824, 624)
        self.bookDetailPageTitle = QLabel(Form)
        self.bookDetailPageTitle.setObjectName(u"bookDetailPageTitle")
        self.bookDetailPageTitle.setGeometry(QRect(40, 40, 271, 51))
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(48)
        self.bookDetailPageTitle.setFont(font)
        self.bookDetailPageTitle.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bookDetailPageTitle.setText(QCoreApplication.translate("Form", u"Book Detail", None))
    # retranslateUi

