# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1620, 1010) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wg_video = QVideoWidget(self.centralwidget)
        self.wg_video.setGeometry(QtCore.QRect(10, 10, 1600, 900))
        self.wg_video.setObjectName("wg_video")

        self.label = QLabel(self.centralwidget) 
        self.label.move(10, 10)
        self.label.resize(1600, 900)

        self.bt_start = QtWidgets.QPushButton(self.centralwidget)
        self.bt_start.setGeometry(QtCore.QRect(730, 920, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.bt_start.setFont(font)
        self.bt_start.setObjectName("bt_start")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video detector"))
        self.bt_start.setText(_translate("MainWindow", "Start"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
