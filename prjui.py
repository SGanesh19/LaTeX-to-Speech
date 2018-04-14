import sys
from PyQt4 import QtGui
from Mainui import Ui_MainWindow
from getEquation import executetxt,executefile
from about import Ui_Aboutwindow

class Aboutwindow(QtGui.QMainWindow, Ui_Aboutwindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("win_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
#        self.label_2.setIcon(icon)
        self.setupUi(self)

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("win_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.ui.about.triggered.connect(self.About)
        self.popAboutDialog=Aboutwindow()

        self.ui.selectfile.clicked.connect(self.openfile)
        self.ui.Open.triggered.connect(self.openfile)
        self.ui.txtasinp.setChecked(True)
        self.ui.Input1.setFocus()
        self.ui.txtasinp.clicked.connect(self.settxtasinp)
        self.ui.fileasinp.clicked.connect(self.setfileasinp)
        self.ui.txtclear.clicked.connect(self.cleartxt)
        self.ui.fileclear.clicked.connect(self.clearfile)
        self.ui.exit.triggered.connect(self.closeEvent)

        self.ui.statusbar.showMessage("**Important note: The software requires network connectivity for proper functioning**")
        if self.ui.mConvert.triggered:
            self.ui.mConvert.triggered.connect(self.load)
            self.ui.mConvert.triggered.connect(self.convertion)
        if self.ui.converbt.clicked:
            self.ui.converbt.clicked.connect(self.load)
            self.ui.converbt.clicked.connect(self.convertion)

    def closeEvent(self,event):

        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            event.ignore()

    def About(self):
        self.popAboutDialog.show()
    def convcmd(self):
        self.ui.converbt.clicked.connect(self.load)
        self.ui.converbt.clicked.connect(self.convertion)
    #Used to clear the txt box contents
    def cleartxt(self):
        self.ui.Input1.clear()

    #Used to clear th input path and set default text to line Edit field
    def clearfile(self):
        self.ui.selectedfileedit.clear()
        self.ui.selectedfileedit.setText("--Select--")
        self.ui.fileprgssbr.setValue(0)
        self.ui.convertprgss.setValue(0)

    #Set text box contents as source input for convertion
    def settxtasinp(self):

        self.ui.txtasinp.setChecked(True)
        self.ui.fileasinp.setChecked(False)
    #Set file as source input for convertion
    def setfileasinp(self):
        self.ui.fileasinp.setChecked(True)
        self.ui.txtasinp.setChecked(False)
    #Function used to open a file as input to the system
    def openfile(self):
        self.ui.txtasinp.setChecked(False)
        self.ui.fileasinp.setChecked(True)
        path = QtGui.QFileDialog.getOpenFileName(self,'Open file', ' ',"LaTeX Files (*.tex)")
        self.ui.selectedfileedit.setText(path)
        if path:
            self.fileload()
            self.load()
            executefile(path)
        else:
            print("No file is selected for convertion!")
            self.ui.selectedfileedit.setText("--Select--")
    #Used in loading the progress bar(fileprgssbr) for file import
    def fileload(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.ui.fileprgssbr.setValue(self.completed)
    #progress bar depicts the execution of convert funtion
    def load(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.ui.convertprgss.setValue(self.completed)
    #Main convertion process
    def convertion(self,filepath):
        if self.ui.txtasinp.isDown:
            inputstr= (self.ui.Input1).toPlainText()
            print(inputstr)
            executetxt(inputstr)
            self.ui.convertprgss.setValue(0)
        else:
            print("Not a valid Input")

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
