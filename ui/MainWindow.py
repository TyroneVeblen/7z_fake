# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(311, 345)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(198, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.select_folder_button = QPushButton(self.centralwidget)
        self.select_folder_button.setObjectName(u"select_folder_button")

        self.horizontalLayout.addWidget(self.select_folder_button)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.horizontalLayout_3.addWidget(self.start)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 311, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6062\u590d", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939:", None))
        self.select_folder_button.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u6b22\u8fce\u4f7f\u7528\u6b64\u8f6f\u4ef6\uff01<br />\u6b64\u8f6f\u4ef6\u4f1a\u5c1d\u8bd5\u4fee\u6539\u6240\u67097z\u6587\u4ef6\u7684\u6587\u4ef6\u5934\uff0c\u4f7f\u5f97\u6587\u4ef6\u65e0\u6cd5\u88ab\u5728\u7ebf\u89e3\u538b\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u8bf7\u9009\u62e9\u6587\u4ef6\u6240\u5728\u7684\u6587\u4ef6\u5939\uff08\u4e0d\u5fc5\u62c5\u5fc3\u4e00\u822c\u6587\u4ef6\u88ab\u4fee\u6539"
                        "\uff0c\u6b64\u8f6f\u4ef6\u4f1a\u81ea\u52a8\u8bc6\u522b\uff09</span></p></body></html>", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

