# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# install requirements and run win.py


from PyQt5 import QtCore, QtGui, QtWidgets
from win32com.client import Dispatch
from win2 import Ui_MainWindow_2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 600))
        MainWindow.setStyleSheet("\n"
"background-color:#e0e0e0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(104, 222, 321, 41))
        self.label.setStyleSheet("font: 75 23pt \"Tahoma\";\n"
"border:none;\n"
"background:none;")
        self.label.setObjectName("label")
        self.nxt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.nxt_1.setGeometry(QtCore.QRect(181, 422, 91, 31))
        self.nxt_1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3362CC, stop:1 rgba(18, 131, 255, 1));\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;")
        self.nxt_1.setObjectName("nxt_1")
        self.txt = QtWidgets.QLineEdit(self.centralwidget)
        self.txt.setGeometry(QtCore.QRect(142, 379, 181, 31))
        self.txt.setStyleSheet("border: 1px solid #b3caff;\n"
"border-radius:8px;\n"
"background:none;\n"
"font:  \"Tahoma\";")
        self.txt.setObjectName("txt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(72, 60, 801, 81))
        self.label_3.setStyleSheet("font: 75 30pt \"Tahoma\";\n"
"border:none;\n"
"background:none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(104, 307, 221, 31))
        self.label_4.setStyleSheet("font: 10.5pt \"Tahoma\";\n"
"border:none;\n"
"background:none;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(101, 250, 321, 61))
        self.label_5.setStyleSheet("background:none;\n"
"font: 75 23pt \"Tahoma\";\n"
"border:none;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(107, 379, 31, 31))
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("src/login.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(417, 148, 391, 371))
        self.label_6.setStyleSheet("background:none;")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("src/Health.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.nxt_1.clicked.connect(self.nxt)

    def nxt(self):
        txt = self.txt.text()
        readn("Hello " + txt)
        self.window = QtWidgets.QMainWindow()
        self.window_ui = Ui_MainWindow_2()
        self.window_ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()
        QtWidgets.qApp.processEvents()  
        readn("Select the Symtoms you are suffering from")
        readn(" if less select those again")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "We care"))
        self.nxt_1.setText(_translate("MainWindow", "Next"))
        self.txt.setPlaceholderText(_translate("MainWindow", " Please Enter Your Name"))
        self.label_3.setText(_translate("MainWindow", "Welcome to Smart Doctor"))
        self.label_4.setText(_translate("MainWindow", "Get a Free checkup Today!"))
        self.label_5.setText(_translate("MainWindow", "about Your Heath"))
import src
def readn(nstr):
        speak=Dispatch(("SAPI.SpVoice"))
        speak.Speak(nstr)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    QtWidgets.qApp.processEvents()
    readn("Welcome to Smart Doctor")
    readn("Please Enter Your Name")
    sys.exit(app.exec_())
