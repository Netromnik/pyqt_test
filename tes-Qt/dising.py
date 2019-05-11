# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tes_main(object):
    def setupUi(self, tes_main):
        tes_main.setObjectName("tes_main")
        tes_main.resize(730, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tes_main.sizePolicy().hasHeightForWidth())
        tes_main.setSizePolicy(sizePolicy)
        tes_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(tes_main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setInputMask("000.000.0.000")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.b1 = QtWidgets.QPushButton(self.groupBox)
        self.b1.setObjectName("b1")
        self.verticalLayout_2.addWidget(self.b1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.text = QtWidgets.QListWidget(self.centralwidget)
        self.text.setObjectName("text")
        self.horizontalLayout_2.addWidget(self.text)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        tes_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tes_main)
        self.statusbar.setObjectName("statusbar")
        tes_main.setStatusBar(self.statusbar)

        self.retranslateUi(tes_main)
        QtCore.QMetaObject.connectSlotsByName(tes_main)

    def retranslateUi(self, tes_main):
        _translate = QtCore.QCoreApplication.translate
        tes_main.setWindowTitle(_translate("tes_main", "MainWindow"))
        self.groupBox_2.setTitle(_translate("tes_main", "GroupBox"))
        self.groupBox.setTitle(_translate("tes_main", "GroupBox"))
        self.pushButton.setText(_translate("tes_main", "PushButton"))
        self.b1.setText(_translate("tes_main", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tes_main = QtWidgets.QMainWindow()
    ui = Ui_tes_main()
    ui.setupUi(tes_main)
    tes_main.show()
    sys.exit(app.exec_())

