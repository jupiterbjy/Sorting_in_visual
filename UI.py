# testing with code from
# https://www.learnpyqt.com/courses/graphics-plotting/plotting-pyqtgraph/

import sys
from PyQt5 import QtWidgets, uic

import Sorting_algorithms as sorts
import g_var
from UI_template import Ui_MainForm


class MainWindow(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.plot([1,2,3,4,5,6,7,8,9,10], [9,7,5,4,3,1,2,3,4,5])
        
        self.assignSorter()
        
        self.Sorts_List.currentItemChanged.connect(self.onSortsListChange)
        
    def plot(self, hour, temperature):
        self.VisualArea.plot(hour, temperature)
        
    def assignSorter(self):
        for idx, item in enumerate(sorts.__all__):
            self.Sorts_List.insertItem(idx, item)
            # self.Sorts_Combo.insertItem(idx, item)
        
        # TODO: Change Sorts_Combo into Visualizing method
        
        # self.Sorts_Combo.addItems(sorts.__all__)
    
    def writeConsole(self, text):
        self.ConsoleOut_textedit.append(str(text))
        
    def onSortsListChange(self):
        index = self.Sorts_List.currentRow()
        label = self.Sorts_List.currentItem()
        self.writeConsole(label)
        g_var.sort = label
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()
