import sys
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import *
from PySide6.QtGui import * 
from PySide6.QtCore import * 
from mtime import MyTime



class StopWatchThread(QThread):
    signal_stopwatch = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0,0,0)


    def run(self):
        while True:
           self.time.plus()
           self.signal_stopwatch.emit(self.time)
           time.sleep(1)

    def reset(self):
        self.time = MyTime(0,0,0)
