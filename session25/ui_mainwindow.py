# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 377)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(70, 70, 70, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush2 = QBrush(QColor(255, 69, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(150, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Active, QPalette.Link, brush4)
        brush5 = QBrush(QColor(40, 40, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(66, 66, 66);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(66, 66, 66, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush4)
        brush7 = QBrush(QColor(100, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.LinkVisited, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.tabWidget.setPalette(palette1)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 541, 231))
        self.label_2.setPixmap(QPixmap(u"photos/favpng_world-clock-world-map-newgate-clocks.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 230, 171, 111))
        font = QFont()
        font.setFamilies([u"Eras Bold ITC"])
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 230, 181, 111))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 230, 171, 111))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.ln_1 = QLineEdit(self.tab_2)
        self.ln_1.setObjectName(u"ln_1")
        self.ln_1.setGeometry(QRect(310, 110, 61, 51))
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(50)
        self.ln_1.setFont(font1)
        self.ln_1.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ln_1.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.ln_1.setFrame(False)
        self.ln_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ln_1.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.ln_1.setClearButtonEnabled(False)
        self.ln_3 = QLineEdit(self.tab_2)
        self.ln_3.setObjectName(u"ln_3")
        self.ln_3.setGeometry(QRect(180, 110, 61, 51))
        self.ln_3.setFont(font1)
        self.ln_3.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.ln_3.setFrame(False)
        self.ln_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ln_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.ln_3.setClearButtonEnabled(False)
        self.ln_2 = QLineEdit(self.tab_2)
        self.ln_2.setObjectName(u"ln_2")
        self.ln_2.setGeometry(QRect(240, 110, 61, 51))
        self.ln_2.setFont(font1)
        self.ln_2.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.ln_2.setFrame(False)
        self.ln_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ln_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.ln_2.setClearButtonEnabled(False)
        self.btn_start_timer = QPushButton(self.tab_2)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(130, 280, 91, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.btn_start_timer.setFont(font2)
        self.btn_start_timer.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.btn_reset_timer = QPushButton(self.tab_2)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(330, 280, 91, 41))
        self.btn_reset_timer.setFont(font2)
        self.btn_reset_timer.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.btn_stop_timer = QPushButton(self.tab_2)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(230, 280, 91, 41))
        self.btn_stop_timer.setFont(font2)
        self.btn_stop_timer.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 10, 251, 251))
        self.label_6.setPixmap(QPixmap(u"photos/clipart1866295.png"))
        self.label_6.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_6.raise_()
        self.ln_3.raise_()
        self.ln_1.raise_()
        self.ln_2.raise_()
        self.btn_start_timer.raise_()
        self.btn_reset_timer.raise_()
        self.btn_stop_timer.raise_()
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 10, 121, 101))
        font3 = QFont()
        font3.setPointSize(86)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton.setFlat(True)
        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 71, 61))
        font4 = QFont()
        font4.setFamilies([u"Seven Segment"])
        font4.setPointSize(40)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 10, 71, 61))
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 90, 421, 22))
        font5 = QFont()
        font5.setPointSize(12)
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_3.setFrame(False)
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 140, 541, 201))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 20, 20, 51))
        font6 = QFont()
        font6.setPointSize(18)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 120, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.tab_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 70, 431, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.btn_start = QPushButton(self.tab_4)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(130, 280, 91, 41))
        self.btn_start.setFont(font2)
        self.btn_start.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.btn_stop = QPushButton(self.tab_4)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(230, 280, 91, 41))
        self.btn_stop.setFont(font2)
        self.btn_stop.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 110, 181, 51))
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(150, 0, 24);")
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_reset = QPushButton(self.tab_4)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(330, 280, 91, 41))
        self.btn_reset.setFont(font2)
        self.btn_reset.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 10, 251, 251))
        self.label_7.setPixmap(QPixmap(u"photos/clipart1866295.png"))
        self.label_7.setScaledContents(True)
        self.tabWidget.addTab(self.tab_4, "")
        self.label_7.raise_()
        self.btn_start.raise_()
        self.btn_stop.raise_()
        self.label.raise_()
        self.btn_reset.raise_()

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.btn_start_timer.setDefault(False)
        self.btn_start.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Timer", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_7.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"StopWatch", None))
    # retranslateUi

