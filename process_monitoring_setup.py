# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process_monitoring.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_monitoring(object):
    def setupUi(self, dialog_monitoring):
        dialog_monitoring.setObjectName("dialog_monitoring")
        dialog_monitoring.resize(800, 950)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        dialog_monitoring.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(dialog_monitoring)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll_area = QtWidgets.QScrollArea(dialog_monitoring)
        font = QtGui.QFont()
        font.setKerning(True)
        self.scroll_area.setFont(font)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scroll_area.setLineWidth(0)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(
            QtCore.QRect(0, 0, 778, 928))
        self.scroll_area_widget_contents.setObjectName(
            "scroll_area_widget_contents")
        self.verticalLayoutWidget = QtWidgets.QWidget(
            self.scroll_area_widget_contents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 720, 921))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vert_layout_monitoring = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.vert_layout_monitoring.setContentsMargins(0, 0, 0, 0)
        self.vert_layout_monitoring.setObjectName("vert_layout_monitoring")
        self.lbl_monitoring = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setKerning(True)
        self.lbl_monitoring.setFont(font)
        self.lbl_monitoring.setObjectName("lbl_monitoring")
        self.vert_layout_monitoring.addWidget(self.lbl_monitoring)
        self.hori_line_monitoring = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.hori_line_monitoring.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_monitoring.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_monitoring.setObjectName("hori_line_monitoring")
        self.vert_layout_monitoring.addWidget(self.hori_line_monitoring)
        self.lbl_tank_availability = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_tank_availability.setFont(font)
        self.lbl_tank_availability.setObjectName("lbl_tank_availability")
        self.vert_layout_monitoring.addWidget(self.lbl_tank_availability)
        self.lbl_tanks = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_tanks.setText("")
        self.lbl_tanks.setObjectName("lbl_tanks")
        self.vert_layout_monitoring.addWidget(self.lbl_tanks)
        self.hori_line_tanks = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.hori_line_tanks.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_tanks.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_tanks.setObjectName("hori_line_tanks")
        self.vert_layout_monitoring.addWidget(self.hori_line_tanks)
        self.lbl_ongoing_processes = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_ongoing_processes.setFont(font)
        self.lbl_ongoing_processes.setObjectName("lbl_ongoing_processes")
        self.vert_layout_monitoring.addWidget(self.lbl_ongoing_processes)
        self.btn_refresh_processes = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_refresh_processes.setObjectName("btn_refresh_processes")
        self.vert_layout_monitoring.addWidget(
            self.btn_refresh_processes, 0, QtCore.Qt.AlignLeft)
        self.lbl_processes = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_processes.setText("")
        self.lbl_processes.setObjectName("lbl_processes")
        self.vert_layout_monitoring.addWidget(self.lbl_processes)
        self.hori_line_ongoing_processes = QtWidgets.QFrame(
            self.verticalLayoutWidget)
        self.hori_line_ongoing_processes.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_ongoing_processes.setFrameShadow(
            QtWidgets.QFrame.Sunken)
        self.hori_line_ongoing_processes.setObjectName(
            "hori_line_ongoing_processes")
        self.vert_layout_monitoring.addWidget(self.hori_line_ongoing_processes)
        self.grid_layout_start_process = QtWidgets.QGridLayout()
        self.grid_layout_start_process.setObjectName(
            "grid_layout_start_process")
        self.lbl_vertical_placeholder = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.lbl_vertical_placeholder.setText("")
        self.lbl_vertical_placeholder.setObjectName("lbl_vertical_placeholder")
        self.grid_layout_start_process.addWidget(
            self.lbl_vertical_placeholder, 0, 2, 1, 1)
        self.lbl_condition_volume = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_condition_volume.setObjectName("lbl_condition_volume")
        self.grid_layout_start_process.addWidget(
            self.lbl_condition_volume, 9, 0, 1, 1)
        self.line_edit_bottle_volume = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.line_edit_bottle_volume.setObjectName("line_edit_bottle_volume")
        self.grid_layout_start_process.addWidget(
            self.line_edit_bottle_volume, 8, 4, 1, 1)
        self.lbl_bottle_recipe = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_bottle_recipe.setObjectName("lbl_bottle_recipe")
        self.grid_layout_start_process.addWidget(
            self.lbl_bottle_recipe, 7, 3, 1, 1)
        self.combo_box_ferment_tank = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_ferment_tank.setObjectName("combo_box_ferment_tank")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.combo_box_ferment_tank.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_ferment_tank, 2, 4, 1, 1)
        self.lbl_hori_placeholder = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_hori_placeholder.setText("")
        self.lbl_hori_placeholder.setObjectName("lbl_hori_placeholder")
        self.grid_layout_start_process.addWidget(
            self.lbl_hori_placeholder, 5, 3, 1, 1)
        self.btn_start_bottling = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_start_bottling.setObjectName("btn_start_bottling")
        self.grid_layout_start_process.addWidget(
            self.btn_start_bottling, 10, 3, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lbl_condition_tank = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_condition_tank.setObjectName("lbl_condition_tank")
        self.grid_layout_start_process.addWidget(
            self.lbl_condition_tank, 8, 0, 1, 1)
        self.line_edit_brew_volume = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.line_edit_brew_volume.setObjectName("line_edit_brew_volume")
        self.grid_layout_start_process.addWidget(
            self.line_edit_brew_volume, 2, 1, 1, 1)
        self.lbl_ferment_volume = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ferment_volume.setObjectName("lbl_ferment_volume")
        self.grid_layout_start_process.addWidget(
            self.lbl_ferment_volume, 3, 3, 1, 1)
        self.btn_start_conditioning = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_start_conditioning.setObjectName("btn_start_conditioning")
        self.grid_layout_start_process.addWidget(
            self.btn_start_conditioning, 10, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.line_edit_condition_volume = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.line_edit_condition_volume.setObjectName(
            "line_edit_condition_volume")
        self.grid_layout_start_process.addWidget(
            self.line_edit_condition_volume, 9, 1, 1, 1)
        self.combo_box_ferment_recipe = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_ferment_recipe.setObjectName("combo_box_ferment_recipe")
        self.combo_box_ferment_recipe.addItem("")
        self.combo_box_ferment_recipe.addItem("")
        self.combo_box_ferment_recipe.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_ferment_recipe, 1, 4, 1, 1)
        self.lbl_start_bottling = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_start_bottling.setFont(font)
        self.lbl_start_bottling.setObjectName("lbl_start_bottling")
        self.grid_layout_start_process.addWidget(
            self.lbl_start_bottling, 6, 3, 1, 1)
        self.line_edit_ferment_volume = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.line_edit_ferment_volume.setObjectName("line_edit_ferment_volume")
        self.grid_layout_start_process.addWidget(
            self.line_edit_ferment_volume, 3, 4, 1, 1)
        self.lbl_ferment_tank = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ferment_tank.setObjectName("lbl_ferment_tank")
        self.grid_layout_start_process.addWidget(
            self.lbl_ferment_tank, 2, 3, 1, 1)
        self.lbl_brew_recipe = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_brew_recipe.setObjectName("lbl_brew_recipe")
        self.grid_layout_start_process.addWidget(
            self.lbl_brew_recipe, 1, 0, 1, 1)
        self.lbl_start_conditioning = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_start_conditioning.setFont(font)
        self.lbl_start_conditioning.setObjectName("lbl_start_conditioning")
        self.grid_layout_start_process.addWidget(
            self.lbl_start_conditioning, 6, 0, 1, 1)
        self.lbl_bottle_volume = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_bottle_volume.setObjectName("lbl_bottle_volume")
        self.grid_layout_start_process.addWidget(
            self.lbl_bottle_volume, 8, 3, 1, 1)
        self.lbl_ferment_recipe = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ferment_recipe.setObjectName("lbl_ferment_recipe")
        self.grid_layout_start_process.addWidget(
            self.lbl_ferment_recipe, 1, 3, 1, 1)
        self.lbl_brew_volume = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_brew_volume.setObjectName("lbl_brew_volume")
        self.grid_layout_start_process.addWidget(
            self.lbl_brew_volume, 2, 0, 1, 1)
        self.combo_box_bottle_recipe = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_bottle_recipe.setObjectName("combo_box_bottle_recipe")
        self.combo_box_bottle_recipe.addItem("")
        self.combo_box_bottle_recipe.addItem("")
        self.combo_box_bottle_recipe.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_bottle_recipe, 7, 4, 1, 1)
        self.combo_box_brew_recipe = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_brew_recipe.setObjectName("combo_box_brew_recipe")
        self.combo_box_brew_recipe.addItem("")
        self.combo_box_brew_recipe.addItem("")
        self.combo_box_brew_recipe.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_brew_recipe, 1, 1, 1, 1)
        self.combo_box_condition_tank = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_condition_tank.setObjectName("combo_box_condition_tank")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.combo_box_condition_tank.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_condition_tank, 8, 1, 1, 1)
        self.lbl_condition_recipe = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_condition_recipe.setObjectName("lbl_condition_recipe")
        self.grid_layout_start_process.addWidget(
            self.lbl_condition_recipe, 7, 0, 1, 1)
        self.combo_box_condition_recipe = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_condition_recipe.setObjectName(
            "combo_box_condition_recipe")
        self.combo_box_condition_recipe.addItem("")
        self.combo_box_condition_recipe.addItem("")
        self.combo_box_condition_recipe.addItem("")
        self.grid_layout_start_process.addWidget(
            self.combo_box_condition_recipe, 7, 1, 1, 1)
        self.lbl_start_fermentation = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_start_fermentation.setFont(font)
        self.lbl_start_fermentation.setObjectName("lbl_start_fermentation")
        self.grid_layout_start_process.addWidget(
            self.lbl_start_fermentation, 0, 3, 1, 1)
        self.lbl_start_brew = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_start_brew.setFont(font)
        self.lbl_start_brew.setObjectName("lbl_start_brew")
        self.grid_layout_start_process.addWidget(
            self.lbl_start_brew, 0, 0, 1, 1)
        self.btn_start_fermentation = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_start_fermentation.setObjectName("btn_start_fermentation")
        self.grid_layout_start_process.addWidget(
            self.btn_start_fermentation, 4, 3, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.btn_start_hot_brew = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_start_hot_brew.setObjectName("btn_start_hot_brew")
        self.grid_layout_start_process.addWidget(
            self.btn_start_hot_brew, 4, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.vert_layout_monitoring.addLayout(self.grid_layout_start_process)
        self.hori_line_start_process = QtWidgets.QFrame(
            self.verticalLayoutWidget)
        self.hori_line_start_process.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_start_process.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_start_process.setObjectName("hori_line_start_process")
        self.vert_layout_monitoring.addWidget(self.hori_line_start_process)
        self.lbl_abort_process = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(True)
        self.lbl_abort_process.setFont(font)
        self.lbl_abort_process.setObjectName("lbl_abort_process")
        self.vert_layout_monitoring.addWidget(self.lbl_abort_process)
        self.grid_layout_abort_process = QtWidgets.QGridLayout()
        self.grid_layout_abort_process.setObjectName(
            "grid_layout_abort_process")
        self.line_edit_abort_volume = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.line_edit_abort_volume.setObjectName("line_edit_abort_volume")
        self.grid_layout_abort_process.addWidget(
            self.line_edit_abort_volume, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.combo_box_abort_process = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_abort_process.setObjectName("combo_box_abort_process")
        self.combo_box_abort_process.addItem("")
        self.combo_box_abort_process.addItem("")
        self.combo_box_abort_process.addItem("")
        self.combo_box_abort_process.addItem("")
        self.grid_layout_abort_process.addWidget(
            self.combo_box_abort_process, 0, 1, 1, 1)
        self.lbl_abort_recipe = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_abort_recipe.setObjectName("lbl_abort_recipe")
        self.grid_layout_abort_process.addWidget(
            self.lbl_abort_recipe, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lbl_abort = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_abort.setObjectName("lbl_abort")
        self.grid_layout_abort_process.addWidget(self.lbl_abort, 0, 0, 1, 1)
        self.lbl_abort_tank = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_abort_tank.setObjectName("lbl_abort_tank")
        self.grid_layout_abort_process.addWidget(
            self.lbl_abort_tank, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lbl_abort_volume = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_abort_volume.setObjectName("lbl_abort_volume")
        self.grid_layout_abort_process.addWidget(
            self.lbl_abort_volume, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.combo_box_abort_tank = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_abort_tank.setObjectName("combo_box_abort_tank")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.combo_box_abort_tank.addItem("")
        self.grid_layout_abort_process.addWidget(
            self.combo_box_abort_tank, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.date_time_edit_completion = QtWidgets.QDateTimeEdit(
            self.verticalLayoutWidget)
        self.date_time_edit_completion.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(2019, 10, 31), QtCore.QTime(0, 0, 0)))
        self.date_time_edit_completion.setCalendarPopup(True)
        self.date_time_edit_completion.setObjectName(
            "date_time_edit_completion")
        self.grid_layout_abort_process.addWidget(
            self.date_time_edit_completion, 4, 1, 1, 1)
        self.combo_box_abort_recipe = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.combo_box_abort_recipe.setObjectName("combo_box_abort_recipe")
        self.combo_box_abort_recipe.addItem("")
        self.combo_box_abort_recipe.addItem("")
        self.combo_box_abort_recipe.addItem("")
        self.grid_layout_abort_process.addWidget(
            self.combo_box_abort_recipe, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.lbl_abort_completion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_abort_completion.setObjectName("lbl_abort_completion")
        self.grid_layout_abort_process.addWidget(
            self.lbl_abort_completion, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout_abort_process.addItem(spacerItem, 1, 2, 1, 1)
        self.vert_layout_monitoring.addLayout(self.grid_layout_abort_process)
        self.btn_abort_process = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.btn_abort_process.setObjectName("btn_abort_process")
        self.vert_layout_monitoring.addWidget(
            self.btn_abort_process, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vert_layout_monitoring.addItem(spacerItem1)
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.gridLayout.addWidget(self.scroll_area, 0, 0, 1, 1)

        self.retranslateUi(dialog_monitoring)
        QtCore.QMetaObject.connectSlotsByName(dialog_monitoring)

    def retranslateUi(self, dialog_monitoring):
        _translate = QtCore.QCoreApplication.translate
        dialog_monitoring.setWindowTitle(_translate(
            "dialog_monitoring", "Process Monitoring - Barnaby\'s Brewhouse"))
        self.lbl_monitoring.setText(_translate(
            "dialog_monitoring", "Process Monitoring"))
        self.lbl_tank_availability.setText(_translate(
            "dialog_monitoring", "Tank Availability"))
        self.lbl_ongoing_processes.setText(_translate(
            "dialog_monitoring", "Ongoing Processes"))
        self.btn_refresh_processes.setText(_translate(
            "dialog_monitoring", "Refresh Processes"))
        self.lbl_condition_volume.setText(
            _translate("dialog_monitoring", "Volume (L):"))
        self.lbl_bottle_recipe.setText(
            _translate("dialog_monitoring", "Beer Recipe:"))
        self.combo_box_ferment_tank.setItemText(
            0, _translate("dialog_monitoring", "Albert"))
        self.combo_box_ferment_tank.setItemText(
            1, _translate("dialog_monitoring", "Brigadier"))
        self.combo_box_ferment_tank.setItemText(
            2, _translate("dialog_monitoring", "Camilla"))
        self.combo_box_ferment_tank.setItemText(
            3, _translate("dialog_monitoring", "Dylon"))
        self.combo_box_ferment_tank.setItemText(
            4, _translate("dialog_monitoring", "Emily"))
        self.combo_box_ferment_tank.setItemText(
            5, _translate("dialog_monitoring", "Florence "))
        self.combo_box_ferment_tank.setItemText(
            6, _translate("dialog_monitoring", "R2D2"))
        self.btn_start_bottling.setText(_translate(
            "dialog_monitoring", "Start Bottling"))
        self.lbl_condition_tank.setText(
            _translate("dialog_monitoring", "Tank:"))
        self.lbl_ferment_volume.setText(
            _translate("dialog_monitoring", "Volume (L):"))
        self.btn_start_conditioning.setText(_translate(
            "dialog_monitoring", "Start Conditioning"))
        self.combo_box_ferment_recipe.setItemText(
            0, _translate("dialog_monitoring", "Organic Red Helles"))
        self.combo_box_ferment_recipe.setItemText(
            1, _translate("dialog_monitoring", "Organic Pilsner"))
        self.combo_box_ferment_recipe.setItemText(
            2, _translate("dialog_monitoring", "Organic Dunkel"))
        self.lbl_start_bottling.setText(_translate(
            "dialog_monitoring", "Start Bottling"))
        self.lbl_ferment_tank.setText(_translate("dialog_monitoring", "Tank:"))
        self.lbl_brew_recipe.setText(_translate(
            "dialog_monitoring", "Beer Recipe:"))
        self.lbl_start_conditioning.setText(_translate(
            "dialog_monitoring", "Start Conditioning"))
        self.lbl_bottle_volume.setText(
            _translate("dialog_monitoring", "Volume (L):"))
        self.lbl_ferment_recipe.setText(
            _translate("dialog_monitoring", "Beer Recipe:"))
        self.lbl_brew_volume.setText(_translate(
            "dialog_monitoring", "Volume (L):"))
        self.combo_box_bottle_recipe.setItemText(
            0, _translate("dialog_monitoring", "Organic Red Helles"))
        self.combo_box_bottle_recipe.setItemText(
            1, _translate("dialog_monitoring", "Organic Pilsner"))
        self.combo_box_bottle_recipe.setItemText(
            2, _translate("dialog_monitoring", "Organic Dunkel"))
        self.combo_box_brew_recipe.setItemText(
            0, _translate("dialog_monitoring", "Organic Red Helles"))
        self.combo_box_brew_recipe.setItemText(
            1, _translate("dialog_monitoring", "Organic Pilsner"))
        self.combo_box_brew_recipe.setItemText(
            2, _translate("dialog_monitoring", "Organic Dunkel"))
        self.combo_box_condition_tank.setItemText(
            0, _translate("dialog_monitoring", "Albert"))
        self.combo_box_condition_tank.setItemText(
            1, _translate("dialog_monitoring", "Brigadier"))
        self.combo_box_condition_tank.setItemText(
            2, _translate("dialog_monitoring", "Camilla"))
        self.combo_box_condition_tank.setItemText(
            3, _translate("dialog_monitoring", "Dylon"))
        self.combo_box_condition_tank.setItemText(
            4, _translate("dialog_monitoring", "Emily"))
        self.combo_box_condition_tank.setItemText(
            5, _translate("dialog_monitoring", "Florence "))
        self.combo_box_condition_tank.setItemText(
            6, _translate("dialog_monitoring", "Gertrude"))
        self.combo_box_condition_tank.setItemText(
            7, _translate("dialog_monitoring", "Harry"))
        self.lbl_condition_recipe.setText(
            _translate("dialog_monitoring", "Beer Recipe:"))
        self.combo_box_condition_recipe.setItemText(
            0, _translate("dialog_monitoring", "Organic Red Helles"))
        self.combo_box_condition_recipe.setItemText(
            1, _translate("dialog_monitoring", "Organic Pilsner"))
        self.combo_box_condition_recipe.setItemText(
            2, _translate("dialog_monitoring", "Organic Dunkel"))
        self.lbl_start_fermentation.setText(_translate(
            "dialog_monitoring", "Start Fermentation"))
        self.lbl_start_brew.setText(_translate(
            "dialog_monitoring", "Start Hot Brew"))
        self.btn_start_fermentation.setText(_translate(
            "dialog_monitoring", "Start Fermentation"))
        self.btn_start_hot_brew.setText(_translate(
            "dialog_monitoring", "Start Hot Brew"))
        self.lbl_abort_process.setText(_translate(
            "dialog_monitoring", "Abort Process"))
        self.combo_box_abort_process.setItemText(
            0, _translate("dialog_monitoring", "Hot Brew"))
        self.combo_box_abort_process.setItemText(
            1, _translate("dialog_monitoring", "Fermentation"))
        self.combo_box_abort_process.setItemText(
            2, _translate("dialog_monitoring", "Conditioning"))
        self.combo_box_abort_process.setItemText(
            3, _translate("dialog_monitoring", "Bottling"))
        self.lbl_abort_recipe.setText(_translate(
            "dialog_monitoring", "Beer Recipe:"))
        self.lbl_abort.setText(_translate("dialog_monitoring", "Process:"))
        self.lbl_abort_tank.setText(_translate("dialog_monitoring", "Tank:"))
        self.lbl_abort_volume.setText(
            _translate("dialog_monitoring", "Volume (L):"))
        self.combo_box_abort_tank.setItemText(
            0, _translate("dialog_monitoring", "N/A"))
        self.combo_box_abort_tank.setItemText(
            1, _translate("dialog_monitoring", "Albert"))
        self.combo_box_abort_tank.setItemText(
            2, _translate("dialog_monitoring", "Brigadier"))
        self.combo_box_abort_tank.setItemText(
            3, _translate("dialog_monitoring", "Camilla"))
        self.combo_box_abort_tank.setItemText(
            4, _translate("dialog_monitoring", "Dylon"))
        self.combo_box_abort_tank.setItemText(
            5, _translate("dialog_monitoring", "Emily"))
        self.combo_box_abort_tank.setItemText(
            6, _translate("dialog_monitoring", "Florence "))
        self.combo_box_abort_tank.setItemText(
            7, _translate("dialog_monitoring", "Gertrude"))
        self.combo_box_abort_tank.setItemText(
            8, _translate("dialog_monitoring", "Harry"))
        self.combo_box_abort_tank.setItemText(
            9, _translate("dialog_monitoring", "R2D2"))
        self.date_time_edit_completion.setDisplayFormat(
            _translate("dialog_monitoring", "dd/MM/yyyy hh:mm:ss"))
        self.combo_box_abort_recipe.setItemText(
            0, _translate("dialog_monitoring", "Organic Red Helles"))
        self.combo_box_abort_recipe.setItemText(
            1, _translate("dialog_monitoring", "Organic Pilsner"))
        self.combo_box_abort_recipe.setItemText(
            2, _translate("dialog_monitoring", "Organic Dunkel"))
        self.lbl_abort_completion.setText(
            _translate("dialog_monitoring", "Completion:"))
        self.btn_abort_process.setText(_translate(
            "dialog_monitoring", "Abort Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_monitoring = QtWidgets.QDialog()
    ui = Ui_dialog_monitoring()
    ui.setupUi(dialog_monitoring)
    dialog_monitoring.show()
    sys.exit(app.exec_())
