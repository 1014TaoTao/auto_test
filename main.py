# coding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from tools.api_auto_test import UiApiAutoTool

if __name__ == '__main__':
    apps = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiApiAutoTool()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(apps.exec_())
