# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fromTo(object):
    def __init__(self):
        self.label = None
        self.gainIP = None
        self.addGain = None

    def setupUi(self, fromTo):
        fromTo.setObjectName("fromTo")
        fromTo.resize(320, 280)
        fromTo.setStyleSheet("background-color:  rgb(204, 217, 221);")

        self.addGain = QtWidgets.QPushButton(fromTo)
        self.addGain.setGeometry(QtCore.QRect(70, 180, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        self.addGain.setFont(font)
        self.addGain.setStyleSheet("background-color: rgb(0, 100, 125);\n"
                                   "color: ghostWhite;")
        self.addGain.setObjectName("addGain")

        self.gainIP = QtWidgets.QLineEdit(fromTo)
        self.gainIP.setGeometry(QtCore.QRect(70, 100, 171, 51))
        self.gainIP.setStyleSheet("background-color: ghostWhite;")
        self.gainIP.setObjectName("gainIP")

        self.label = QtWidgets.QLabel(fromTo)
        self.label.setGeometry(QtCore.QRect(20, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(fromTo)
        QtCore.QMetaObject.connectSlotsByName(fromTo)

    def retranslateUi(self, fromTo):
        _translate = QtCore.QCoreApplication.translate
        fromTo.setWindowTitle(_translate("fromTo", "GainWindow"))
        self.addGain.setText(_translate("fromTo", "Add Gain"))
        self.label.setText(_translate("fromTo",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#2d2d2d; vertical-align:super;\">Gain From node 1 to node 2</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fromTo = QtWidgets.QDialog()
    ui = Ui_fromTo()
    ui.setupUi(fromTo)
    fromTo.show()
    sys.exit(app.exec_())
