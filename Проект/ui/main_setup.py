# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1123, 845)
        self.main_table = QtWidgets.QTableWidget(Form)
        self.main_table.setGeometry(QtCore.QRect(10, 40, 761, 791))
        self.main_table.setObjectName("main_table")
        self.main_table.setColumnCount(6)
        self.main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(5, item)
        self.new_elem = QtWidgets.QPushButton(Form)
        self.new_elem.setGeometry(QtCore.QRect(10, 10, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_elem.setFont(font)
        self.new_elem.setObjectName("new_elem")
        self.showforkrit = QtWidgets.QPushButton(Form)
        self.showforkrit.setGeometry(QtCore.QRect(790, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showforkrit.setFont(font)
        self.showforkrit.setObjectName("showforkrit")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(800, 30, 301, 271))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.error.setFont(font)
        self.error.setObjectName("error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.main_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.main_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Наименование"))
        item = self.main_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Цена за штуку"))
        item = self.main_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Количество"))
        item = self.main_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Номер партии"))
        item = self.main_table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Состояние"))
        self.new_elem.setText(_translate("Form", "Добавить"))
        self.showforkrit.setText(_translate("Form", "Показать по критерию"))
        self.error.setText(_translate("Form", "Ошибка!"))