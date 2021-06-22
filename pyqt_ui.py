# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
import sys
import pyaudio
import time


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(490, 260))
        Form.setMaximumSize(QtCore.QSize(490, 260))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 140, 121, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 527, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(400, 30))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 421, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 75, 109, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(2, 13))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(54, 105, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMaximumSize(QtCore.QSize(60, 20))
        self.comboBox_2.setBaseSize(QtCore.QSize(60, 20))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 251, 80))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(0, 26, 161, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 16, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(0)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2.setEnabled(False)

        self.retranslateUi(Form)
        
        self.label_4.windowIconTextChanged['QString'].connect(self.label_3.update)
        QtCore.QMetaObject.connectSlotsByName(Form)
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Speech Censor v0.1"))
        self.pushButton.setText(_translate("Form", "Обновить фильтр"))
        self.pushButton_2.setText(_translate("Form", "▶"))
        self.label_5.setText(_translate("Form", "Длительность потока: 0:00 "))
        self.label.setText(_translate("Form", "Источник аудиопотока:"))
        self.label_2.setText(_translate("Form", "Язык распознавания:"))
        self.groupBox.setTitle(_translate("Form", "Состояние"))
        self.label_4.setText(_translate("Form", "Выберите источник"))
        self.label_3.setText(_translate("Form", "❌"))

 
class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data = "" #tmp
        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.ui.pushButton.clicked.connect(self.openFileNameDialog)
        self.ui.comboBox.addItem("--Выберите источник ввода--")
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            if (p.get_device_info_by_index(i).get('maxInputChannels')) > 0:
                self.ui.comboBox.addItem(p.get_device_info_by_index(i).get('name'))
                
        self.ui.comboBox_2.addItem("RU-ru")
        self.start_flag = False
        self.ui.pushButton_2.clicked.connect(self.mainActivity)
        self.ui.comboBox.currentIndexChanged['int'].connect(self.audioInputChanged)
   
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Открыть файл", "","All Files (*.*)", options=options)
        if fileName:            
            f = open(fileName, 'r',encoding="utf-8")		
            with f:
                data1 = f.read()
            self.data = data1.split(" ")
            if len(self.data)> 0 and self.ui.comboBox.currentIndex() != 0:
                self.ui.label_4.setText("Готово к работе")
                self.ui.label_3.setText("✔️")
                self.ui.pushButton_2.setEnabled(True)
            else:
                self.ui.label_4.setText("Обновите фильтр")
                self.ui.pushButton_2.setEnabled(False)
                self.ui.label_3.setText("❌")
    
    def onTimeout(self):
        cur_time = time.gmtime(time.time()-self.start_time)
        self.ui.label_5.setText('Длительность потока: {0}:{1}:{2}'.format(cur_time.tm_hour,cur_time.tm_min,cur_time.tm_sec))
        self.ui.label_5.adjustSize()   

    def mainActivity(self):
        self.start_flag = not self.start_flag
        if self.start_flag:
            self.start_time = time.time()
            self.ui.pushButton_2.setText("■")
            self.setWindowTitle("🔴Speech Censor v0.1")
            self.ui.comboBox.setEnabled(False)
            self.ui.comboBox_2.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            self.ui.label_4.setText("В эфире")
            self.ui.label_3.setText("🔴")
            self.timer.start(1000)
        else:
            self.ui.pushButton_2.setText("▶")
            self.ui.comboBox.setEnabled(True)
            self.ui.comboBox_2.setEnabled(True)
            self.ui.pushButton.setEnabled(True)
            self.setWindowTitle("Speech Censor v0.1")
            self.ui.label_4.setText("Готово к работе")
            self.ui.label_3.setText("✔️")
            self.timer.stop()
        
    def audioInputChanged(self):
        if self.ui.comboBox.currentIndex() != 0 and len(self.data)> 0:
            self.ui.label_4.setText("Готово к работе")
            self.ui.label_3.setText("✔️")
            self.ui.pushButton_2.setEnabled(True)
        elif self.ui.comboBox.currentIndex() != 0:
            self.ui.label_4.setText("Обновите фильтр")
            self.ui.pushButton_2.setEnabled(False)
            self.ui.label_3.setText("❌")
        else:
            self.ui.label_4.setText("Выберите источник")
            self.ui.pushButton_2.setEnabled(False)
            self.ui.label_3.setText("❌")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())



