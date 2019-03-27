# -*- coding:utf-8 -*-

"""
    2019/4/8 11:41 by young
"""

import sys
from lib_ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
