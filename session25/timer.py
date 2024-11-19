import sys
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import *
from PySide6.QtGui import * 
from PySide6.QtCore import * 
from mtime import MyTime



class TimerThread(QThread):
    signal_timer = Signal(MyTime)

    def __init__(self, hour, minute, second):
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = MyTime(self.hour,self.minute,self.second)


    def run(self):
        while True:
           self.time.minus()
           self.signal_timer.emit(self.time)
           time.sleep(1)

    def reset(self):
        self.time = MyTime(self.hour,self.minute,self.second)
