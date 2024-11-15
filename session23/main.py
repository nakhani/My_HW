import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPalette, QColor, QBrush, QLinearGradient, QGradient
from ui_mainwindow import Ui_MainWindow
from sudoku import Sudoku

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.new_game.triggered.connect(self.new_game)
        self.ui.open_file.triggered.connect(self.open_file)
        self.ui.about_2.triggered.connect(self.show_about)
        self.ui.help.triggered.connect(self.show_help)
        self.ui.exit.triggered.connect(self.close)
        self.ui.solve_puzzle.triggered.connect(self.solve_puzzle)
        self.ui.actionDark.triggered.connect(self.toggle_dark_mode)

        self.dark_mode_enabled = False
        self.line_edits = [[QLineEdit() for j in range(9)] for i in range(9)]
        self.new_game()

    def toggle_dark_mode(self):
        self.dark_mode_enabled =  not self.dark_mode_enabled
        self.apply_styles()

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open File")[0]
            with open(file_path, "r") as f:
                big_text = f.read()
            
            rows = big_text.split("\n")
            puzzle_board = [[None for _ in range(9)] for _ in range(9)]
            
            for i in range(len(rows)):
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])

            for i in range(9):
                for j in range(9):
                    new_cell = QLineEdit()
                    new_cell.setAlignment(Qt.AlignCenter)  
                    if puzzle_board[i][j] != 0:
                        new_cell.setText(str(puzzle_board[i][j]))
                        new_cell.setReadOnly(True)
                    self.ui.gl_game.addWidget(new_cell, i, j)
                    new_cell.textChanged.connect(partial(self.validation, i, j))
                    self.line_edits[i][j] = new_cell
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load the file: {e}")

    def new_game(self):
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(Qt.AlignCenter)  
                if puzzle.board[i][j] is not None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.gl_game.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
        
        self.apply_styles()

    def apply_styles(self):
        palette = QPalette()
        if self.dark_mode_enabled:
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
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #121212;
                }
                QLineEdit {
                    background-color: #333333;
                    color: #FFFFFF;
                    border: 1px solid #555555;
                    padding: 5px;
                    border-radius: 3px;
                    text-align: center;
                }
            """)
        else:
            gradient = QLinearGradient(0, 0, 1, 1)
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(0, QColor("#ff9a9e"))
            gradient.setColorAt(1, QColor("#fad0c4"))
            palette.setBrush(QPalette.Window, QBrush(gradient))
            self.setStyleSheet("""
                QMainWindow {
                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                                stop:0 #ff9a9e, stop:1 #fad0c4);
                }
                QLineEdit {
                    background-color: #fff0f5;
                    color: #000000;
                    border: 1px solid #ff69b4;
                    padding: 5px;
                    border-radius: 3px;
                    text-align: center;
                }
            """)

        self.setPalette(palette)


    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")
        self.check()

    def check(self):
        def highlight_duplicates(numbers, elements):
            seen = {}
            for index, number in enumerate(numbers):
                if number in seen:
                    elements[index].setStyleSheet("background-color: pink;")
                    elements[seen[number]].setStyleSheet("background-color: pink;")
                else:
                    seen[number] = index

        for i in range(9):
            row_numbers = []
            row_elements = []
            col_numbers = []
            col_elements = []
            for j in range(9):
                row_text = self.line_edits[i][j].text()
                col_text = self.line_edits[j][i].text()
                if row_text:
                    row_numbers.append(row_text)
                    row_elements.append(self.line_edits[i][j])
                if col_text:
                    col_numbers.append(col_text)
                    col_elements.append(self.line_edits[j][i])
            highlight_duplicates(row_numbers, row_elements)
            highlight_duplicates(col_numbers, col_elements)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid_numbers = []
                grid_elements = []
                for k in range(3):
                    for l in range(3):
                        text = self.line_edits[i + k][j + l].text()
                        if text:
                            grid_numbers.append(text)
                            grid_elements.append(self.line_edits[i + k][j + l])
                highlight_duplicates(grid_numbers, grid_elements)

        if all(self.line_edits[i][j].text() == str(Sudoku(3).board[i][j]) for i in range(9) for j in range(9)):
            QMessageBox.information(self, "Congratulations!", "You have completed the Sudoku correctly! 🎉")

    def show_about(self):
        QMessageBox.information(self, "About", "This is a Sudoku game.")

    def show_help(self):
        QMessageBox.information(self, "Help", "Fill in the Sudoku grid following the rules: each number 1-9 must appear only once per row, column, and 3x3 grid.")

    def solve_puzzle(self):
        solved_puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5).board
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setText(str(solved_puzzle[i][j]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
