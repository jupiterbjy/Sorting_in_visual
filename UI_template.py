# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sorter_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(681, 480)
        self.Start_button = QtWidgets.QPushButton(MainForm)
        self.Start_button.setGeometry(QtCore.QRect(440, 450, 70, 23))
        self.Start_button.setAutoDefault(False)
        self.Start_button.setDefault(False)
        self.Start_button.setFlat(False)
        self.Start_button.setObjectName("Start_button")
        self.Stop_Button = QtWidgets.QPushButton(MainForm)
        self.Stop_Button.setGeometry(QtCore.QRect(520, 450, 70, 23))
        self.Stop_Button.setObjectName("Stop_Button")
        self.Reset_Button = QtWidgets.QPushButton(MainForm)
        self.Reset_Button.setGeometry(QtCore.QRect(600, 450, 70, 23))
        self.Reset_Button.setObjectName("Reset_Button")
        self.Delay_Spin = QtWidgets.QSpinBox(MainForm)
        self.Delay_Spin.setGeometry(QtCore.QRect(350, 450, 81, 22))
        self.Delay_Spin.setMinimum(5)
        self.Delay_Spin.setMaximum(10000)
        self.Delay_Spin.setSingleStep(5)
        self.Delay_Spin.setProperty("value", 20)
        self.Delay_Spin.setObjectName("Delay_Spin")
        self.Nums_Spin = QtWidgets.QSpinBox(MainForm)
        self.Nums_Spin.setGeometry(QtCore.QRect(260, 450, 81, 22))
        self.Nums_Spin.setMinimum(10)
        self.Nums_Spin.setMaximum(100000)
        self.Nums_Spin.setProperty("value", 50)
        self.Nums_Spin.setObjectName("Nums_Spin")
        self.Sorts_Combo = QtWidgets.QComboBox(MainForm)
        self.Sorts_Combo.setGeometry(QtCore.QRect(15, 450, 231, 22))
        self.Sorts_Combo.setWhatsThis("")
        self.Sorts_Combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sorts_Combo.setMinimumContentsLength(0)
        self.Sorts_Combo.setFrame(True)
        self.Sorts_Combo.setObjectName("Sorts_Combo")
        self.widget = QtWidgets.QWidget(MainForm)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(10, 350, 501, 91))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.ConsoleOut_textedit = QtWidgets.QTextEdit(self.widget)
        self.ConsoleOut_textedit.setGeometry(QtCore.QRect(0, 0, 501, 91))
        self.ConsoleOut_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ConsoleOut_textedit.setObjectName("ConsoleOut_textedit")
        self.VisualArea = PlotWidget(MainForm)
        self.VisualArea.setGeometry(QtCore.QRect(10, 10, 501, 331))
        self.VisualArea.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.VisualArea.setObjectName("VisualArea")
        self.Sorts_List = QtWidgets.QListWidget(MainForm)
        self.Sorts_List.setGeometry(QtCore.QRect(520, 10, 151, 431))
        self.Sorts_List.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Sorts_List.setAlternatingRowColors(True)
        self.Sorts_List.setObjectName("Sorts_List")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Sorting in Visual"))
        self.Start_button.setText(_translate("MainForm", "Start"))
        self.Stop_Button.setText(_translate("MainForm", "Stop"))
        self.Reset_Button.setText(_translate("MainForm", "Reset"))
        self.Delay_Spin.setSuffix(_translate("MainForm", " ms"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
