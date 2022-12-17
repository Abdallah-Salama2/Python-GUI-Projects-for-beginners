from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from qtconsole.qtconsoleapp import QtCore


class Main(QMainWindow):    #inherits from Qmain Window cuz our mainui is Qmain window too
    def __init__(self):     #function gets called when ibject is made
        super(Main,self).__init__()
        loadUi("windw.ui", self) #all different widgets in main ui loaded as class atrrib to main class
        todos = ["play code","Walk dog","Buy groceserres"]
        for todo in todos:
            item = QListWidgetItem(todo) #for each string in the list  create qlist item
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable) #dont modify anything with orignal flag ( every q widget have flags)
            # then from | add new flags which is QtCore.Qt.ItemIsUserCheckable) tells pyqt5 go and boxes
            item.setCheckState(QtCore.Qt.Unchecked) # this line perform the func of adding boxes with check state
            self.listWidget.addItem(item)
        self.pushButton.clicked.connect(self.toggleall) # connecting this burron the function toggle all


    def toggleall(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i) # 5soh listwidget ele feha klam w shof item kaza 7oto fe item(QlistWidget)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)



#to execute the app the block code enables us to create Qapplication#
if __name__  == '__main__':
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec()