import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from stopwatch import StopWatchThread
from ui_mainwindow import Ui_MainWindow
from timer import TimerThread
from clockworld import WorldClockThread
from alarm import AlarmThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

       
        self.apply_dark_cherry_theme()

        self.thread_stopwatch = StopWatchThread()
        self.thread_timer = None  

        self.ui.label.setText("0:0:0")
        self.ui.ln_1.setText("30")
        self.ui.ln_2.setText("15")
        self.ui.ln_3.setText("0")

        
        self.ui.btn_start.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop.clicked.connect(self.stop_stopwatch)
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        
        self.thread_stopwatch.signal_stopwatch.connect(self.show_number)

        cities = [
            ("Tehran", "🇮🇷 Iran", "Asia/Tehran"),
            ("Berlin", "🇩🇪 Germany", "Europe/Berlin"),
            ("New York", "🇺🇸 USA", "America/New_York")
        ]

        self.threads = []
        for city, country, timezone in cities:
            thread_clock = WorldClockThread(city, country, timezone)
            thread_clock.signal_clock.connect(self.update_time)
            self.threads.append(thread_clock)
            thread_clock.start()

        self.alarm_manager = AlarmThread(self.ui)

    def apply_dark_cherry_theme(self):
        dark_palette = self.create_dark_cherry_palette()
        QApplication.setPalette(dark_palette)
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def create_dark_cherry_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))  
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(0, 0, 0))  
        palette.setColor(QPalette.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(70, 70, 70))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, QColor(255, 69, 0)) 
        palette.setColor(QPalette.Highlight, QColor(150, 0, 0))  
        palette.setColor(QPalette.HighlightedText, Qt.white)
        palette.setColor(QPalette.Link, QColor(150, 0, 0))  
        palette.setColor(QPalette.LinkVisited, QColor(100, 0, 0))  
        return palette

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def stop_timer(self):
        if self.thread_timer:
            self.thread_timer.terminate()

    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def start_timer(self):
        self.thread_timer = TimerThread(int(self.ui.ln_3.text()), int(self.ui.ln_2.text()), int(self.ui.ln_1.text()))
        self.thread_timer.signal_timer.connect(self.show_number_timer)
        self.thread_timer.start()

    def reset(self):
        self.thread_stopwatch.reset()
        self.ui.label.setText("0:0:0")
        self.stop_stopwatch()

    def reset_timer(self):
        if self.thread_timer:
            self.thread_timer.reset()
        self.ui.ln_1.setText("30")
        self.ui.ln_2.setText("15")
        self.ui.ln_3.setText("0")
        self.stop_timer()
    
    def show_number(self, time):
        self.ui.label.setText(f"{time.hour}:{time.minute}:{time.second}")

    def show_number_timer(self, time):
        self.ui.ln_1.setText(f"{time.second}")
        self.ui.ln_2.setText(f"{time.minute}")
        self.ui.ln_3.setText(f"{time.hour}")

    def update_time(self, city, country, current_time):
        cherry_color = "#960018"  
        label_text = f'<span style="color:{cherry_color}">{city}, {country}</span><br><span style="font-size:12px;">{current_time}</span>'
        if city == "Tehran":
            self.ui.label_3.setText(label_text)
        elif city == "Berlin":
            self.ui.label_4.setText(label_text)
        elif city == "New York":
            self.ui.label_5.setText(label_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
