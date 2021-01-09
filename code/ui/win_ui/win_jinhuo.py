# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_jinhuo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_jinhuo(object):
    def setupUi(self, win_jinhuo):
        win_jinhuo.setObjectName("win_jinhuo")
        win_jinhuo.resize(1046, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_jinhuo.sizePolicy().hasHeightForWidth())
        win_jinhuo.setSizePolicy(sizePolicy)
        self.input_win_name = QtWidgets.QTextEdit(win_jinhuo)
        self.input_win_name.setGeometry(QtCore.QRect(350, 60, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.input_win_name.setFont(font)
        self.input_win_name.setDocumentTitle("")
        self.input_win_name.setObjectName("input_win_name")
        self.hint_input_book_name = QtWidgets.QLabel(win_jinhuo)
        self.hint_input_book_name.setGeometry(QtCore.QRect(350, 0, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_input_book_name.setFont(font)
        self.hint_input_book_name.setObjectName("hint_input_book_name")
        self.hint_book_table = QtWidgets.QLabel(win_jinhuo)
        self.hint_book_table.setGeometry(QtCore.QRect(130, 0, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_book_table.setFont(font)
        self.hint_book_table.setObjectName("hint_book_table")
        self.book_table = QtWidgets.QTableWidget(win_jinhuo)
        self.book_table.setGeometry(QtCore.QRect(30, 60, 301, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_table.sizePolicy().hasHeightForWidth())
        self.book_table.setSizePolicy(sizePolicy)
        self.book_table.setAutoScrollMargin(16)
        self.book_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.book_table.setObjectName("book_table")
        self.book_table.setColumnCount(3)
        self.book_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(2, item)
        self.book_table.horizontalHeader().setCascadingSectionResizes(False)
        self.book_table.horizontalHeader().setDefaultSectionSize(80)
        self.book_table.horizontalHeader().setMinimumSectionSize(25)
        self.book_table.horizontalHeader().setSortIndicatorShown(False)
        self.book_table.horizontalHeader().setStretchLastSection(True)
        self.book_table.verticalHeader().setHighlightSections(True)
        self.book_table.verticalHeader().setStretchLastSection(False)
        self.book_name_btn = QtWidgets.QPushButton(win_jinhuo)
        self.book_name_btn.setGeometry(QtCore.QRect(350, 100, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.book_name_btn.setFont(font)
        self.book_name_btn.setAutoDefault(False)
        self.book_name_btn.setObjectName("book_name_btn")
        self.hint_jin_huo_table = QtWidgets.QLabel(win_jinhuo)
        self.hint_jin_huo_table.setGeometry(QtCore.QRect(460, 130, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_jin_huo_table.setFont(font)
        self.hint_jin_huo_table.setObjectName("hint_jin_huo_table")
        self.jin_huo_btn = QtWidgets.QPushButton(win_jinhuo)
        self.jin_huo_btn.setGeometry(QtCore.QRect(350, 460, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.jin_huo_btn.setFont(font)
        self.jin_huo_btn.setAutoDefault(False)
        self.jin_huo_btn.setObjectName("jin_huo_btn")
        self.jin_huo_table = QtWidgets.QTableWidget(win_jinhuo)
        self.jin_huo_table.setGeometry(QtCore.QRect(350, 190, 331, 261))
        self.jin_huo_table.setRowCount(0)
        self.jin_huo_table.setColumnCount(4)
        self.jin_huo_table.setObjectName("jin_huo_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table.setHorizontalHeaderItem(3, item)
        self.jin_huo_table.horizontalHeader().setDefaultSectionSize(75)
        self.jin_huo_table.horizontalHeader().setSortIndicatorShown(False)
        self.jin_huo_table.horizontalHeader().setStretchLastSection(True)
        self.jin_huo_table_2 = QtWidgets.QTableWidget(win_jinhuo)
        self.jin_huo_table_2.setGeometry(QtCore.QRect(700, 60, 311, 431))
        self.jin_huo_table_2.setRowCount(0)
        self.jin_huo_table_2.setColumnCount(4)
        self.jin_huo_table_2.setObjectName("jin_huo_table_2")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.jin_huo_table_2.setHorizontalHeaderItem(3, item)
        self.jin_huo_table_2.horizontalHeader().setDefaultSectionSize(75)
        self.jin_huo_table_2.horizontalHeader().setSortIndicatorShown(False)
        self.jin_huo_table_2.horizontalHeader().setStretchLastSection(True)
        self.hint_jin_huo_table_2 = QtWidgets.QLabel(win_jinhuo)
        self.hint_jin_huo_table_2.setGeometry(QtCore.QRect(820, 0, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_jin_huo_table_2.setFont(font)
        self.hint_jin_huo_table_2.setObjectName("hint_jin_huo_table_2")

        self.retranslateUi(win_jinhuo)
        QtCore.QMetaObject.connectSlotsByName(win_jinhuo)

    def retranslateUi(self, win_jinhuo):
        _translate = QtCore.QCoreApplication.translate
        win_jinhuo.setWindowTitle(_translate("win_jinhuo", "进货"))
        self.hint_input_book_name.setText(_translate("win_jinhuo", "输入欲进货书名"))
        self.hint_book_table.setText(_translate("win_jinhuo", "藏书列表"))
        item = self.book_table.horizontalHeaderItem(0)
        item.setText(_translate("win_jinhuo", "ID"))
        item = self.book_table.horizontalHeaderItem(1)
        item.setText(_translate("win_jinhuo", "书名"))
        item = self.book_table.horizontalHeaderItem(2)
        item.setText(_translate("win_jinhuo", "库存"))
        self.book_name_btn.setText(_translate("win_jinhuo", "确认"))
        self.hint_jin_huo_table.setText(_translate("win_jinhuo", "备选书单"))
        self.jin_huo_btn.setText(_translate("win_jinhuo", "确认进货"))
        item = self.jin_huo_table.horizontalHeaderItem(0)
        item.setText(_translate("win_jinhuo", "书目ID"))
        item = self.jin_huo_table.horizontalHeaderItem(1)
        item.setText(_translate("win_jinhuo", "供应商ID"))
        item = self.jin_huo_table.horizontalHeaderItem(2)
        item.setText(_translate("win_jinhuo", "进货价"))
        item = self.jin_huo_table.horizontalHeaderItem(3)
        item.setText(_translate("win_jinhuo", "进货数量"))
        item = self.jin_huo_table_2.horizontalHeaderItem(0)
        item.setText(_translate("win_jinhuo", "书目ID"))
        item = self.jin_huo_table_2.horizontalHeaderItem(1)
        item.setText(_translate("win_jinhuo", "供应商ID"))
        item = self.jin_huo_table_2.horizontalHeaderItem(2)
        item.setText(_translate("win_jinhuo", "进货价"))
        item = self.jin_huo_table_2.horizontalHeaderItem(3)
        item.setText(_translate("win_jinhuo", "进货数量"))
        self.hint_jin_huo_table_2.setText(_translate("win_jinhuo", "进货单"))
