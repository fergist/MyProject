# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Проект\ui\crit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1073, 851)
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(10, 10, 611, 821))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.criteti = QtWidgets.QComboBox(Form)
        self.criteti.setGeometry(QtCore.QRect(640, 30, 131, 31))
        self.criteti.setObjectName("criteti")
        self.text_crit = QtWidgets.QLineEdit(Form)
        self.text_crit.setGeometry(QtCore.QRect(820, 30, 241, 31))
        self.text_crit.setObjectName("text_crit")
        self.show_it = QtWidgets.QPushButton(Form)
        self.show_it.setGeometry(QtCore.QRect(900, 80, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_it.setFont(font)
        self.show_it.setObjectName("show_it")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.show_it.setText(_translate("Form", "Показать"))
