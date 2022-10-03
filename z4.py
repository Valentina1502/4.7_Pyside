#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QLabel,\
    QWidget, QLineEdit, QPushButton, QFileDialog, QTextEdit
from PySide2.QtCore import QByteArray
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.line_edit = QLineEdit(self)
        self.button1 = QPushButton("Открыть", self)
        self.button2 = QPushButton("Сохранить", self)
        self.label = QLabel(self)
        self.text = QTextEdit(self)
        self.initializeUI()


    def initializeUI(self):
        self.setGeometry(50, 100, 600, 550)
        self.setWindowTitle("Работа с файлами")

        self.line_edit.move(200, 10)
        self.line_edit.resize(200, 20)
        self.button1.move(200, 35)
        self.button1.resize(95, 25)
        self.button1.setStyleSheet("background: #AFEEEE")
        self.button2.move(305, 35)
        self.button2.resize(95, 25)
        self.button2.setStyleSheet("background: #F0E68C")
        self.label.move(200, 65)
        self.label.resize(200, 10)
        self.text.move(20, 85)
        self.text.resize(560, 450)

        self.button1.clicked.connect(self.OpenF)
        self.button2.clicked.connect(self.SaveF)
        self.show()

    def OpenF(self):
        if self.line_edit.text() != '':
            try:
                file_name = self.line_edit.text()
                with open(file_name, 'r', encoding="utf-8") as f:
                    file = f.read()
                self.text.setText(file)
            except Exception as excep:
                self.label.setText(f"Ошибка. {excep}")
        else:
            self.label.setText(f"Введите имя файла")


    def SaveF(self):
        if self.line_edit.text() != '':
            file = self.text.toPlainText()
            file = bytes(file, encoding='utf-8')
            file = QByteArray(file)
            file_name = self.line_edit.text()
            QFileDialog.saveFileContent(file, file_name)
        else:
            self.label.setText("Введите имя файла")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
