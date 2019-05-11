# -*- coding: utf-8 -*-
import sys
from builtins import print

from PyQt5 import QtWidgets , QtCore ,QtGui , QtNetwork
import dising
import client

class test_app(QtWidgets.QMainWindow,dising.Ui_tes_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b1.clicked.connect(self.tes_B)
        self.pushButton.clicked.connect(self.tes_A)


    def tes_A(self):
        print("test b2 ")
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("test")
        t=self.lineEdit.text()
        print(t)
        return 1

    def tes_B(self):
        print("test b1")
        self.text.clear()
        for i in range(100):
            self.text.addItem("test")
        return 1
    def tes(self):
        QtNetwork.QUdpSocket(self)
def main():
    app=QtWidgets.QApplication(sys.argv)
    window=test_app()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()