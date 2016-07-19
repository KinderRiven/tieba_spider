# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(742, 395)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(150, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.txt_log = QtGui.QTextEdit(self.centralwidget)
        self.txt_log.setGeometry(QtCore.QRect(20, 150, 711, 161))
        self.txt_log.setObjectName(_fromUtf8("txt_log"))
        self.lab_id = QtGui.QLabel(self.centralwidget)
        self.lab_id.setGeometry(QtCore.QRect(30, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lab_id.setFont(font)
        self.lab_id.setObjectName(_fromUtf8("lab_id"))
        self.btn_stop = QtGui.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(310, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.btn_exit = QtGui.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(470, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.txt_post_id = QtGui.QLineEdit(self.centralwidget)
        self.txt_post_id.setGeometry(QtCore.QRect(90, 30, 251, 31))
        self.txt_post_id.setObjectName(_fromUtf8("txt_post_id"))
        self.lab_start = QtGui.QLabel(self.centralwidget)
        self.lab_start.setGeometry(QtCore.QRect(380, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lab_start.setFont(font)
        self.lab_start.setObjectName(_fromUtf8("lab_start"))
        self.txt_post_start = QtGui.QLineEdit(self.centralwidget)
        self.txt_post_start.setGeometry(QtCore.QRect(470, 30, 81, 31))
        self.txt_post_start.setObjectName(_fromUtf8("txt_post_start"))
        self.lab_end = QtGui.QLabel(self.centralwidget)
        self.lab_end.setGeometry(QtCore.QRect(580, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lab_end.setFont(font)
        self.lab_end.setObjectName(_fromUtf8("lab_end"))
        self.txt_post_end = QtGui.QLineEdit(self.centralwidget)
        self.txt_post_end.setGeometry(QtCore.QRect(640, 30, 81, 31))
        self.txt_post_end.setObjectName(_fromUtf8("txt_post_end"))
        self.txt_save_path = QtGui.QLineEdit(self.centralwidget)
        self.txt_save_path.setGeometry(QtCore.QRect(190, 90, 441, 31))
        self.txt_save_path.setObjectName(_fromUtf8("txt_save_path"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_path = QtGui.QPushButton(self.centralwidget)
        self.btn_path.setGeometry(QtCore.QRect(640, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_path.setFont(font)
        self.btn_path.setText(_fromUtf8(""))
        self.btn_path.setObjectName(_fromUtf8("btn_path"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_start, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.start)
        QtCore.QObject.connect(self.btn_path, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update_save_path)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_start.setText(_translate("MainWindow", "START", None))
        self.lab_id.setText(_translate("MainWindow", "ID", None))
        self.btn_stop.setText(_translate("MainWindow", "STOP", None))
        self.btn_exit.setText(_translate("MainWindow", "EXIT", None))
        self.lab_start.setText(_translate("MainWindow", "from", None))
        self.lab_end.setText(_translate("MainWindow", "To", None))
        self.label_4.setText(_translate("MainWindow", "Save Path", None))

