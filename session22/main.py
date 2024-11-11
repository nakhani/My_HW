import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIcon, QPixmap
from ui_mainwindow import Ui_MainWindow
from database import Database
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()
        self.ui.btn.clicked.connect(self.new_task)

        self.ui.tb_new_task_description.setPlaceholderText("Description")
        self.ui.tb_new_task.setPlaceholderText("Title")
        self.ui.lineEdit.setPlaceholderText("YY/MM/DD")
        self.ui.btn.setFlat(True) 
        
        self.set_background_image("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session22/images/IMG_3154.JPG") 


    def set_background_image(self, image_path): 
        self.setStyleSheet(f""" 
                        QMainWindow {{ 
                           background-image: url({image_path}); 
                           background-repeat: no-repeat; 
                           background-position: center; 
                           background-size: 736px 1165px;
                           }} 
                      """)

    def read_from_database(self):

        tasks = self.db.get_task()
        tasks = sorted(tasks, key=lambda task: task[3])

        for i in reversed(range(self.ui.gl_task.count())): 
            widget = self.ui.gl_task.itemAt(i).widget() 
            if widget is not None: 
               widget.setParent(None)


        for i in range (len(tasks)):

            new_checkbox = QCheckBox()
            new_btn = QPushButton()
            new_btn2 = QPushButton()
            new_checkbox.setText(tasks[i][1])
            new_btn.setIcon(QIcon("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session22/images/clipart890862.png"))
            new_btn2.setIcon(QIcon("C:/Users/Dr.Laptop/Desktop/python_class/My_HW\session22/images/—Pngtree—vector information icon_3785582.png"))

            new_btn2.setFixedSize(20, 21)
            new_btn.setFixedSize(40, 21)

            new_btn.setFlat(True) 
            new_btn2.setFlat(True)
            

            if tasks[i][3]:
              new_checkbox.setChecked(True)
              new_checkbox.setStyleSheet("color: rgb(60,60,60);text-decoration: line-through;")

            if tasks[i][4]:
              new_checkbox.setStyleSheet("color: red;")

            self.ui.gl_task.addWidget(new_checkbox, i, 0)
            self.ui.gl_task.addWidget(new_btn2, i, 1)
            self.ui.gl_task.addWidget(new_btn, i, 2)
            
            new_checkbox.stateChanged.connect(lambda _, task= tasks[i]: self.update_task(task[1]))      
            new_btn.clicked.connect(partial(self.remove_task,tasks[i][1]))
            
            new_btn2.clicked.connect(partial(self.show_task_info, tasks[i][2], tasks[i][5]))
       
            
        
    def update_task(self,title):
        self.db.update_task(title)
        self.read_from_database()
        
    def show_task_info(self, message1, message2): 
        msg_box = QMessageBox() 
        msg_box.setText(f"{message2} \n{message1}") 
        msg_box.setDetailedText(message1) 
        msg_box.exec_()        

    def remove_task(self, title): 
        self.db.remove_task(title)
        self.read_from_database()

    def new_task(self):
        new_title = self.ui.tb_new_task.text()
        new_date = self.ui.lineEdit.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        feedback = self.db.add_new_task(new_title, new_description, new_date)
        if feedback == True:
            self.read_from_database()
            self.ui.tb_new_task.setText("")
            self.ui.lineEdit.setText("")
            self.ui.tb_new_task_description.setText("")
        else:
            msg_box = QMessageBox()
            msg_box.setText("Unsuccessful, Please Try Again!")
            msg_box.exec_()


if __name__ == "__main__":
   
   app = QApplication(sys.argv)

   main_window = MainWindow()
   main_window.show()

   app.exec_()