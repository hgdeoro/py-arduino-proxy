# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Main.ui'
#
# Created: Tue May  3 22:35:48 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 661, 461))
        self.frame.setStyleSheet("background-image: url(:/images/Arduino-Uno.png);\n"
"background-position: top left;\n"
"background-repeat: none;\n"
"")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pinEnabled13 = QtGui.QCheckBox(self.frame)
        self.pinEnabled13.setGeometry(QtCore.QRect(200, 70, 21, 21))
        self.pinEnabled13.setText("")
        self.pinEnabled13.setObjectName("pinEnabled13")
        self.pinEnabled12 = QtGui.QCheckBox(self.frame)
        self.pinEnabled12.setGeometry(QtCore.QRect(240, 70, 16, 21))
        self.pinEnabled12.setText("")
        self.pinEnabled12.setObjectName("pinEnabled12")
        self.pinEnabled11 = QtGui.QCheckBox(self.frame)
        self.pinEnabled11.setGeometry(QtCore.QRect(280, 70, 16, 21))
        self.pinEnabled11.setText("")
        self.pinEnabled11.setObjectName("pinEnabled11")
        self.pinEnabled10 = QtGui.QCheckBox(self.frame)
        self.pinEnabled10.setGeometry(QtCore.QRect(320, 70, 16, 21))
        self.pinEnabled10.setText("")
        self.pinEnabled10.setObjectName("pinEnabled10")
        self.pinEnabled9 = QtGui.QCheckBox(self.frame)
        self.pinEnabled9.setGeometry(QtCore.QRect(360, 70, 16, 21))
        self.pinEnabled9.setText("")
        self.pinEnabled9.setObjectName("pinEnabled9")
        self.pinEnabled8 = QtGui.QCheckBox(self.frame)
        self.pinEnabled8.setGeometry(QtCore.QRect(400, 70, 16, 21))
        self.pinEnabled8.setText("")
        self.pinEnabled8.setObjectName("pinEnabled8")
        self.pinMode13 = QtGui.QPushButton(self.frame)
        self.pinMode13.setGeometry(QtCore.QRect(200, 90, 16, 27))
        self.pinMode13.setAutoFillBackground(False)
        self.pinMode13.setCheckable(False)
        self.pinMode13.setChecked(False)
        self.pinMode13.setDefault(False)
        self.pinMode13.setFlat(False)
        self.pinMode13.setObjectName("pinMode13")
        self.pinMode12 = QtGui.QPushButton(self.frame)
        self.pinMode12.setGeometry(QtCore.QRect(240, 90, 16, 27))
        self.pinMode12.setObjectName("pinMode12")
        self.pinMode11 = QtGui.QPushButton(self.frame)
        self.pinMode11.setGeometry(QtCore.QRect(280, 90, 16, 27))
        self.pinMode11.setObjectName("pinMode11")
        self.pinMode10 = QtGui.QPushButton(self.frame)
        self.pinMode10.setGeometry(QtCore.QRect(320, 90, 16, 27))
        self.pinMode10.setObjectName("pinMode10")
        self.pinMode9 = QtGui.QPushButton(self.frame)
        self.pinMode9.setGeometry(QtCore.QRect(360, 90, 16, 27))
        self.pinMode9.setObjectName("pinMode9")
        self.pinMode8 = QtGui.QPushButton(self.frame)
        self.pinMode8.setGeometry(QtCore.QRect(400, 90, 16, 27))
        self.pinMode8.setObjectName("pinMode8")
        self.pinValue11 = QtGui.QSlider(self.frame)
        self.pinValue11.setGeometry(QtCore.QRect(280, 180, 29, 91))
        self.pinValue11.setMaximum(255)
        self.pinValue11.setOrientation(QtCore.Qt.Vertical)
        self.pinValue11.setObjectName("pinValue11")
        self.pinValue10 = QtGui.QSlider(self.frame)
        self.pinValue10.setGeometry(QtCore.QRect(320, 180, 29, 91))
        self.pinValue10.setMaximum(255)
        self.pinValue10.setOrientation(QtCore.Qt.Vertical)
        self.pinValue10.setObjectName("pinValue10")
        self.pinValue9 = QtGui.QSlider(self.frame)
        self.pinValue9.setGeometry(QtCore.QRect(360, 180, 29, 91))
        self.pinValue9.setMaximum(255)
        self.pinValue9.setOrientation(QtCore.Qt.Vertical)
        self.pinValue9.setObjectName("pinValue9")
        self.label13 = QtGui.QLabel(self.frame)
        self.label13.setGeometry(QtCore.QRect(180, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label13.setFont(font)
        self.label13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label13.setObjectName("label13")
        self.label12 = QtGui.QLabel(self.frame)
        self.label12.setGeometry(QtCore.QRect(220, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label12.setFont(font)
        self.label12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label12.setObjectName("label12")
        self.label11 = QtGui.QLabel(self.frame)
        self.label11.setGeometry(QtCore.QRect(260, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label11.setFont(font)
        self.label11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label11.setObjectName("label11")
        self.label10 = QtGui.QLabel(self.frame)
        self.label10.setGeometry(QtCore.QRect(300, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label10.setObjectName("label10")
        self.label9 = QtGui.QLabel(self.frame)
        self.label9.setGeometry(QtCore.QRect(340, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label9.setObjectName("label9")
        self.label8 = QtGui.QLabel(self.frame)
        self.label8.setGeometry(QtCore.QRect(380, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label8.setObjectName("label8")
        self.lcdPWM11 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM11.setGeometry(QtCore.QRect(260, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM11.setFont(font)
        self.lcdPWM11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdPWM11.setNumDigits(4)
        self.lcdPWM11.setObjectName("lcdPWM11")
        self.lcdPWM10 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM10.setGeometry(QtCore.QRect(300, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM10.setFont(font)
        self.lcdPWM10.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdPWM10.setNumDigits(4)
        self.lcdPWM10.setObjectName("lcdPWM10")
        self.lcdPWM9 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM9.setGeometry(QtCore.QRect(340, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM9.setFont(font)
        self.lcdPWM9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdPWM9.setNumDigits(4)
        self.lcdPWM9.setObjectName("lcdPWM9")
        self.led13 = QtGui.QLabel(self.frame)
        self.led13.setGeometry(QtCore.QRect(200, 30, 21, 21))
        self.led13.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led13.setText("")
        self.led13.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led13.setObjectName("led13")
        self.led12 = QtGui.QLabel(self.frame)
        self.led12.setGeometry(QtCore.QRect(240, 30, 21, 21))
        self.led12.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led12.setText("")
        self.led12.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led12.setObjectName("led12")
        self.led11 = QtGui.QLabel(self.frame)
        self.led11.setGeometry(QtCore.QRect(280, 30, 21, 21))
        self.led11.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led11.setText("")
        self.led11.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led11.setObjectName("led11")
        self.led10 = QtGui.QLabel(self.frame)
        self.led10.setGeometry(QtCore.QRect(320, 30, 21, 21))
        self.led10.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led10.setText("")
        self.led10.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led10.setObjectName("led10")
        self.led9 = QtGui.QLabel(self.frame)
        self.led9.setGeometry(QtCore.QRect(360, 30, 21, 21))
        self.led9.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led9.setText("")
        self.led9.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led9.setObjectName("led9")
        self.led8 = QtGui.QLabel(self.frame)
        self.led8.setGeometry(QtCore.QRect(400, 30, 21, 21))
        self.led8.setStyleSheet("background-image: none;\n"
"background: none;\n"
"")
        self.led8.setText("")
        self.led8.setPixmap(QtGui.QPixmap(":/images/led-off.png"))
        self.led8.setObjectName("led8")
        self.dw13_l = QtGui.QPushButton(self.frame)
        self.dw13_l.setGeometry(QtCore.QRect(200, 150, 16, 21))
        self.dw13_l.setObjectName("dw13_l")
        self.dw12_l = QtGui.QPushButton(self.frame)
        self.dw12_l.setGeometry(QtCore.QRect(240, 150, 16, 21))
        self.dw12_l.setObjectName("dw12_l")
        self.dw11_l = QtGui.QPushButton(self.frame)
        self.dw11_l.setGeometry(QtCore.QRect(280, 150, 16, 21))
        self.dw11_l.setObjectName("dw11_l")
        self.dw10_l = QtGui.QPushButton(self.frame)
        self.dw10_l.setGeometry(QtCore.QRect(320, 150, 16, 21))
        self.dw10_l.setObjectName("dw10_l")
        self.dw9_l = QtGui.QPushButton(self.frame)
        self.dw9_l.setGeometry(QtCore.QRect(360, 150, 16, 21))
        self.dw9_l.setObjectName("dw9_l")
        self.dw8_l = QtGui.QPushButton(self.frame)
        self.dw8_l.setGeometry(QtCore.QRect(400, 150, 16, 21))
        self.dw8_l.setObjectName("dw8_l")
        self.label_enabled = QtGui.QLabel(self.frame)
        self.label_enabled.setGeometry(QtCore.QRect(60, 70, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_enabled.setFont(font)
        self.label_enabled.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enabled.setObjectName("label_enabled")
        self.label_pinMode = QtGui.QLabel(self.frame)
        self.label_pinMode.setGeometry(QtCore.QRect(60, 100, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_pinMode.setFont(font)
        self.label_pinMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pinMode.setObjectName("label_pinMode")
        self.label_digitalWrite = QtGui.QLabel(self.frame)
        self.label_digitalWrite.setGeometry(QtCore.QRect(60, 130, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_digitalWrite.setFont(font)
        self.label_digitalWrite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_digitalWrite.setObjectName("label_digitalWrite")
        self.label_digitalRead = QtGui.QLabel(self.frame)
        self.label_digitalRead.setGeometry(QtCore.QRect(60, 30, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_digitalRead.setFont(font)
        self.label_digitalRead.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_digitalRead.setObjectName("label_digitalRead")
        self.label_analogWrite = QtGui.QLabel(self.frame)
        self.label_analogWrite.setGeometry(QtCore.QRect(60, 180, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_analogWrite.setFont(font)
        self.label_analogWrite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_analogWrite.setObjectName("label_analogWrite")
        self.dw13_h = QtGui.QPushButton(self.frame)
        self.dw13_h.setGeometry(QtCore.QRect(200, 130, 16, 21))
        self.dw13_h.setObjectName("dw13_h")
        self.dw12_h = QtGui.QPushButton(self.frame)
        self.dw12_h.setGeometry(QtCore.QRect(240, 130, 16, 21))
        self.dw12_h.setObjectName("dw12_h")
        self.dw11_h = QtGui.QPushButton(self.frame)
        self.dw11_h.setGeometry(QtCore.QRect(280, 130, 16, 21))
        self.dw11_h.setObjectName("dw11_h")
        self.dw10_h = QtGui.QPushButton(self.frame)
        self.dw10_h.setGeometry(QtCore.QRect(320, 130, 16, 21))
        self.dw10_h.setObjectName("dw10_h")
        self.dw9_h = QtGui.QPushButton(self.frame)
        self.dw9_h.setGeometry(QtCore.QRect(360, 130, 16, 21))
        self.dw9_h.setObjectName("dw9_h")
        self.dw8_h = QtGui.QPushButton(self.frame)
        self.dw8_h.setGeometry(QtCore.QRect(400, 130, 16, 21))
        self.dw8_h.setObjectName("dw8_h")
        self.pushButtonUpdate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(20, 490, 85, 27))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.checkboxAutoUpdate = QtGui.QCheckBox(self.centralwidget)
        self.checkboxAutoUpdate.setGeometry(QtCore.QRect(120, 490, 141, 21))
        self.checkboxAutoUpdate.setObjectName("checkboxAutoUpdate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pinValue11, QtCore.SIGNAL("valueChanged(int)"), self.lcdPWM11.display)
        QtCore.QObject.connect(self.pinValue10, QtCore.SIGNAL("valueChanged(int)"), self.lcdPWM10.display)
        QtCore.QObject.connect(self.pinValue9, QtCore.SIGNAL("valueChanged(int)"), self.lcdPWM9.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled13.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled12.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled11.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled10.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled9.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled8.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode13.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode13.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode12.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode12.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode11.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode11.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode10.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode10.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode9.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode9.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode8.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode8.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue11.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue10.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue9.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label13.setText(QtGui.QApplication.translate("MainWindow", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.label12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.label11.setText(QtGui.QApplication.translate("MainWindow", "~11", None, QtGui.QApplication.UnicodeUTF8))
        self.label10.setText(QtGui.QApplication.translate("MainWindow", "~10", None, QtGui.QApplication.UnicodeUTF8))
        self.label9.setText(QtGui.QApplication.translate("MainWindow", "~9", None, QtGui.QApplication.UnicodeUTF8))
        self.label8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.label_enabled.setText(QtGui.QApplication.translate("MainWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pinMode.setText(QtGui.QApplication.translate("MainWindow", "pinMode()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_digitalWrite.setText(QtGui.QApplication.translate("MainWindow", "digitalWrite()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_digitalRead.setText(QtGui.QApplication.translate("MainWindow", "digitalRead()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_analogWrite.setText(QtGui.QApplication.translate("MainWindow", "PWM ~ analogWrite()", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxAutoUpdate.setText(QtGui.QApplication.translate("MainWindow", "Auto update", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
