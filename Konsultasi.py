from PyQt5 import QtCore,QtGui,QtWidgets
Super=super
String=str
Print=print
Lenght=len
Max=max
Range=range
Round=round

Application=QtWidgets.QApplication
TableWidgetItem=QtWidgets.QTableWidgetItem
AbstractItemView=QtWidgets.QAbstractItemView
ListWidget=QtWidgets.QListWidget
Label=QtWidgets.QLabel
PushButton=QtWidgets.QPushButton
TableWidget=QtWidgets.QTableWidget
MainWindow=QtWidgets.QMainWindow
CoreApplication=QtCore.QCoreApplication
MetaObject=QtCore.QMetaObject
Rect=QtCore.QRect

import sys
Exit=sys.exit
argumen=sys.argv

import pymysql
con=pymysql.connect

import FormMain
db='db_cbr_python'
password=''
user='root'
host='127.0.0.1'

class Konsultasi(MainWindow):
 def __init__(main):
  super().__init__()
  main.program(main)

 def program(main,Konsultasi):
  Konsultasi.setObjectName("Konsultasi")
  Konsultasi.resize(872,520)
  main.tableHasilAkhir=TableWidget(Konsultasi)
  main.tableHasilAkhir.setGeometry(Rect(20,270,401,201))
  main.tableHasilAkhir.setObjectName("tableHasilAkhir")
  main.tableHasilAkhir.setColumnCount(0)
  main.tableHasilAkhir.setRowCount(0)
  main.buttonPerhitungan=PushButton(Konsultasi)
  main.buttonPerhitungan.setGeometry(Rect(350,210,75,23))
  main.buttonPerhitungan.setObjectName("buttonPerhitungan")
  main.label=Label(Konsultasi)
  main.label.setGeometry(Rect(20,10,161,16))
  main.label.setObjectName("label")
  main.label_2=Label(Konsultasi)
  main.label_2.setGeometry(Rect(20,250,161,16))
  main.label_2.setObjectName("label_2")
  main.tablePerhitungan=TableWidget(Konsultasi)
  main.tablePerhitungan.setGeometry(Rect(450,270,401,201))
  main.tablePerhitungan.setObjectName("tablePerhitungan")
  main.tablePerhitungan.setColumnCount(0)
  main.tablePerhitungan.setRowCount(0)
  main.label_6=Label(Konsultasi)
  main.label_6.setGeometry(Rect(450,250,161,16))
  main.label_6.setObjectName("label_6")
  main.label_8=Label(Konsultasi)
  main.label_8.setGeometry(Rect(450,10,161,16))
  main.label_8.setObjectName("label_8")
  main.tableBasisKasus=TableWidget(Konsultasi)
  main.tableBasisKasus.setGeometry(Rect(450,30,401,211))
  main.tableBasisKasus.setObjectName("tableBasisKasus")
  main.tableBasisKasus.setColumnCount(0)
  main.tableBasisKasus.setRowCount(0)
  main.listGejala=ListWidget(Konsultasi)
  main.listGejala.setGeometry(Rect(20,30,401,171))
  main.listGejala.setSelectionMode(AbstractItemView.MultiSelection)
  main.listGejala.setObjectName("listGejala")
  main.buttonProses=PushButton(Konsultasi)
  main.buttonProses.setGeometry(Rect(20,210,75,23))
  main.buttonProses.setObjectName("buttonProses")
  main.labelHasil=Label(Konsultasi)
  main.labelHasil.setGeometry(Rect(20,480,401,31))
  main.labelHasil.setObjectName("labelHasil")
  main.label.raise_()
  main.tableHasilAkhir.raise_()
  main.buttonPerhitungan.raise_()
  main.label_2.raise_()
  main.tablePerhitungan.raise_()
  main.label_6.raise_()
  main.label_8.raise_()
  main.tableBasisKasus.raise_()
  main.listGejala.raise_()
  main.buttonProses.raise_()
  main.labelHasil.raise_()
  main.tampilan(Konsultasi)
  main.buttonProses.clicked.connect(main.perhitungan)
  main.buttonPerhitungan.clicked.connect(main.proses)
  MetaObject.connectSlotsByName(Konsultasi)
     
 def tampilan(main,Konsultasi):
  bagian=CoreApplication.translate
  Konsultasi.setWindowTitle(bagian("FormKonsultasiCBR","Sistem Pakar Metode Case Based Reasoning (CBR)"))
  main.buttonPerhitungan.setText(bagian("FormKonsultasiCBR","Perhitungan"))
  main.label.setText(bagian("FormKonsultasiCBR","Pilih Gejala"))
  main.label_2.setText(bagian("FormKonsultasiCBR","<html><head/><body><p>Hasil Akhir</p></body></html>"))
  main.label_6.setText(bagian("FormKonsultasiCBR","Perhitungan"))
  main.label_8.setText(bagian("FormKonsultasiCBR","Basis Kasus"))
  main.buttonProses.setText(bagian("FormKonsultasiCBR","Proses"))
  main.labelHasil.setText(bagian("FormKonsultasiCBR","-"))
  main.pilihGejala()
  main.basisKasus()
  Konsultasi.resize(445,250)
  main.show()
     
 def pilihGejala(main):
  data=con(host,user,password,db)
  query=data.cursor()
  
  sql="SELECT * FROM gejala"
  main.list_id_gejala=[]
  main.listGejala.clear()
  try:
   query.execute(sql)
   suc=query.fetchall()
   i=0
   for indek in suc:
    main.list_id_gejala.append(String(indek[0]))
    main.listGejala.addItem(indek[1])
    i=i+1
  except:
   Print("Error: unable to fetch data")
  data.close()
     
 def basisKasus(main):
  data=con(host,user,password,db)
  query=data.cursor()
  sql="SELECT basis_kasus.*, penyakit.nama_penyakit, gejala.nama_gejala FROM basis_kasus LEFT JOIN penyakit ON penyakit.id_penyakit = basis_kasus.id_penyakit LEFT JOIN gejala ON basis_kasus.id_gejala = gejala.id_gejala"
  main.list_no_basis_kasus=[]
  main.list_id_penyakit_basis_kasus=[]
  main.list_id_gejala_basis_kasus=[]
  try:
   query.execute(sql)
   suc=query.fetchall()
   main.tableBasisKasus.setColumnCount(3)
   main.tableBasisKasus.setRowCount(Lenght(suc)) 
   main.tableBasisKasus.setHorizontalHeaderLabels(('No Basis Kasus','Penyakit','Gejala'))
   i=0
   main.vheader=[]
   for indek in suc:
    main.vheader.append('')
    main.list_no_basis_kasus.append(String(indek[0]))
    main.list_id_penyakit_basis_kasus.append(String(indek[1]))
    main.list_id_gejala_basis_kasus.append(String(indek[2]))
    main.tableBasisKasus.setItem(i,0,TableWidgetItem(String(indek[1])))
    main.tableBasisKasus.setItem(i,1,TableWidgetItem(indek[4]))
    main.tableBasisKasus.setItem(i,2,TableWidgetItem(indek[5]))
    i=i+1
   main.id_basis_kasus=""
   main.tableBasisKasus.setVerticalHeaderLabels(main.vheader)
  except:
   Print("Error: unable to fetch data")
  data.close()
 
 def perhitungan(main):
  main.list_id_gejala_terpilih=[]
  main.list_nama_gejala_terpilih=[]
  suf=main.listGejala.selectedIndexes()
  suP=main.listGejala.selectedItems()
  i=0
  for indek in suf:
   main.list_id_gejala_terpilih.append(String(main.list_id_gejala[suf[i].row()]))
   main.list_nama_gejala_terpilih.append(suP[i].text())
   i=i+1
  data=con(host,user,password,db)
  query=data.cursor()
  sql="SELECT basis_kasus.*, penyakit.nama_penyakit, gejala.nama_gejala FROM basis_kasus LEFT JOIN penyakit ON penyakit.id_penyakit = basis_kasus.id_penyakit LEFT JOIN gejala ON basis_kasus.id_gejala = gejala.id_gejala ORDER BY no_kasus ASC, basis_kasus.id_penyakit ASC, basis_kasus.id_gejala"
  main.list_no_basis_kasus=[]
  main.list_id_penyakit_basis_kasus=[]
  main.list_nama_penyakit_basis_kasus=[]
  main.list_jml_gejala_cocok=[]
  main.list_jml_gejala_kasus=[]
  main.list_jml_gejala_dipilih=[]
  main.list_pembagi=[]
  main.list_nilai_hasil=[]
  sub=""
  try:
   query.execute(sql)
   suc=query.fetchall()
   i=-1
   for indek in suc:
    if(sub!=String(indek[1])):
     i=i+1
     main.list_no_basis_kasus.append(String(indek[1]))
     main.list_id_penyakit_basis_kasus.append(indek[2])
     main.list_nama_penyakit_basis_kasus.append(String(indek[4]))
     main.list_jml_gejala_cocok.append(0)
     main.list_jml_gejala_kasus.append(0)
     main.list_jml_gejala_dipilih.append(Lenght(main.list_id_gejala_terpilih))
     main.list_pembagi.append(0)
     main.list_nilai_hasil.append(0)
    main.list_jml_gejala_kasus[i]=main.list_jml_gejala_kasus[i]+1
    for suy in main.list_id_gejala_terpilih:
     if(suy==String(indek[3])):
      main.list_jml_gejala_cocok[i]=main.list_jml_gejala_cocok[i]+1
    sub=String(indek[1])
   i=0
   for indek in main.list_no_basis_kasus:
    main.list_pembagi[i]=Max(main.list_jml_gejala_kasus[i],main.list_jml_gejala_dipilih[i]);
    if(main.list_pembagi[i]>0):
     main.list_nilai_hasil[i]=main.list_jml_gejala_cocok[i]/main.list_pembagi[i]
    i=i+1
  except:
   Print("Error: unable to fetch data")
  data.close()
  main.tablePerhitungan.setColumnCount(6)
  main.tablePerhitungan.setRowCount(Lenght(main.list_no_basis_kasus))
  main.tablePerhitungan.setHorizontalHeaderLabels(('Kasus','Jml Gejala Cocok','Jml Gejala Kasus','Jml Gejala Dipilih','Pembagi','Nilai Hasil'))
  main.vheader=[]
  i=0
  for indek in main.list_no_basis_kasus:
   main.vheader.append('')
   main.tablePerhitungan.setItem(i,0,TableWidgetItem(main.list_no_basis_kasus[i]))
   main.tablePerhitungan.setItem(i,1,TableWidgetItem(String(main.list_jml_gejala_cocok[i])))
   main.tablePerhitungan.setItem(i,2,TableWidgetItem(String(main.list_jml_gejala_kasus[i])))
   main.tablePerhitungan.setItem(i,3,TableWidgetItem(String(main.list_jml_gejala_dipilih[i])))
   main.tablePerhitungan.setItem(i,4,TableWidgetItem(String(main.list_pembagi[i])))
   main.tablePerhitungan.setItem(i,5,TableWidgetItem(String(main.list_nilai_hasil[i])))
   i=i+1
  main.tablePerhitungan.setVerticalHeaderLabels(main.vheader)
  main.rangking_no_basis_kasus=[]
  main.rangking_id_penyakit_basis_kasus=[]
  main.rangking_nama_penyakit_basis_kasus=[]
  main.rangking_nilai_hasil=[]
  i=0
  for indek in main.list_no_basis_kasus:
   main.rangking_no_basis_kasus.append(main.list_no_basis_kasus[i])
   main.rangking_id_penyakit_basis_kasus.append(main.list_id_penyakit_basis_kasus[i])
   main.rangking_nama_penyakit_basis_kasus.append(main.list_nama_penyakit_basis_kasus[i])
   main.rangking_nilai_hasil.append(main.list_nilai_hasil[i])
   i=i+1
  for i in Range(Lenght(main.rangking_no_basis_kasus)):
   for j in Range(Lenght(main.rangking_no_basis_kasus)):
    if j>i:
     if main.rangking_nilai_hasil[j]>main.rangking_nilai_hasil[i]:
      suH=main.rangking_no_basis_kasus[i]
      suO=main.rangking_id_penyakit_basis_kasus[i]
      suo=main.rangking_nama_penyakit_basis_kasus[i]
      sux=main.rangking_nilai_hasil[i]
      main.rangking_no_basis_kasus[i]=main.rangking_no_basis_kasus[j]
      main.rangking_id_penyakit_basis_kasus[i]=main.rangking_id_penyakit_basis_kasus[j]
      main.rangking_nama_penyakit_basis_kasus[i]=main.rangking_nama_penyakit_basis_kasus[j]
      main.rangking_nilai_hasil[i]=main.rangking_nilai_hasil[j]
      main.rangking_no_basis_kasus[j]=suH
      main.rangking_id_penyakit_basis_kasus[j]=suO
      main.rangking_nama_penyakit_basis_kasus[j]=suo
      main.rangking_nilai_hasil[j]=sux
  main.tableHasilAkhir.setColumnCount(4)
  main.tableHasilAkhir.setRowCount(Lenght(main.rangking_no_basis_kasus))
  main.tableHasilAkhir.setHorizontalHeaderLabels(('Rangking','Kasus','Penyakit','Nilai Hasil'))
  main.vheader=[]
  i=0
  for indek in main.rangking_no_basis_kasus:
   main.vheader.append('')
   main.tableHasilAkhir.setItem(i,0,TableWidgetItem(String(i+1)))
   main.tableHasilAkhir.setItem(i,1,TableWidgetItem(main.rangking_no_basis_kasus[i]))
   main.tableHasilAkhir.setItem(i,2,TableWidgetItem(main.rangking_nama_penyakit_basis_kasus[i]))
   main.tableHasilAkhir.setItem(i,3,TableWidgetItem(String(Round(main.rangking_nilai_hasil[i],2))))
   i=i+1
  main.tableHasilAkhir.setVerticalHeaderLabels(main.vheader)
  main.labelHasil.setText("Penyakit Terbesar "+String(main.rangking_id_penyakit_basis_kasus[0])+". "+main.rangking_nama_penyakit_basis_kasus[0]+" pada Kasus ke-"+String(main.rangking_no_basis_kasus[0])+" dengan Hasil Nilai "+String(Round(main.rangking_nilai_hasil[0],2)))
  main.resize(445,520)
     
 def proses(main):
  Print("Konsultasi Berhasil")
  main.resize(872,520)

if __name__=='__main__':
 selesai=Application(argumen)
 ex=Konsultasi()
 Exit(selesai.exec())

# Created by pyminifier (https://github.com/liftoff/pyminifier)
