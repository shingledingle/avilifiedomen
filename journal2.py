import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout,
                            QWidget, QTextEdit, QScrollArea)
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Journal App")
        self.setMinimumSize(QSize(800, 1000))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)

        self.label = QLabel("Input your miseries and consultations fine sir")
        self.label.setFont(QFont("Times New Roman", 24, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumHeight(800)
        layout.addWidget(self.text_edit)

        self.save_button = QPushButton("Save impetus writing")
        self.save_button.clicked.connect(self.clicked)
        layout.addWidget(self.save_button)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(self.returnbutton)
        layout.addWidget(self.return_button)

        scroll.setWidget(content)
        self.setCentralWidget(scroll)

    def clicked(self):
        self.label.setText("Catalogue of misfortunes and flowery thoughts")

    def returnbutton(self):
        self.label.setText("Input your miseries and consultations fine sir")


app = QApplication([])

window = MainWindow()
window.show()  

app.exec()

