from PySide6.QtCore import QThread, Signal
from datetime import datetime
import pytz

class WorldClockThread(QThread):
    signal_clock = Signal(str, str, str)

    def __init__(self, city, country, timezone):
        super().__init__()
        self.city = city
        self.country = country
        self.timezone = timezone
        self.emit_current_time()

    def emit_current_time(self):
        city_time = datetime.now(pytz.timezone(self.timezone)).strftime("%Y-%m-%d %H:%M:%S")
        self.signal_clock.emit(self.city, self.country, city_time)

    def run(self):
        while True:
            self.emit_current_time()
            QThread.sleep(1)
