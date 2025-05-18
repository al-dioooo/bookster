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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(800, 600))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background: #FFF;\n"
"	border-radius: 12px;\n"
"	padding: 24px;\n"
"}")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout = QVBoxLayout(self.startPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.startPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(500, 0))
        font = QFont()
        font.setFamilies([u"Magic Retro"])
        font.setPointSize(128)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.frame = QFrame(self.startPage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 0))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainButton = QPushButton(self.frame)
        self.mainButton.setObjectName(u"mainButton")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(16)
        self.mainButton.setFont(font1)
        self.mainButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background: #93C5FD;\n"
"	color: white;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.mainButton)

        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFont(font1)
        self.loginButton.setMouseTracking(True)
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background: #3B82F6;\n"
"	color: white;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(59, 130, 246, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgba(59, 130, 246, 150);\n"
"}")
        self.loginButton.setCheckable(False)
        self.loginButton.setChecked(False)

        self.horizontalLayout.addWidget(self.loginButton)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.startPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.frame_8 = QFrame(self.historyPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(20, 180, 728, 64))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	margin:0;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.searchHistoryInput = QLineEdit(self.frame_8)
        self.searchHistoryInput.setObjectName(u"searchHistoryInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchHistoryInput.sizePolicy().hasHeightForWidth())
        self.searchHistoryInput.setSizePolicy(sizePolicy1)
        self.searchHistoryInput.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(14)
        self.searchHistoryInput.setFont(font2)
        self.searchHistoryInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")
        self.searchHistoryInput.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.searchHistoryInput)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.addHistoryButton = QToolButton(self.frame_8)
        self.addHistoryButton.setObjectName(u"addHistoryButton")
        self.addHistoryButton.setMinimumSize(QSize(36, 36))
        self.addHistoryButton.setFont(font1)
        self.addHistoryButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 3px solid #DBEAFE;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.addHistoryButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.addHistoryButton, 0, Qt.AlignmentFlag.AlignRight)

        self.layoutWidget_4 = QWidget(self.historyPage)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 14, 728, 156))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.userPageTitle_2 = QLabel(self.layoutWidget_4)
        self.userPageTitle_2.setObjectName(u"userPageTitle_2")
        font3 = QFont()
        font3.setFamilies([u"Magic Retro"])
        font3.setPointSize(48)
        self.userPageTitle_2.setFont(font3)
        self.userPageTitle_2.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout_16.addWidget(self.userPageTitle_2)

        self.userPageDescription_2 = QLabel(self.layoutWidget_4)
        self.userPageDescription_2.setObjectName(u"userPageDescription_2")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(18)
        self.userPageDescription_2.setFont(font4)

        self.verticalLayout_16.addWidget(self.userPageDescription_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.historyPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_9 = QVBoxLayout(self.mainPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.mainPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.greetingsLabel = QLabel(self.frame_9)
        self.greetingsLabel.setObjectName(u"greetingsLabel")
        self.greetingsLabel.setFont(font3)
        self.greetingsLabel.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout_3.addWidget(self.greetingsLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.roleLabel = QLabel(self.frame_9)
        self.roleLabel.setObjectName(u"roleLabel")
        self.roleLabel.setFont(font4)

        self.verticalLayout_3.addWidget(self.roleLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.mainLogoutButton = QToolButton(self.frame_9)
        self.mainLogoutButton.setObjectName(u"mainLogoutButton")
        self.mainLogoutButton.setFont(font1)
        self.mainLogoutButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 3px solid #DBEAFE;\n"
"	padding: 3px 3px 3px 6px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.mainLogoutButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_7.addWidget(self.mainLogoutButton, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.mainPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.bookManagementLinkButton = QToolButton(self.frame_2)
        self.bookManagementLinkButton.setObjectName(u"bookManagementLinkButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bookManagementLinkButton.sizePolicy().hasHeightForWidth())
        self.bookManagementLinkButton.setSizePolicy(sizePolicy2)
        self.bookManagementLinkButton.setMinimumSize(QSize(150, 150))
        self.bookManagementLinkButton.setMaximumSize(QSize(150, 150))
        self.bookManagementLinkButton.setBaseSize(QSize(150, 150))
        self.bookManagementLinkButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 6px solid #DBEAFE;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.bookManagementLinkButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_6.addWidget(self.bookManagementLinkButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.userManagementLinkButton = QToolButton(self.frame_3)
        self.userManagementLinkButton.setObjectName(u"userManagementLinkButton")
        sizePolicy2.setHeightForWidth(self.userManagementLinkButton.sizePolicy().hasHeightForWidth())
        self.userManagementLinkButton.setSizePolicy(sizePolicy2)
        self.userManagementLinkButton.setMinimumSize(QSize(150, 150))
        self.userManagementLinkButton.setMaximumSize(QSize(150, 150))
        self.userManagementLinkButton.setBaseSize(QSize(150, 150))
        self.userManagementLinkButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 6px solid #DBEAFE;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.userManagementLinkButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_7.addWidget(self.userManagementLinkButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.historyLinkButton = QToolButton(self.frame_4)
        self.historyLinkButton.setObjectName(u"historyLinkButton")
        sizePolicy2.setHeightForWidth(self.historyLinkButton.sizePolicy().hasHeightForWidth())
        self.historyLinkButton.setSizePolicy(sizePolicy2)
        self.historyLinkButton.setMinimumSize(QSize(150, 150))
        self.historyLinkButton.setMaximumSize(QSize(150, 150))
        self.historyLinkButton.setBaseSize(QSize(150, 150))
        self.historyLinkButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 6px solid #DBEAFE;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.historyLinkButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_8.addWidget(self.historyLinkButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.mainPage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_4 = QVBoxLayout(self.loginPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loginTitleLabel = QLabel(self.loginPage)
        self.loginTitleLabel.setObjectName(u"loginTitleLabel")
        font5 = QFont()
        font5.setFamilies([u"Magic Retro"])
        font5.setPointSize(64)
        self.loginTitleLabel.setFont(font5)
        self.loginTitleLabel.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout_4.addWidget(self.loginTitleLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.usernameAndPasswordFrame = QFrame(self.loginPage)
        self.usernameAndPasswordFrame.setObjectName(u"usernameAndPasswordFrame")
        self.usernameAndPasswordFrame.setMinimumSize(QSize(500, 0))
        self.usernameAndPasswordFrame.setMaximumSize(QSize(500, 16777215))
        self.usernameAndPasswordFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.usernameAndPasswordFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.usernameAndPasswordFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usernameLabel = QLabel(self.usernameAndPasswordFrame)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(0, 0))
        self.usernameLabel.setMaximumSize(QSize(16777215, 20))
        self.usernameLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.usernameLabel, 0, Qt.AlignmentFlag.AlignBottom)

        self.usernameInput = QLineEdit(self.usernameAndPasswordFrame)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setFont(font1)
        self.usernameInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 12px;\n"
"	border-radius: 12px;\n"
"	border: 6px solid #DBEAFE;\n"
"}")

        self.verticalLayout_2.addWidget(self.usernameInput)

        self.passwordLabel = QLabel(self.usernameAndPasswordFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setMaximumSize(QSize(16777215, 20))
        self.passwordLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.passwordLabel)

        self.passwordInput = QLineEdit(self.usernameAndPasswordFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font1)
        self.passwordInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 12px;\n"
"	border-radius: 12px;\n"
"	border: 6px solid #DBEAFE;\n"
"}")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.passwordInput)


        self.verticalLayout_4.addWidget(self.usernameAndPasswordFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.submitLoginFrame = QFrame(self.loginPage)
        self.submitLoginFrame.setObjectName(u"submitLoginFrame")
        self.submitLoginFrame.setMinimumSize(QSize(500, 0))
        self.submitLoginFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.submitLoginFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.submitLoginFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.submitLoginButton = QPushButton(self.submitLoginFrame)
        self.submitLoginButton.setObjectName(u"submitLoginButton")
        self.submitLoginButton.setMaximumSize(QSize(16777215, 16777215))
        self.submitLoginButton.setFont(font1)
        self.submitLoginButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background: #3B82F6;\n"
"	color: white;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgba(59, 130, 246, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgba(59, 130, 246, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.submitLoginButton, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_4.addWidget(self.submitLoginFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.loginPage)
        self.bookManagementPage = QWidget()
        self.bookManagementPage.setObjectName(u"bookManagementPage")
        self.verticalLayout_12 = QVBoxLayout(self.bookManagementPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_10 = QFrame(self.bookManagementPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 40))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bookManagementBackButton = QToolButton(self.frame_10)
        self.bookManagementBackButton.setObjectName(u"bookManagementBackButton")
        self.bookManagementBackButton.setMinimumSize(QSize(40, 40))
        self.bookManagementBackButton.setMaximumSize(QSize(40, 40))
        self.bookManagementBackButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 3px solid #DBEAFE;\n"
"	padding: 3px 3px 3px 6px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.bookManagementBackButton.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.bookManagementBackButton)


        self.verticalLayout_12.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.bookPageTitle = QLabel(self.bookManagementPage)
        self.bookPageTitle.setObjectName(u"bookPageTitle")
        self.bookPageTitle.setFont(font3)
        self.bookPageTitle.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout_10.addWidget(self.bookPageTitle)

        self.bookPageDescription = QLabel(self.bookManagementPage)
        self.bookPageDescription.setObjectName(u"bookPageDescription")
        self.bookPageDescription.setFont(font4)

        self.verticalLayout_10.addWidget(self.bookPageDescription)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.frame_6 = QFrame(self.bookManagementPage)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	margin:0;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.searchBookInput = QLineEdit(self.frame_6)
        self.searchBookInput.setObjectName(u"searchBookInput")
        sizePolicy1.setHeightForWidth(self.searchBookInput.sizePolicy().hasHeightForWidth())
        self.searchBookInput.setSizePolicy(sizePolicy1)
        self.searchBookInput.setMaximumSize(QSize(300, 16777215))
        self.searchBookInput.setFont(font2)
        self.searchBookInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")
        self.searchBookInput.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.searchBookInput)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.addBookButton = QToolButton(self.frame_6)
        self.addBookButton.setObjectName(u"addBookButton")
        self.addBookButton.setMinimumSize(QSize(36, 36))
        self.addBookButton.setFont(font1)
        self.addBookButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 3px solid #DBEAFE;\n"
"	padding: 3px 3px 3px 6px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.addBookButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_4.addWidget(self.addBookButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.bookListScrollArea = QScrollArea(self.bookManagementPage)
        self.bookListScrollArea.setObjectName(u"bookListScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.bookListScrollArea.sizePolicy().hasHeightForWidth())
        self.bookListScrollArea.setSizePolicy(sizePolicy3)
        self.bookListScrollArea.setStyleSheet(u"QScrollArea {\n"
"	background: #FFF;\n"
"	border-radius: 16px;\n"
"	border: 2px solid #E5E5E5;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: none\n"
"}")
        self.bookListScrollArea.setWidgetResizable(True)
        self.bookListScrollAreaWidgetContents = QWidget()
        self.bookListScrollAreaWidgetContents.setObjectName(u"bookListScrollAreaWidgetContents")
        self.bookListScrollAreaWidgetContents.setGeometry(QRect(0, 0, 724, 226))
        self.verticalLayout_11 = QVBoxLayout(self.bookListScrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.bookListScrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_11.addWidget(self.widget)

        self.bookListScrollArea.setWidget(self.bookListScrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.bookListScrollArea)

        self.stackedWidget.addWidget(self.bookManagementPage)
        self.userManagementPage = QWidget()
        self.userManagementPage.setObjectName(u"userManagementPage")
        self.verticalLayout_15 = QVBoxLayout(self.userManagementPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.userPageTitle = QLabel(self.userManagementPage)
        self.userPageTitle.setObjectName(u"userPageTitle")
        self.userPageTitle.setFont(font3)
        self.userPageTitle.setStyleSheet(u"QLabel {\n"
"	color: #3B82F6;\n"
"}")

        self.verticalLayout_14.addWidget(self.userPageTitle)

        self.userPageDescription = QLabel(self.userManagementPage)
        self.userPageDescription.setObjectName(u"userPageDescription")
        self.userPageDescription.setFont(font4)

        self.verticalLayout_14.addWidget(self.userPageDescription)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.frame_7 = QFrame(self.userManagementPage)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	margin:0;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.searchUserInput = QLineEdit(self.frame_7)
        self.searchUserInput.setObjectName(u"searchUserInput")
        sizePolicy1.setHeightForWidth(self.searchUserInput.sizePolicy().hasHeightForWidth())
        self.searchUserInput.setSizePolicy(sizePolicy1)
        self.searchUserInput.setMaximumSize(QSize(300, 16777215))
        self.searchUserInput.setFont(font2)
        self.searchUserInput.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 12px;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #E5E5E5;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #DBEAFE;\n"
"}")
        self.searchUserInput.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.searchUserInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.addUserButton = QToolButton(self.frame_7)
        self.addUserButton.setObjectName(u"addUserButton")
        self.addUserButton.setMinimumSize(QSize(36, 36))
        self.addUserButton.setFont(font1)
        self.addUserButton.setStyleSheet(u"QToolButton {\n"
"	background: #93C5FD;\n"
"	color: #FFF;\n"
"	border-radius: 12px;\n"
"	border: 2px solid #DBEAFE;\n"
"	padding: 4px 4px 4px 7px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background: rgba(147, 197, 253, 200);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: rgba(147, 197, 253, 150);\n"
"}\n"
"\n"
"QToolButton QLabel {\n"
"	margin-left: 6px;\n"
"}")
        self.addUserButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_5.addWidget(self.addUserButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.userListScrollArea = QScrollArea(self.userManagementPage)
        self.userListScrollArea.setObjectName(u"userListScrollArea")
        sizePolicy3.setHeightForWidth(self.userListScrollArea.sizePolicy().hasHeightForWidth())
        self.userListScrollArea.setSizePolicy(sizePolicy3)
        self.userListScrollArea.setStyleSheet(u"QScrollArea {\n"
"	background: #FFF;\n"
"	border-radius: 16px;\n"
"	border: 2px solid #E5E5E5;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: none\n"
"}")
        self.userListScrollArea.setWidgetResizable(True)
        self.userListScrollAreaWidgetContents = QWidget()
        self.userListScrollAreaWidgetContents.setObjectName(u"userListScrollAreaWidgetContents")
        self.userListScrollAreaWidgetContents.setGeometry(QRect(0, 0, 72, 16))
        self.verticalLayout_13 = QVBoxLayout(self.userListScrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.userListScrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_13.addWidget(self.widget_2)

        self.userListScrollArea.setWidget(self.userListScrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.userListScrollArea)

        self.stackedWidget.addWidget(self.userManagementPage)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bookster", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Bookster</p></body></html>", None))
        self.mainButton.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.searchHistoryInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search History Data", None))
        self.addHistoryButton.setText(QCoreApplication.translate("MainWindow", u"Borrow", None))
        self.userPageTitle_2.setText(QCoreApplication.translate("MainWindow", u"Loan History", None))
        self.userPageDescription_2.setText(QCoreApplication.translate("MainWindow", u"3 Data Available", None))
        self.greetingsLabel.setText(QCoreApplication.translate("MainWindow", u"Hey, there!", None))
        self.roleLabel.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.mainLogoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.bookManagementLinkButton.setText(QCoreApplication.translate("MainWindow", u"Book", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Book", None))
        self.userManagementLinkButton.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.historyLinkButton.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.loginTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.submitLoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.bookManagementBackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.bookPageTitle.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.bookPageDescription.setText(QCoreApplication.translate("MainWindow", u"18 Books Available", None))
        self.searchBookInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book Data", None))
        self.addBookButton.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.userPageTitle.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.userPageDescription.setText(QCoreApplication.translate("MainWindow", u"18 User Available", None))
        self.searchUserInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search User Data", None))
        self.addUserButton.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
    # retranslateUi

