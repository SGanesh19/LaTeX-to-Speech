# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Aboutwindow(object):
    def setupUi(self, Aboutwindow):
        Aboutwindow.setObjectName(_fromUtf8("Aboutwindow"))
        Aboutwindow.resize(761, 327)
        Aboutwindow.setMinimumSize(QtCore.QSize(761, 327))
        Aboutwindow.setMaximumSize(QtCore.QSize(761, 327))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("win_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Aboutwindow.setWindowIcon(icon)
        Aboutwindow.setIconSize(QtCore.QSize(64, 64))
        Aboutwindow.setAnimated(True)
        Aboutwindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(Aboutwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 741, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(220, 40, 421, 141))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 191, 221))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("win_icon.png")))
        self.label_2.setScaledContents(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Aboutwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Aboutwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Aboutwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Aboutwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Aboutwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Aboutwindow)
        QtCore.QMetaObject.connectSlotsByName(Aboutwindow)

    def retranslateUi(self, Aboutwindow):
        Aboutwindow.setWindowTitle(_translate("Aboutwindow", "About", None))
        self.groupBox.setTitle(_translate("Aboutwindow", "About:", None))
        self.label.setText(_translate("Aboutwindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">LaTeX to Speech</span></p><p>LaTeX to Speech is a free and open source utility tool used for converting the (La)Tex </p>\n"
"<p>equations to its equivalent Speech form.</p>\n"
"</body></html>", None))
        self.label_2.setPixmap(QtGui.QPixmap("win_icon.png"))
#import icon_rc
