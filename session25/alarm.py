# alarm_manager.py
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from datetime import datetime
from database import DatabaseManager
from functools import partial

class AlarmThread:
    def __init__(self, ui):
        self.ui = ui
        self.db = DatabaseManager()
        self.load_alarms()
        self.ui.pushButton.clicked.connect(self.add_alarm)
        self.ui.lineEdit.setPlaceholderText("00")
        self.ui.lineEdit_2.setPlaceholderText("00")
        self.ui.lineEdit_3.setPlaceholderText("TEXT")
        
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.check_alarms)
        self.alarm_timer.start(1000)  # Check every second


    def load_alarms(self):
        
        
        for i in reversed(range(self.ui.gridLayout_2.count())): 
            widget_to_remove = self.ui.gridLayout_2.itemAt(i).widget() 
            if widget_to_remove is not None: 
                widget_to_remove.setParent(None) 

        alarms = self.db.get_alarms()       
        
        for i in range(len(alarms)):
            new_label = QLineEdit()
            new_label2 = QLineEdit()
            new_label3 = QLineEdit()
            new_label4 = QLabel()
            new_btn = QPushButton()
            new_btn2 = QPushButton()
            new_label.setText(alarms[i][1])
            new_label2.setText(alarms[i][2])
            new_label3.setText(alarms[i][3])
            new_label4.setText(":")

            new_label.setFrame(False) 
            new_label.setReadOnly(True) 
            new_label2.setFrame(False) 
            new_label2.setReadOnly(True) 
            new_label3.setFrame(False) 
            new_label3.setReadOnly(True)

            
            font_clock = QFont("Seven Segment",25) 
            font_text = QFont() 
            font_text.setPointSize(9) 
            new_label.setFont(font_clock) 
            new_label2.setFont(font_clock) 
            new_label3.setFont(font_text)
            new_label4.setFont(font_clock) 
            new_label.setAlignment(Qt.AlignCenter) 
            new_label2.setAlignment(Qt.AlignCenter)
            new_label4.setAlignment(Qt.AlignCenter)
            new_label.setFixedSize(60,30) 
            new_label2.setFixedSize(60,30)
            new_label4.setFixedSize(30,30)
            new_label3.setFixedSize(320,30)

            new_btn.setIcon(QIcon("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session25/photos/—Pngtree—delete icon_4490395.png"))
            new_btn2.setIcon(QIcon("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session25/photos/—Pngtree—white edit icon_4559214.png"))

            new_btn2.setFixedSize(40, 30)
            new_btn.setFixedSize(40, 30)
            

            self.ui.gridLayout_2.addWidget(new_label, i, 0)
            self.ui.gridLayout_2.addWidget(new_label4, i, 1)
            self.ui.gridLayout_2.addWidget(new_label2, i, 2)
            self.ui.gridLayout_2.addWidget(new_label3, i, 3)
            self.ui.gridLayout_2.addWidget(new_btn2, i, 4)
            self.ui.gridLayout_2.addWidget(new_btn, i, 5)
            
          


            new_btn.clicked.connect(partial(self.remove_alarm,alarms[i][0]))
            new_btn2.clicked.connect(partial(self.edit_alarm, alarms[i], new_label,new_label2,new_label3,i))
            

    def add_alarm(self):
        new_hour = self.ui.lineEdit.text()
        new_minute = self.ui.lineEdit_2.text()
        new_text = self.ui.lineEdit_3.text()
        feedback = self.db.add_alarm(new_hour, new_minute, new_text)
        print(feedback)

        if feedback == True:
            self.load_alarms()
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit_3.setText("")
        elif feedback == False:
            msg_box = QMessageBox()
            msg_box.setText("Unsuccessful, Please Try Again!")
            msg_box.exec_()

    def edit_alarm(self, alarm, new_label,new_label2, new_label3, i):

        
        new_label.setReadOnly(False)  
        new_label2.setReadOnly(False) 
        new_label3.setReadOnly(False)
        button_done = QPushButton("Done")
        button_done.setFixedSize(40, 30)

        self.ui.gridLayout_2.addWidget(button_done, i, 4)


        def save_changes(): 
            new_hour = new_label.text() 
            new_minute = new_label2.text() 
            new_text = new_label3.text() 
            self.db.update_alarm(alarm[0], new_hour, new_minute, new_text) 
            new_label.setReadOnly(True) 
            new_label2.setReadOnly(True) 
            new_label3.setReadOnly(True) 
            button_done.deleteLater() 
             
            self.load_alarms() 
           

        button_done.clicked.connect(save_changes)

    def remove_alarm(self, id):
        self.db.delete_alarm(id)
        self.load_alarms()

    def check_alarms(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        alarms = self.db.get_alarms()
        for alarm in alarms:
            if alarm[1] == current_time:
                # Show notification (for simplicity, we'll just print it)
                print(f"Alarm: {alarm[2]} at {alarm[1]}")
