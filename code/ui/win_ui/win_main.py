# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 711)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 350, 261, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_jinhuo = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_jinhuo.setFont(font)
        self.btn_jinhuo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_jinhuo.setCheckable(False)
        self.btn_jinhuo.setObjectName("btn_jinhuo")
        self.verticalLayout.addWidget(self.btn_jinhuo)
        self.btn_tuihuo = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_tuihuo.setFont(font)
        self.btn_tuihuo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_tuihuo.setObjectName("btn_tuihuo")
        self.verticalLayout.addWidget(self.btn_tuihuo)
        self.btn_tongji = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_tongji.setFont(font)
        self.btn_tongji.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_tongji.setObjectName("btn_tongji")
        self.verticalLayout.addWidget(self.btn_tongji)
        self.btn_xiaoshou = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xiaoshou.setFont(font)
        self.btn_xiaoshou.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_xiaoshou.setObjectName("btn_xiaoshou")
        self.verticalLayout.addWidget(self.btn_xiaoshou)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书销售管理系统"))
        self.btn_jinhuo.setText(_translate("MainWindow", "进货"))
        self.btn_tuihuo.setText(_translate("MainWindow", "退货"))
        self.btn_tongji.setText(_translate("MainWindow", "统计"))
        self.btn_xiaoshou.setText(_translate("MainWindow", "销售"))
