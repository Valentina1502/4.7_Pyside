#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QLabel,\
    QWidget, QLineEdit, QPushButton
import sys
from PySide2.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.button1 = QPushButton('+', self)
        self.button2 = QPushButton('-', self)
        self.button3 = QPushButton('*', self)
        self.button4 = QPushButton('/', self)
        self.label = QLabel(self)
        self.initializeUI()


    def initializeUI(self):
        self.setGeometry(400, 200, 220, 250)
        self.setWindowTitle("Калькулятор")

        self.line_edit1.move(10, 10)
        self.line_edit1.resize(200, 20)
        self.line_edit2.move(10, 35)
        self.line_edit2.resize(200, 20)
        self.button1.move(10, 70)
        self.button1.resize(200, 30)
        self.button2.move(10, 100)
        self.button2.resize(200, 30)
        self.button3.move(10, 130)
        self.button3.resize(200, 30)
        self.button4.move(10, 160)
        self.button4.resize(200, 30)
        self.answer_label = QLabel(self)
        self.answer_label.move(10, 215)
        self.answer_label.resize(200, 30)
        self.answer_label.setFont(QFont('Comic Sans MS', 17))

        self.button1.clicked.connect(self.Calculator)
        self.button2.clicked.connect(self.Calculator)
        self.button3.clicked.connect(self.Calculator)
        self.button4.clicked.connect(self.Calculator)
        self.show()

    def Calculator(self):
        try:
            if float(self.line_edit1.text()) and float(self.line_edit2.text()):
                n1 = float(self.line_edit1.text())
                n2 = float(self.line_edit2.text())
        except ValueError:
            self.answer_label.setText("Введите числа")

        sender = self.sender()
        if sender.text() == "+":
            self.answer_label.setText(str(n1 + n2))
        elif sender.text() == "-":
            self.answer_label.setText(str(n1 - n2))
        elif sender.text() == "*":
            self.answer_label.setText(str(n1 * n2))
        elif sender.text() == "/":
            self.answer_label.setText(str(n1 / n2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) #зацикливание
