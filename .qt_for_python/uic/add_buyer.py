# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\ExcelVBA_BAYNA\source\dist\ui\add_buyer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 250)
        Form.setMinimumSize(QtCore.QSize(700, 250))
        Form.setMaximumSize(QtCore.QSize(700, 250))
        self.back_label = QtWidgets.QLabel(Form)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 700, 250))
        self.back_label.setText("")
        self.back_label.setPixmap(QtGui.QPixmap("e:\\ExcelVBA_BAYNA\\source\\dist\\ui\\../image/add_buyer_back.jpg"))
        self.back_label.setObjectName("back_label")
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(480, 190, 97, 41))
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setText("")
        self.add_button.setObjectName("add_button")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(593, 190, 97, 41))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.lineEdit_buyer_url = QtWidgets.QLineEdit(Form)
        self.lineEdit_buyer_url.setGeometry(QtCore.QRect(150, 118, 531, 31))
        font = QtGui.QFont()
        font.setFamily("源ノ角ゴシック JP Heavy")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_buyer_url.setFont(font)
        self.lineEdit_buyer_url.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(200, 200, 200);")
        self.lineEdit_buyer_url.setText("")
        self.lineEdit_buyer_url.setFrame(False)
        self.lineEdit_buyer_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_buyer_url.setObjectName("lineEdit_buyer_url")

        self.retranslateUi(Form)
        self.add_button.clicked.connect(Form.Add) # type: ignore
        self.exit_button.clicked.connect(Form.Exit) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Buyer"))
