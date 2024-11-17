import os
from threading import Thread
from time import time
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QMessageBox
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fast Downloader")
        self.setGeometry(300, 300, 500, 300)

        # Set up the dark mode palette
        self.setPalette(self.create_dark_palette())

        layout = QVBoxLayout()

        self.label = QLabel("Enter the URLs (one per line):")
        layout.addWidget(self.label)

        self.url_input = QTextEdit()
        layout.addWidget(self.url_input)

        self.label_output = QLabel("Select the folder to save outputs:")
        layout.addWidget(self.label_output)

        self.select_output_button = QPushButton("Select Output Directory")
        self.select_output_button.clicked.connect(self.select_output_directory)
        layout.addWidget(self.select_output_button)

        self.process_button = QPushButton("Start Download")
        self.process_button.clicked.connect(self.start_process)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.output_directory = ""

        # Apply styling
        self.apply_styles()

    def create_dark_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(18, 18, 18))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(18, 18, 18))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        return palette

    def apply_styles(self):
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #FFFFFF;
            }
            QTextEdit, QLineEdit {
                background-color: #333333;
                color: #FFFFFF;
                border: 1px solid #555555;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #444444;
                color: #FFFFFF;
                border: 1px solid #555555;
                padding: 8px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        """)

    def select_output_directory(self):
        self.output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        self.label_output.setText(f"Output directory: {self.output_directory}")

    def start_process(self):
        if not self.output_directory:
            QMessageBox.warning(self, "Selection Error", "Please select an output directory.")
            return

        urls = self.url_input.toPlainText().strip().split('\n')
        if not urls or urls == ['']:
            QMessageBox.warning(self, "Input Error", "Please enter at least one URL.")
            return

        start_time = time()

        threads = []
        for idx, url in enumerate(urls):
            filename = os.path.join(self.output_directory, f"file_{idx+1}.bin")
            threads.append(Thread(target=self.download, args=[url, filename]))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        end_time = time()
        QMessageBox.information(self, "Download Completed", f"Downloaded {len(urls)} files in {end_time - start_time:.2f} seconds.")

    def download(self, url, name):
        try:
            result = requests.get(url)
            with open(name, "wb") as f:
                f.write(result.content)
        except Exception as e:
            QMessageBox.critical(self, "Download Error", f"Failed to download {url}: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
