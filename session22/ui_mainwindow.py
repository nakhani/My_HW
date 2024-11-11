# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(347, 424)
        font = QFont()
        font.setPointSize(29)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 213, 213);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_new_task = QLineEdit(self.centralwidget)
        self.tb_new_task.setObjectName(u"tb_new_task")
        font1 = QFont()
        font1.setPointSize(14)
        self.tb_new_task.setFont(font1)
        self.tb_new_task.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.tb_new_task)

        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        font2 = QFont()
        font2.setPointSize(24)
        self.btn.setFont(font2)
        icon = QIcon()
        icon.addFile(u"C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session22/images/clipart3001834.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn.setIcon(icon)
        self.btn.setIconSize(QSize(48, 24))

        self.horizontalLayout.addWidget(self.btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.tb_new_task_description)

        self.gl_task = QGridLayout()
        self.gl_task.setObjectName(u"gl_task")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gl_task.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gl_task.addWidget(self.label_2, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gl_task)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn.setText("")
        self.label_3.setText("")
        self.label_2.setText("")
    # retranslateUi

