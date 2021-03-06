# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\ExcelVBA_BAYNA\source\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWidget(object):
    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(1402, 757)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QWidget.sizePolicy().hasHeightForWidth())
        QWidget.setSizePolicy(sizePolicy)
        QWidget.setMinimumSize(QtCore.QSize(1402, 757))
        QWidget.setMaximumSize(QtCore.QSize(1402, 757))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(16)
        QWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/cyi/.designer/backup/mainIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QWidget.setWindowIcon(icon)
        QWidget.setAutoFillBackground(False)
        QWidget.setStyleSheet("background-color: rgb(42, 53, 127);\n"
"color: rgb(255, 255, 255);")
        self.back_label = QtWidgets.QLabel(QWidget)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 1190, 768))
        self.back_label.setStyleSheet("border-image: url(:/image/main_back.jpg);")
        self.back_label.setText("")
        self.back_label.setPixmap(QtGui.QPixmap("C:/Users/cyi/.designer/image/main_back.jpg"))
        self.back_label.setObjectName("back_label")
        self.except_button = QtWidgets.QPushButton(QWidget)
        self.except_button.setGeometry(QtCore.QRect(913, 45, 90, 90))
        self.except_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.except_button.setText("")
        self.except_button.setObjectName("except_button")
        self.condition_table = QtWidgets.QTableWidget(QWidget)
        self.condition_table.setGeometry(QtCore.QRect(0, 190, 1186, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.condition_table.setFont(font)
        self.condition_table.setStyleSheet("")
        self.condition_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.condition_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.condition_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.condition_table.setAlternatingRowColors(True)
        self.condition_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.condition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.condition_table.setShowGrid(True)
        self.condition_table.setWordWrap(False)
        self.condition_table.setRowCount(0)
        self.condition_table.setObjectName("condition_table")
        self.condition_table.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.condition_table.setHorizontalHeaderItem(8, item)
        self.condition_table.horizontalHeader().setVisible(True)
        self.condition_table.verticalHeader().setVisible(True)
        self.result_button = QtWidgets.QPushButton(QWidget)
        self.result_button.setGeometry(QtCore.QRect(565, 45, 90, 90))
        self.result_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result_button.setText("")
        self.result_button.setObjectName("result_button")
        self.check_button = QtWidgets.QPushButton(QWidget)
        self.check_button.setGeometry(QtCore.QRect(745, 45, 90, 90))
        self.check_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_button.setText("")
        self.check_button.setObjectName("check_button")
        self.buyer_button = QtWidgets.QPushButton(QWidget)
        self.buyer_button.setGeometry(QtCore.QRect(655, 45, 90, 90))
        self.buyer_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buyer_button.setText("")
        self.buyer_button.setObjectName("buyer_button")
        self.add_button = QtWidgets.QPushButton(QWidget)
        self.add_button.setGeometry(QtCore.QRect(475, 45, 90, 90))
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setStyleSheet("")
        self.add_button.setText("")
        self.add_button.setObjectName("add_button")
        self.except_view_button = QtWidgets.QPushButton(QWidget)
        self.except_view_button.setGeometry(QtCore.QRect(998, 45, 90, 90))
        self.except_view_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.except_view_button.setText("")
        self.except_view_button.setObjectName("except_view_button")
        self.result_table = QtWidgets.QTableWidget(QWidget)
        self.result_table.setGeometry(QtCore.QRect(0, 360, 1186, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_table.setFont(font)
        self.result_table.setStyleSheet("")
        self.result_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.result_table.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.result_table.setAlternatingRowColors(True)
        self.result_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.result_table.setShowGrid(True)
        self.result_table.setWordWrap(False)
        self.result_table.setRowCount(0)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(10, item)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setSortIndicatorShown(False)
        self.result_table.verticalHeader().setVisible(True)
        self.label = QtWidgets.QLabel(QWidget)
        self.label.setGeometry(QtCore.QRect(3, 732, 1184, 33))
        self.label.setStyleSheet("background-color: rgb(42, 53, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.csv_button = QtWidgets.QPushButton(QWidget)
        self.csv_button.setGeometry(QtCore.QRect(1087, 45, 90, 90))
        self.csv_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csv_button.setText("")
        self.csv_button.setObjectName("csv_button")
        self.product_table = QtWidgets.QTableWidget(QWidget)
        self.product_table.setGeometry(QtCore.QRect(10, 510, 1186, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.product_table.setFont(font)
        self.product_table.setStyleSheet("")
        self.product_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.product_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.product_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.product_table.setAlternatingRowColors(True)
        self.product_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.product_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.product_table.setShowGrid(True)
        self.product_table.setWordWrap(False)
        self.product_table.setRowCount(0)
        self.product_table.setObjectName("product_table")
        self.product_table.setColumnCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(12, item)
        self.product_table.horizontalHeader().setVisible(True)
        self.product_table.horizontalHeader().setSortIndicatorShown(True)
        self.product_table.verticalHeader().setVisible(True)
        self.frame = QtWidgets.QFrame(QWidget)
        self.frame.setGeometry(QtCore.QRect(2, 733, 1186, 21))
        self.frame.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progress_bar_product_all = QtWidgets.QLabel(self.frame)
        self.progress_bar_product_all.setGeometry(QtCore.QRect(67, 0, 50, 20))
        self.progress_bar_product_all.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.489, stop:0.00564972 rgba(0, 0, 200, 255), stop:1 rgba(94, 156, 255, 255));\n"
"\n"
"")
        self.progress_bar_product_all.setText("")
        self.progress_bar_product_all.setObjectName("progress_bar_product_all")
        self.progress_bar_all = QtWidgets.QLabel(self.frame)
        self.progress_bar_all.setGeometry(QtCore.QRect(10, 0, 50, 20))
        self.progress_bar_all.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.489, stop:0.00564972 rgba(0, 0, 200, 255), stop:1 rgba(94, 156, 255, 255));\n"
"\n"
"\n"
"")
        self.progress_bar_all.setText("")
        self.progress_bar_all.setObjectName("progress_bar_all")
        self.cur_pos_product = QtWidgets.QLabel(self.frame)
        self.cur_pos_product.setGeometry(QtCore.QRect(70, 0, 1190, 20))
        self.cur_pos_product.setMinimumSize(QtCore.QSize(50, 0))
        self.cur_pos_product.setMaximumSize(QtCore.QSize(1190, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_pos_product.setFont(font)
        self.cur_pos_product.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cur_pos_product.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_pos_product.setObjectName("cur_pos_product")
        self.cur_pos = QtWidgets.QLabel(self.frame)
        self.cur_pos.setGeometry(QtCore.QRect(330, 0, 1189, 20))
        self.cur_pos.setMinimumSize(QtCore.QSize(50, 0))
        self.cur_pos.setMaximumSize(QtCore.QSize(1189, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_pos.setFont(font)
        self.cur_pos.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cur_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_pos.setObjectName("cur_pos")
        self.cur_state = QtWidgets.QLabel(self.frame)
        self.cur_state.setGeometry(QtCore.QRect(140, 0, 191, 20))
        self.cur_state.setMinimumSize(QtCore.QSize(50, 0))
        self.cur_state.setMaximumSize(QtCore.QSize(1189, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_state.setFont(font)
        self.cur_state.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cur_state.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cur_state.setObjectName("cur_state")
        self.cur_product_state = QtWidgets.QLabel(self.frame)
        self.cur_product_state.setGeometry(QtCore.QRect(990, 0, 191, 20))
        self.cur_product_state.setMinimumSize(QtCore.QSize(50, 0))
        self.cur_product_state.setMaximumSize(QtCore.QSize(1189, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_product_state.setFont(font)
        self.cur_product_state.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cur_product_state.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cur_product_state.setObjectName("cur_product_state")
        self.label_title_back = QtWidgets.QLabel(QWidget)
        self.label_title_back.setGeometry(QtCore.QRect(4, 137, 161, 51))
        self.label_title_back.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_title_back.setText("")
        self.label_title_back.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_back.setObjectName("label_title_back")
        self.second_button = QtWidgets.QPushButton(QWidget)
        self.second_button.setGeometry(QtCore.QRect(831, 45, 90, 90))
        self.second_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_button.setText("")
        self.second_button.setObjectName("second_button")
        self.list_title = QtWidgets.QLabel(QWidget)
        self.list_title.setGeometry(QtCore.QRect(0, 152, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.list_title.setFont(font)
        self.list_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.list_title.setAlignment(QtCore.Qt.AlignCenter)
        self.list_title.setObjectName("list_title")
        self.label_control_pannel = QtWidgets.QLabel(QWidget)
        self.label_control_pannel.setGeometry(QtCore.QRect(1027, 141, 161, 51))
        self.label_control_pannel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_control_pannel.setText("")
        self.label_control_pannel.setPixmap(QtGui.QPixmap("e:\\ExcelVBA_BAYNA\\source\\ui\\../image/control_panel.png"))
        self.label_control_pannel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control_pannel.setObjectName("label_control_pannel")
        self.except_table = QtWidgets.QTableWidget(QWidget)
        self.except_table.setGeometry(QtCore.QRect(10, 600, 1186, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.except_table.setFont(font)
        self.except_table.setStyleSheet("")
        self.except_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.except_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.except_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.except_table.setAlternatingRowColors(True)
        self.except_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.except_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.except_table.setShowGrid(True)
        self.except_table.setWordWrap(False)
        self.except_table.setRowCount(0)
        self.except_table.setObjectName("except_table")
        self.except_table.setColumnCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.except_table.setHorizontalHeaderItem(9, item)
        self.except_table.horizontalHeader().setVisible(True)
        self.except_table.verticalHeader().setVisible(True)
        self.widget_pannel = QtWidgets.QWidget(QWidget)
        self.widget_pannel.setGeometry(QtCore.QRect(1058, 147, 117, 41))
        self.widget_pannel.setStyleSheet("#widget_pannel{background-color: rgba(255, 255, 255, 0);}")
        self.widget_pannel.setObjectName("widget_pannel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_pannel)
        self.horizontalLayout.setContentsMargins(1, 0, 1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stopButton = QtWidgets.QToolButton(self.widget_pannel)
        self.stopButton.setMinimumSize(QtCore.QSize(28, 28))
        self.stopButton.setMaximumSize(QtCore.QSize(28, 28))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.playButton = QtWidgets.QToolButton(self.widget_pannel)
        self.playButton.setMinimumSize(QtCore.QSize(28, 28))
        self.playButton.setMaximumSize(QtCore.QSize(28, 28))
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QToolButton(self.widget_pannel)
        self.pauseButton.setMinimumSize(QtCore.QSize(28, 28))
        self.pauseButton.setMaximumSize(QtCore.QSize(28, 28))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setText("")
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.settingButton = QtWidgets.QToolButton(self.widget_pannel)
        self.settingButton.setMinimumSize(QtCore.QSize(28, 28))
        self.settingButton.setMaximumSize(QtCore.QSize(28, 28))
        self.settingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.horizontalLayout.addWidget(self.settingButton)
        self.label_table_corner = QtWidgets.QLabel(QWidget)
        self.label_table_corner.setGeometry(QtCore.QRect(1200, 240, 52, 71))
        self.label_table_corner.setStyleSheet("background-color: rgb(45, 45, 61);")
        self.label_table_corner.setText("")
        self.label_table_corner.setObjectName("label_table_corner")
        self.back_label.raise_()
        self.label.raise_()
        self.except_button.raise_()
        self.condition_table.raise_()
        self.result_button.raise_()
        self.check_button.raise_()
        self.buyer_button.raise_()
        self.add_button.raise_()
        self.except_view_button.raise_()
        self.result_table.raise_()
        self.csv_button.raise_()
        self.product_table.raise_()
        self.frame.raise_()
        self.label_title_back.raise_()
        self.second_button.raise_()
        self.list_title.raise_()
        self.label_control_pannel.raise_()
        self.except_table.raise_()
        self.widget_pannel.raise_()
        self.label_table_corner.raise_()

        self.retranslateUi(QWidget)
        self.add_button.clicked.connect(QWidget.Add_URL) # type: ignore
        self.result_button.clicked.connect(QWidget.Result) # type: ignore
        self.condition_table.itemDoubleClicked['QTableWidgetItem*'].connect(QWidget.Condition_table_click) # type: ignore
        self.check_button.clicked.connect(QWidget.Check) # type: ignore
        self.buyer_button.clicked.connect(QWidget.BuyerAdd) # type: ignore
        self.except_button.clicked.connect(QWidget.Except) # type: ignore
        self.csv_button.clicked.connect(QWidget.CSV_write) # type: ignore
        QWidget.destroyed.connect(QWidget.deleteLater) # type: ignore
        self.second_button.clicked.connect(QWidget.second_find) # type: ignore
        self.result_table.itemDoubleClicked['QTableWidgetItem*'].connect(QWidget.Result_table_click) # type: ignore
        self.product_table.itemDoubleClicked['QTableWidgetItem*'].connect(QWidget.product_table_click) # type: ignore
        self.except_view_button.clicked.connect(QWidget.Except_view) # type: ignore
        self.except_table.itemDoubleClicked['QTableWidgetItem*'].connect(QWidget.except_table_click) # type: ignore
        self.playButton.clicked.connect(QWidget.Play) # type: ignore
        self.pauseButton.clicked.connect(QWidget.Pause) # type: ignore
        self.stopButton.clicked.connect(QWidget.Stop) # type: ignore
        self.settingButton.clicked.connect(QWidget.Setting) # type: ignore
        self.result_table.itemChanged['QTableWidgetItem*'].connect(QWidget.result_item_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "BUYMA MODELING Pro"))
        self.condition_table.setSortingEnabled(False)
        item = self.condition_table.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "?????? URL"))
        item = self.condition_table.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "?????????"))
        item = self.condition_table.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "?????????"))
        item = self.condition_table.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "?????????"))
        item = self.condition_table.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "30????????????"))
        item = self.condition_table.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "??????????????????"))
        item = self.condition_table.horizontalHeaderItem(6)
        item.setText(_translate("QWidget", "?????????????????????"))
        item = self.condition_table.horizontalHeaderItem(7)
        item.setText(_translate("QWidget", "?????????????????????"))
        item = self.condition_table.horizontalHeaderItem(8)
        item.setText(_translate("QWidget", "????????????"))
        self.result_table.setSortingEnabled(True)
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "?????????????????????"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "???????????????"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "????????????URL"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "?????????"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "?????????"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("QWidget", "??????"))
        item = self.result_table.horizontalHeaderItem(7)
        item.setText(_translate("QWidget", "30????????????"))
        item = self.result_table.horizontalHeaderItem(8)
        item.setText(_translate("QWidget", "5???????????????"))
        item = self.result_table.horizontalHeaderItem(9)
        item.setText(_translate("QWidget", "????????????"))
        item = self.result_table.horizontalHeaderItem(10)
        item.setText(_translate("QWidget", "??????"))
        self.product_table.setSortingEnabled(True)
        item = self.product_table.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "???????????????"))
        item = self.product_table.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "??????"))
        item = self.product_table.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "?????????"))
        item = self.product_table.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "????????????"))
        item = self.product_table.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "???????????????URL"))
        item = self.product_table.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "???????????????"))
        item = self.product_table.horizontalHeaderItem(6)
        item.setText(_translate("QWidget", "????????????????????????"))
        item = self.product_table.horizontalHeaderItem(7)
        item.setText(_translate("QWidget", "???????????????"))
        item = self.product_table.horizontalHeaderItem(8)
        item.setText(_translate("QWidget", "??????30????????????"))
        item = self.product_table.horizontalHeaderItem(9)
        item.setText(_translate("QWidget", "?????????"))
        item = self.product_table.horizontalHeaderItem(10)
        item.setText(_translate("QWidget", "?????????"))
        item = self.product_table.horizontalHeaderItem(11)
        item.setText(_translate("QWidget", "?????????"))
        item = self.product_table.horizontalHeaderItem(12)
        item.setText(_translate("QWidget", "?????????"))
        self.cur_pos_product.setText(_translate("QWidget", "0/3600"))
        self.cur_pos.setText(_translate("QWidget", "0/3600"))
        self.cur_state.setText(_translate("QWidget", "-"))
        self.cur_product_state.setText(_translate("QWidget", "-"))
        self.list_title.setText(_translate("QWidget", "URL List"))
        item = self.except_table.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "?????????????????????"))
        item = self.except_table.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "???????????????"))
        item = self.except_table.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "????????????URL"))
        item = self.except_table.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "?????????"))
        item = self.except_table.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "?????????"))
        item = self.except_table.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "??????"))
        item = self.except_table.horizontalHeaderItem(6)
        item.setText(_translate("QWidget", "30????????????"))
        item = self.except_table.horizontalHeaderItem(7)
        item.setText(_translate("QWidget", "5???????????????"))
        item = self.except_table.horizontalHeaderItem(8)
        item.setText(_translate("QWidget", "????????????"))
        item = self.except_table.horizontalHeaderItem(9)
        item.setText(_translate("QWidget", "??????"))
