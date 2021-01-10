# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brewhouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwindow_brewhouse(object):
    def setupUi(self, mwindow_brewhouse):
        mwindow_brewhouse.setObjectName("mwindow_brewhouse")
        mwindow_brewhouse.resize(700, 825)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        mwindow_brewhouse.setFont(font)
        self.central_widget = QtWidgets.QWidget(mwindow_brewhouse)
        self.central_widget.setObjectName("central_widget")
        self.layoutWidget = QtWidgets.QWidget(self.central_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 681, 801))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vert_layout_brewhouse = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vert_layout_brewhouse.setContentsMargins(0, 0, 0, 0)
        self.vert_layout_brewhouse.setObjectName("vert_layout_brewhouse")
        self.lbl_brewhouse = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_brewhouse.setFont(font)
        self.lbl_brewhouse.setObjectName("lbl_brewhouse")
        self.vert_layout_brewhouse.addWidget(self.lbl_brewhouse)
        self.hori_line_brewhouse = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_brewhouse.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_brewhouse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_brewhouse.setObjectName("hori_line_brewhouse")
        self.vert_layout_brewhouse.addWidget(self.hori_line_brewhouse)
        self.hori_layout_nav = QtWidgets.QHBoxLayout()
        self.hori_layout_nav.setObjectName("hori_layout_nav")
        self.btn_inv_management = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_inv_management.setObjectName("btn_inv_management")
        self.hori_layout_nav.addWidget(self.btn_inv_management, 0, QtCore.Qt.AlignLeft)
        self.btn_process_monitoring = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_process_monitoring.setObjectName("btn_process_monitoring")
        self.hori_layout_nav.addWidget(self.btn_process_monitoring, 0, QtCore.Qt.AlignLeft)
        self.btn_upload_sales = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_upload_sales.setObjectName("btn_upload_sales")
        self.hori_layout_nav.addWidget(self.btn_upload_sales)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hori_layout_nav.addItem(spacerItem)
        self.vert_layout_brewhouse.addLayout(self.hori_layout_nav)
        self.hori_line_nav = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_nav.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_nav.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_nav.setObjectName("hori_line_nav")
        self.vert_layout_brewhouse.addWidget(self.hori_line_nav)
        self.lbl_sales = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_sales.setFont(font)
        self.lbl_sales.setObjectName("lbl_sales")
        self.vert_layout_brewhouse.addWidget(self.lbl_sales)
        self.lbl_overall_sales = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_overall_sales.setObjectName("lbl_overall_sales")
        self.vert_layout_brewhouse.addWidget(self.lbl_overall_sales)
        self.lbl_red_helles_sales = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_red_helles_sales.setObjectName("lbl_red_helles_sales")
        self.vert_layout_brewhouse.addWidget(self.lbl_red_helles_sales)
        self.lbl_pilsner_sales = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pilsner_sales.setObjectName("lbl_pilsner_sales")
        self.vert_layout_brewhouse.addWidget(self.lbl_pilsner_sales)
        self.lbl_dunkel_sales = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dunkel_sales.setObjectName("lbl_dunkel_sales")
        self.vert_layout_brewhouse.addWidget(self.lbl_dunkel_sales)
        self.hori_line_sales = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_sales.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_sales.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_sales.setObjectName("hori_line_sales")
        self.vert_layout_brewhouse.addWidget(self.hori_line_sales)
        self.lbl_ratios = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_ratios.setFont(font)
        self.lbl_ratios.setObjectName("lbl_ratios")
        self.vert_layout_brewhouse.addWidget(self.lbl_ratios)
        self.lbl_red_helles_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_red_helles_ratio.setObjectName("lbl_red_helles_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_red_helles_ratio)
        self.lbl_pilsner_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pilsner_ratio.setObjectName("lbl_pilsner_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_pilsner_ratio)
        self.lbl_dunkel_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dunkel_ratio.setObjectName("lbl_dunkel_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_dunkel_ratio)
        self.hori_line_ratios = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_ratios.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_ratios.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_ratios.setObjectName("hori_line_ratios")
        self.vert_layout_brewhouse.addWidget(self.hori_line_ratios)
        self.lbl_growth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_growth.setFont(font)
        self.lbl_growth.setObjectName("lbl_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_growth)
        self.lbl_red_helles_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_red_helles_growth.setObjectName("lbl_red_helles_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_red_helles_growth)
        self.lbl_pilsner_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pilsner_growth.setObjectName("lbl_pilsner_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_pilsner_growth)
        self.lbl_dunkel_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dunkel_growth.setObjectName("lbl_dunkel_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_dunkel_growth)
        self.hori_line_growth = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_growth.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_growth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_growth.setObjectName("hori_line_growth")
        self.vert_layout_brewhouse.addWidget(self.hori_line_growth)
        self.lbl_predict = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_predict.setFont(font)
        self.lbl_predict.setObjectName("lbl_predict")
        self.vert_layout_brewhouse.addWidget(self.lbl_predict)
        self.hori_layout_predict = QtWidgets.QHBoxLayout()
        self.hori_layout_predict.setObjectName("hori_layout_predict")
        self.lbl_predict_date = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_predict_date.setObjectName("lbl_predict_date")
        self.hori_layout_predict.addWidget(self.lbl_predict_date, 0, QtCore.Qt.AlignLeft)
        self.date_edit_predict = QtWidgets.QDateEdit(self.layoutWidget)
        self.date_edit_predict.setMinimumSize(QtCore.QSize(120, 0))
        self.date_edit_predict.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 31), QtCore.QTime(0, 0, 0)))
        self.date_edit_predict.setCalendarPopup(True)
        self.date_edit_predict.setObjectName("date_edit_predict")
        self.hori_layout_predict.addWidget(self.date_edit_predict, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hori_layout_predict.addItem(spacerItem1)
        self.vert_layout_brewhouse.addLayout(self.hori_layout_predict)
        self.lbl_predictions = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_predictions.setText("")
        self.lbl_predictions.setObjectName("lbl_predictions")
        self.vert_layout_brewhouse.addWidget(self.lbl_predictions)
        self.btn_predict = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_predict.setObjectName("btn_predict")
        self.vert_layout_brewhouse.addWidget(self.btn_predict, 0, QtCore.Qt.AlignLeft)
        self.hori_line_predict = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_predict.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_predict.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_predict.setObjectName("hori_line_predict")
        self.vert_layout_brewhouse.addWidget(self.hori_line_predict)
        self.lbl_production_advice = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_production_advice.setFont(font)
        self.lbl_production_advice.setObjectName("lbl_production_advice")
        self.vert_layout_brewhouse.addWidget(self.lbl_production_advice)
        self.lbl_advice = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_advice.setText("")
        self.lbl_advice.setObjectName("lbl_advice")
        self.vert_layout_brewhouse.addWidget(self.lbl_advice)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vert_layout_brewhouse.addItem(spacerItem2)
        mwindow_brewhouse.setCentralWidget(self.central_widget)

        self.retranslateUi(mwindow_brewhouse)
        QtCore.QMetaObject.connectSlotsByName(mwindow_brewhouse)

    def retranslateUi(self, mwindow_brewhouse):
        _translate = QtCore.QCoreApplication.translate
        mwindow_brewhouse.setWindowTitle(_translate("mwindow_brewhouse", "Barnaby\'s Brewhouse"))
        self.lbl_brewhouse.setText(_translate("mwindow_brewhouse", "Barnaby\'s Brewhouse"))
        self.btn_inv_management.setText(_translate("mwindow_brewhouse", "Inventory Management"))
        self.btn_process_monitoring.setText(_translate("mwindow_brewhouse", "Process Monitoring"))
        self.btn_upload_sales.setText(_translate("mwindow_brewhouse", "Upload Sales Data"))
        self.lbl_sales.setText(_translate("mwindow_brewhouse", "Total Sales (November 2018 to October 2019)"))
        self.lbl_overall_sales.setText(_translate("mwindow_brewhouse", "Overall: "))
        self.lbl_red_helles_sales.setText(_translate("mwindow_brewhouse", "Organic Red Helles: "))
        self.lbl_pilsner_sales.setText(_translate("mwindow_brewhouse", "Organic Pilsner: "))
        self.lbl_dunkel_sales.setText(_translate("mwindow_brewhouse", "Organic Dunkel: "))
        self.lbl_ratios.setText(_translate("mwindow_brewhouse", "Sales Ratios (November 2018 to October 2019)"))
        self.lbl_red_helles_ratio.setText(_translate("mwindow_brewhouse", "Organic Red Helles: "))
        self.lbl_pilsner_ratio.setText(_translate("mwindow_brewhouse", "Organic Pilsner: "))
        self.lbl_dunkel_ratio.setText(_translate("mwindow_brewhouse", "Organic Dunkel:"))
        self.lbl_growth.setText(_translate("mwindow_brewhouse", "Average Monthly Growth Percentages (November 2018 to October 2019)"))
        self.lbl_red_helles_growth.setText(_translate("mwindow_brewhouse", "Organic Red Helles: "))
        self.lbl_pilsner_growth.setText(_translate("mwindow_brewhouse", "Organic Pilsner: "))
        self.lbl_dunkel_growth.setText(_translate("mwindow_brewhouse", "Organic Dunkel: "))
        self.lbl_predict.setText(_translate("mwindow_brewhouse", "Predicted Sales"))
        self.lbl_predict_date.setText(_translate("mwindow_brewhouse", "Date (DD/MM/YYYY):"))
        self.btn_predict.setText(_translate("mwindow_brewhouse", "Update Sales Prediction"))
        self.lbl_production_advice.setText(_translate("mwindow_brewhouse", "Beer Production Advice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwindow_brewhouse = QtWidgets.QMainWindow()
    ui = Ui_mwindow_brewhouse()
    ui.setupUi(mwindow_brewhouse)
    mwindow_brewhouse.show()
    sys.exit(app.exec_())
