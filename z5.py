#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, \
    QPushButton, QButtonGroup, QLabel, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PadioButtons")
        self.setGeometry(100, 100, 280, 100)

        self.label = QLabel(self)
        self.label.move(50, 50)
        self.label.resize(100, 20)
        self.RadioButton1 = QPushButton('ФИО', self)
        self.RadioButton1.setCheckable(True)
        self.RadioButton1.move(10, 10)
        self.RadioButton1.resize(80, 20)
        self.RadioButton2 = QPushButton('Группа', self)
        self.RadioButton2.setCheckable(True)
        self.RadioButton2.move(100, 10)
        self.RadioButton2.resize(80, 20)
        self.RadioButton3 = QPushButton('Телефон', self)
        self.RadioButton3.setCheckable(True)
        self.RadioButton3.move(190, 10)
        self.RadioButton3.resize(80, 20)
        self.buttonGr = QButtonGroup()
        self.buttonGr.addButton(self.RadioButton1)
        self.buttonGr.addButton(self.RadioButton2)
        self.buttonGr.addButton(self.RadioButton3)
        self.buttonGr.buttonClicked.connect(self.RadioButtonClicked)
        Layout = QVBoxLayout(self)
        Layout.addWidget(self.RadioButton1)
        Layout.addWidget(self.RadioButton2)
        Layout.addWidget(self.RadioButton3)
        Layout.addWidget(self.label)
        self.show()


    def RadioButtonClicked(self, Rb):
        self.label.setText(info[Rb.text()])


if __name__ == "__main__":
    info = {
            'ФИО': 'Новикова Валенина Сергеевна',
            'Группа': 'ИВТ-б-о-20-1',
            'Телефон': '8-(988)-755-11-15'
        }
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
