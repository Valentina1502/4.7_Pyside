#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QLabel,\
    QWidget, QLineEdit, QPushButton
import sys
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.label = QLabel(self)
        self.line_edit = QLineEdit(self)
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)

        self.initializeUI()


    def initializeUI(self):
        self.setGeometry(200, 200, 220, 290)
        self.setWindowTitle("Радуга")

        self.label = QLabel(self)
        self.label.move(10, 1)
        self.label.resize(200, 30)
        self.label.setFont(QFont('Comic Sans MS', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.line_edit.move(10, 40)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.resize(200, 20)
        self.button1.move(10, 70)
        self.button1.resize(200, 30)
        self.button1.setStyleSheet("background: #ff0000")
        self.button2.move(10, 100)
        self.button2.resize(200, 30)
        self.button2.setStyleSheet("background: #ff7d00")
        self.button3.move(10, 130)
        self.button3.resize(200, 30)
        self.button3.setStyleSheet("background: #ffff00")
        self.button4.move(10, 160)
        self.button4.resize(200, 30)
        self.button4.setStyleSheet("background: #00ff00")
        self.button5.move(10, 190)
        self.button5.resize(200, 30)
        self.button5.setStyleSheet("background: #007dff")
        self.button6.move(10, 220)
        self.button6.resize(200, 30)
        self.button6.setStyleSheet("background: #0000ff")
        self.button7.move(10, 250)
        self.button7.resize(200, 30)
        self.button7.setStyleSheet("background: #7d00ff")

        self.button1.clicked.connect(self.Red)
        self.button2.clicked.connect(self.Orange)
        self.button3.clicked.connect(self.Yellow)
        self.button4.clicked.connect(self.Green)
        self.button5.clicked.connect(self.LBlue)
        self.button6.clicked.connect(self.Blue)
        self.button7.clicked.connect(self.Purple)
        self.show()

    def Red(self):
        self.label.setText("Красный")
        self.line_edit.setText("#ff0000")


    def Orange(self):
        self.label.setText("Оранжевый")
        self.line_edit.setText("#ff7d00")


    def Yellow(self):
        self.label.setText("Желтый")
        self.line_edit.setText("#ffff00")


    def Green(self):
        self.label.setText("Зеленый")
        self.line_edit.setText("#00ff00")


    def LBlue(self):
        self.label.setText("Голубой")
        self.line_edit.setText("#007dff")


    def Blue(self):
        self.label.setText("Синий")
        self.line_edit.setText("#0000ff")


    def Purple(self):
        self.label.setText("Фиолетовый")
        self.line_edit.setText("#7d00ff")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
