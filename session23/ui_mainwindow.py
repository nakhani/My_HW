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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 436)
        icon = QIcon()
        icon.addFile(u"C:/Users/Dr.Laptop/Desktop/python_class/My_HW\session23/images/unnamed.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.new_game = QAction(MainWindow)
        self.new_game.setObjectName(u"new_game")
        self.open_file = QAction(MainWindow)
        self.open_file.setObjectName(u"open_file")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.Help = QAction(MainWindow)
        self.Help.setObjectName(u"Help")
        self.about_2 = QAction(MainWindow)
        self.about_2.setObjectName(u"about_2")
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.exit = QAction(MainWindow)
        self.exit.setObjectName(u"exit")
        self.solve_puzzle = QAction(MainWindow)
        self.solve_puzzle.setObjectName(u"solve_puzzle")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gl_game = QGridLayout()
        self.gl_game.setObjectName(u"gl_game")

        self.gridLayout.addLayout(self.gl_game, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 427, 22))
        self.menuNew_Game = QMenu(self.menubar)
        self.menuNew_Game.setObjectName(u"menuNew_Game")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        self.menuSolve = QMenu(self.menubar)
        self.menuSolve.setObjectName(u"menuSolve")
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNew_Game.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuSolve.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menuNew_Game.addAction(self.new_game)
        self.menuNew_Game.addAction(self.open_file)
        self.menuAbout.addAction(self.about_2)
        self.menuHelp.addAction(self.help)
        self.menuExit.addAction(self.exit)
        self.menuSolve.addAction(self.solve_puzzle)
        self.menuMode.addAction(self.actionDark)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SUDOKU", None))
        self.new_game.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.Help.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.about_2.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.solve_puzzle.setText(QCoreApplication.translate("MainWindow", u"solve puzzle", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.menuNew_Game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuSolve.setTitle(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
    # retranslateUi

