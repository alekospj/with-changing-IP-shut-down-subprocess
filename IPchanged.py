# -*- coding: utf-8 -*-

#ALEKOSPJ
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

#alekospj 05/12/18

from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
import urllib.request, time;
import win32com.shell.shell as shell
import time
import subprocess
from multiprocessing import Process
import socket 
from threading import Thread

ASADMIN = 'asadmin'


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)                         
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        
        '''--- Console ---'''
        self.textBrowser_consola = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_consola.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textBrowser_consola.setObjectName("textBrowser_consola")
        self.verticalLayout.addWidget(self.textBrowser_consola)
        
        '''---Button Start---'''
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_start_shield = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_shield.setObjectName("pushButton_start_shield")
        
        self.p = None
        self.textBrowser_consola.append('*** Started! ***')
        
        '''Thread for the button'''
        def run_thrd_start():
            try:
                thrd_start = Thread(target = self.shield_start())
                thrd_start.start()
                thrd_start.join()
            except:
                print('Lagare!')
        
        stsh = self.pushButton_start_shield        
        stsh.clicked.connect(run_thrd_start)
        
        
        
        '''---Close---'''
        self.verticalLayout.addWidget(self.pushButton_start_shield)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        
        
        '''Thread for the stop'''        
        def run_thrd_stop():
            thrd_stop = Thread(target = self.close_app())
            thrd_stop.start()
            thrd_stop.join()
        
        clsb = self.pushButton_close
        clsb.clicked.connect(run_thrd_stop)
        
        
        self.verticalLayout.addWidget(self.pushButton_close)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.main_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        self.menuShield = QtWidgets.QMenu(self.menubar)
        self.menuShield.setObjectName("menuShield")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuShield.menuAction())

        self.retranslateUi(MainWindow)       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start_shield.setText(_translate("MainWindow", "Start Shield"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.menuShield.setTitle(_translate("MainWindow", "Shield"))
    
    def shield_start(self):
        
        def actul_rn():
            def open_program(path_name):
                return subprocess.Popen(path_name)
             
            self.p = open_program(r"C:\Users\xoxlios\Desktop\uTorrent\uTorrent.exe") 

            ip = socket.gethostbyname(socket.gethostname())
            
            while True:
                if ip == socket.gethostbyname(socket.gethostname()):
                    print('Conected at:',ip)
                    self.textBrowser_consola.append('Conected at:'+str(ip))
                    time.sleep(5)
                else:
                    self.textBrowser_consola.append('\nConection Lost!\n')
                    self.p.terminate()
                    break
               
        thrd_scrn = Thread(target = actul_rn())
        thrd_scrn.start()
        thrd_scrn.join()
        
        
    def close_app (self):
        print('Bonne Nuit!!!')
        self.p.terminate()
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

