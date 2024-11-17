import os
from threading import Thread
from time import time
from moviepy import editor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fast Downloader")
        self.setGeometry(200, 200, 400, 200)  

       
        self.setPalette(self.create_dark_palette())

        layout = QVBoxLayout()
        layout.setSpacing(5)  
        layout.setContentsMargins(10, 10, 10, 10)  

        self.label = QLabel("Selected video files:")
        layout.addWidget(self.label)

        self.select_files_button = QPushButton("Select Video Files")
        self.select_files_button.clicked.connect(self.select_video_files)
        layout.addWidget(self.select_files_button)

        self.label_output = QLabel("Select the folder to save outputs:")
        layout.addWidget(self.label_output)

        self.select_output_button = QPushButton("Select Output Directory")
        self.select_output_button.clicked.connect(self.select_output_directory)
        layout.addWidget(self.select_output_button)

        self.process_button = QPushButton("Start Conversion")
        self.process_button.clicked.connect(self.start_process)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.video_files = []
        self.output_directory = ""

       
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

    def select_video_files(self):
        self.video_files, _ = QFileDialog.getOpenFileNames(self, "Select Video Files", "", "Video Files (*.mp4 *.mov)")
        self.label.setText(f"Selected {len(self.video_files)} video files")

    def select_output_directory(self):
        self.output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        self.label_output.setText(f"Output directory: {self.output_directory}")

    def start_process(self):
        if not self.output_directory:
            QMessageBox.warning(self, "Selection Error", "Please select an output directory.")
            return

        if not self.video_files:
            QMessageBox.warning(self, "Input Error", "Please select at least one video file.")
            return

        start_time = time()

        threads = []
        for url in self.video_files:
            threads.append(Thread(target=self.convert, args=(url,)))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        end_time = time()
        QMessageBox.information(self, "Conversion Completed", f"Converted {len(self.video_files)} files in {end_time - start_time:.2f} seconds.")

    def convert(self, url):
        try:
            name = os.path.join(self.output_directory, os.path.basename(url).rsplit('.', 1)[0] + '.mp3')
            video = editor.VideoFileClip(url)
            video.audio.write_audiofile(name)
            print(f"Converted {url} to {name}")
        except Exception as e:
            QMessageBox.critical(self, "Conversion Error", f"Failed to convert {url}: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
