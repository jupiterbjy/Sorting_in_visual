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
        MainForm.resize(640, 480)
        self.Start_button = QtWidgets.QPushButton(MainForm)
        self.Start_button.setGeometry(QtCore.QRect(400, 450, 75, 23))
        self.Start_button.setAutoDefault(False)
        self.Start_button.setDefault(False)
        self.Start_button.setObjectName("Start_button")
        self.Stop_Button = QtWidgets.QPushButton(MainForm)
        self.Stop_Button.setGeometry(QtCore.QRect(480, 450, 75, 23))
        self.Stop_Button.setObjectName("Stop_Button")
        self.Reset_Button = QtWidgets.QPushButton(MainForm)
        self.Reset_Button.setGeometry(QtCore.QRect(560, 450, 75, 23))
        self.Reset_Button.setObjectName("Reset_Button")
        self.Sorts_ListView = QtWidgets.QListView(MainForm)
        self.Sorts_ListView.setGeometry(QtCore.QRect(520, 10, 111, 431))
        self.Sorts_ListView.setObjectName("Sorts_ListView")
        self.Delay_Spin = QtWidgets.QSpinBox(MainForm)
        self.Delay_Spin.setGeometry(QtCore.QRect(311, 450, 81, 22))
        self.Delay_Spin.setObjectName("Delay_Spin")
        self.Nums_Spin = QtWidgets.QSpinBox(MainForm)
        self.Nums_Spin.setGeometry(QtCore.QRect(220, 450, 81, 22))
        self.Nums_Spin.setObjectName("Nums_Spin")
        self.Sorts_Combo = QtWidgets.QComboBox(MainForm)
        self.Sorts_Combo.setGeometry(QtCore.QRect(15, 450, 191, 22))
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
        self.Console_verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.Console_verticalScrollBar.setGeometry(QtCore.QRect(480, 0, 20, 91))
        self.Console_verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.Console_verticalScrollBar.setObjectName("Console_verticalScrollBar")
        self.ConsoleOut_textedit = QtWidgets.QTextEdit(self.widget)
        self.ConsoleOut_textedit.setGeometry(QtCore.QRect(0, 0, 471, 91))
        self.ConsoleOut_textedit.setObjectName("ConsoleOut_textedit")
        self.VisualArea = QtWidgets.QWidget(MainForm)
        self.VisualArea.setGeometry(QtCore.QRect(10, 10, 501, 331))
        self.VisualArea.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.VisualArea.setObjectName("VisualArea")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Sorting in Visual"))
        self.Start_button.setText(_translate("MainForm", "Start"))
        self.Stop_Button.setText(_translate("MainForm", "Stop"))
        self.Reset_Button.setText(_translate("MainForm", "Reset"))
        self.Delay_Spin.setSuffix(_translate("MainForm", " ms"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
