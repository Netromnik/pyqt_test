# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.xy = QtWidgets.QGraphicsView(self.groupBox_2)
        self.xy.setObjectName("xy")
        self.gridLayout.addWidget(self.xy, 4, 0, 1, 1)
        self.yz = QtWidgets.QGraphicsView(self.groupBox_2)
        self.yz.setObjectName("yz")
        self.gridLayout.addWidget(self.yz, 4, 2, 1, 1)
        self.xz = QtWidgets.QGraphicsView(self.groupBox_2)
        self.xz.setAcceptDrops(False)
        self.xz.setToolTip("")
        self.xz.setObjectName("xz")
        self.gridLayout.addWidget(self.xz, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok = QtWidgets.QPushButton(self.groupBox)
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.end = QtWidgets.QPushButton(self.groupBox)
        self.end.setObjectName("end")
        self.horizontalLayout_2.addWidget(self.end)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "область графиков"))
        self.label_3.setText(_translate("MainWindow", "yaw"))
        self.label_2.setText(_translate("MainWindow", "pitch"))
        self.label.setText(_translate("MainWindow", "roll"))
        self.ok.setText(_translate("MainWindow", "start"))
        self.end.setText(_translate("MainWindow", "end"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

