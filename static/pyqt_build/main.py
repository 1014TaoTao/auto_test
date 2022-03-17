#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 9:07
@Author  : ZhangTAO
@File    : main.py
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_py.apitest import Ui_ApiTool

if __name__ == '__main__':
    apps = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_ApiTool()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(apps.exec_())
