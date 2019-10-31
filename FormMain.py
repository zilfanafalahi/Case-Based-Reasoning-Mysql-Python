from PyQt5 import QtCore,QtGui,QtWidgets
Super=super
Benar=True
Salah=False
Application=QtWidgets.QApplication
Action=QtWidgets.QAction
StatusBar=QtWidgets.QStatusBar
Menu=QtWidgets.QMenu
MenuBar=QtWidgets.QMenuBar
Widget=QtWidgets.QWidget
MainWindow=QtWidgets.QMainWindow
CoreApplication=QtCore.QCoreApplication
MetaObject=QtCore.QMetaObject
Rect=QtCore.QRect

import sys
Exit=sys.exit
argumen=sys.argv

import pymysql
from Konsultasi import*

host='127.0.0.1'
user='root'
password=''
db='db_cbr_python'
akses='admin'

class window(MainWindow):
 def __init__(main):
  super().__init__()
  
  main.program(main)

 def program(main,window):
  window.setObjectName("FormMain")
  window.resize(800,520)
  main.centralwidget=Widget(window)
  main.centralwidget.setObjectName("centralwidget")

  window.setCentralWidget(main.centralwidget)
  main.setCentralWidget=MenuBar(window)
  main.setCentralWidget.setGeometry(Rect(0,0,800,21))
  main.setCentralWidget.setObjectName("setCentralWidget")

  main.tKeluar=Menu(main.setCentralWidget)
  main.tKeluar.setObjectName("tKeluar")
  main.tPakar=Menu(main.setCentralWidget)
  main.tPakar.setObjectName("tPakar")

  window.setMenuBar(main.setCentralWidget)
  main.setMenuBar=StatusBar(window)
  main.setMenuBar.setObjectName("setMenuBar")

  window.setStatusBar(main.setMenuBar)
  main.keluar=Action(window)
  main.keluar.setObjectName("keluar")
  main.konsultasiCBR=Action(window)
  main.konsultasiCBR.setObjectName("konsultasiCBR")
  main.tKeluar.addAction(main.keluar)
  main.tPakar.addAction(main.konsultasiCBR)
  main.setCentralWidget.addAction(main.tPakar.menuAction())
  main.setCentralWidget.addAction(main.tKeluar.menuAction())

  main.konsultasiCBR.triggered.connect(main.Benar)
  main.keluar.triggered.connect(main.quit)
  main.tampilan(window)

  MetaObject.connectSlotsByName(window)

 def tampilan(main,window):
  bagian=CoreApplication.translate
  window.setWindowTitle(bagian("FormMain","Sistem Pakar Metode Case Based Reasoning (CBR)"))

  main.tPakar.setTitle(bagian("FormMain","Sistem Pakar"))
  main.konsultasiCBR.setText(bagian("FormMain", "Konsultasi Sistem Pakar CBR"))

  main.tKeluar.setTitle(bagian("FormMain","Keluar"))
  main.keluar.setText(bagian("FormMain", "Keluar"))

  main.show()

 def Benar(main):
  main.Konsultasi=Konsultasi()
  main.Konsultasi.show()

 def quit(main):
  main.close()

if __name__=='__main__':
 selesai=Application(argumen)
 ex=window()
 Exit(selesai.exec())
