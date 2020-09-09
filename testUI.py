# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
import pandas
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):

    def variables(self):
        self.D1_='D1'
        self.D2_='D2'
        self.D3_='D3'
        self.AVF_='AVF'
        self.AVR_='AVR'
        self.AVL_='AVL'
        self.GENRAL_='GENRAL'

    

    def setupUi(self, MainWindow):

        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")
        


        path1 = os.path.join(base_path, "imagen1.jpeg")
        path2 = os.path.join(base_path, "imagen2.jpeg")


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 747)
        #MainWindow.setStyleSheet("background-color: blue;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAbrir.setGeometry(QtCore.QRect(280, 10, 300, 32))
        self.pushButtonAbrir.setObjectName("pushButtonAbrir")
        #self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(510, 90, 151, 41))
        #self.pushButton_2.setObjectName("pushButton_2")

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(750, 230, 585, 370))
        self.graphicsView.setObjectName("graphicsView")
        
        #self.graphicsView.setBackground(background=None)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1050, 1, 300, 100))
        self.label_7.setObjectName("label_7")
        pixmap = QPixmap(path1)
        self.label_7.setPixmap(pixmap)


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(800, 1, 300, 100))
        self.label_8.setObjectName("label_8")
        pixmap = QPixmap(path2)
        self.label_8.setPixmap(pixmap)

        #Persona que creo el programa
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1000, 630, 2000, 70))
        self.label_9.setObjectName("label_9")

        #Nombre del proyecto
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1000, 595, 2000, 70))
        self.label_10.setObjectName("label_10")

        #Parametros de la persona
        self.label_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_nom.setGeometry(QtCore.QRect(800, 20, 800, 200))
        self.label_nom.setObjectName("label_nom")

        self.label_edad = QtWidgets.QLabel(self.centralwidget)
        self.label_edad.setGeometry(QtCore.QRect(800, 60, 800, 200))
        self.label_edad.setObjectName("label_edad")

        self.label_sexo = QtWidgets.QLabel(self.centralwidget)
        self.label_sexo.setGeometry(QtCore.QRect(800, 100, 800, 200))
        self.label_sexo.setObjectName("label_sexo")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 675, 841))
        self.groupBox.setObjectName("groupBox")
        
        self.graphicD1 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD1.setObjectName("graphicD1")
        self.graphicD1.setGeometry(QtCore.QRect(65, 30, 1000, 110))
        self.graphicD1.setBackground(background=None)

        self.graphicD2 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD2.setObjectName("graphicD2")
        self.graphicD2.setGeometry(QtCore.QRect(65, 130, 1000, 110))
        self.graphicD2.setBackground(background=None)

        self.graphicD3 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD3.setObjectName("graphicD3")
        self.graphicD3.setGeometry(QtCore.QRect(65, 230, 1000, 110))
        self.graphicD3.setBackground(background=None)

        self.graphicD3_2 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD3_2.setObjectName("graphicD3_2")
        self.graphicD3_2.setGeometry(QtCore.QRect(65, 330, 1000, 110))
        self.graphicD3_2.setBackground(background=None)

        self.graphicD3_3 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD3_3.setGeometry(QtCore.QRect(65, 430, 1000, 110))
        self.graphicD3_3.setObjectName("graphicD3_3")
        self.graphicD3_3.setBackground(background=None)

        self.graphicD3_4 = GraphicsLayoutWidget(self.groupBox)
        self.graphicD3_4.setObjectName("graphicD3_4")
        self.graphicD3_4.setGeometry(QtCore.QRect(65, 530, 1000, 110))
        self.graphicD3_4.setBackground(background=None)
       

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 65, 50, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 165, 50, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 265, 50, 24))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 365, 60, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 465, 60, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 565, 60, 24))
        self.label_6.setObjectName("label_6")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 22))
        self.menubar.setObjectName("menubar")
    
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.pushButtonAbrir.clicked.connect(self.mybutton_clicked)
        #self.pushButton_2.clicked.connect(self.generatedReport)

        #Cajas de texto

        self.line_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nom.resize(200, 32)
        self.line_nom.move(875, 100)

        self.line_edad = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edad.resize(200, 32)
        self.line_edad.move(875, 140)

        #self.line_sexo = QtWidgets.QLineEdit(self.centralwidget)
        #self.line_sexo.resize(200, 32)
        #self.line_sexo.move(875, 180)

        self.combo_sexo = QtWidgets.QComboBox(self.centralwidget)
        self.combo_sexo.resize(200, 32)
        self.combo_sexo.move(875, 180)
        self.combo_sexo.addItems(["None","Male","Female" ])
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        



    def mybutton_clicked(self):
        try:
            self.variables()
            #Nombre de encabezados del archivo CSV
            

            persona = {"Nombre":self.line_nom.text(),"Edad":self.line_edad.text(),"Genero":self.combo_sexo.currentText()}
            combo_textt =self.combo_sexo.currentText()
            #print(combo_textt)

            filename= QtWidgets.QFileDialog.getOpenFileName()
            df = pandas.read_csv(filename[0])

            x_max=df['x'].max()

            a=(df["x"])/4
            b= (df["x"]+x_max)/4
            c= (df["x"]+(2*x_max))/4
            d= (df["x"]+(3*x_max))/4
            r = pandas.concat([a,b,c,d])
            s= pandas.concat([df[self.D1_],df[self.D1_],df[self.D1_],df[self.D1_]])
            t= pandas.concat([df[self.D2_],df[self.D2_],df[self.D2_],df[self.D2_]])
            u= pandas.concat([df[self.D3_],df[self.D3_],df[self.D3_],df[self.D3_]])
            v= pandas.concat([df[self.AVF_],df[self.AVF_],df[self.AVF_],df[self.AVF_]])
            w= pandas.concat([df[self.AVR_],df[self.AVR_],df[self.AVR_],df[self.AVR_]])
            x= pandas.concat([df[self.AVL_],df[self.AVL_],df[self.AVL_],df[self.AVL_]])
            y= pandas.concat([df[self.GENRAL_],df[self.GENRAL_],df[self.GENRAL_],df[self.GENRAL_]])
            df = pandas.DataFrame({"x":r, "D1":s,"D2":t,"D3":u,"AVF":v,"AVR":w,"AVL":x,"GENRAL":y})




            self.d1_INTERVAL_1=df.query('x >= 3.03 & x <= 3.08')#st
            self.d1_INTERVAL_2=df.query('x >= 1.7 & x <= 1.9')#t
            self.d1_INTERVAL_3=df.query('x >= 4.2 & x <= 4.3')#p
            self.d1_INTERVAL_1_MAX= self.d1_INTERVAL_1[self.D1_].max()
            self.d1_INTERVAL_2_MAX= self.d1_INTERVAL_2[self.D1_].max()
            self.d1_INTERVAL_3_MAX= self.d1_INTERVAL_3[self.D1_].max()

            self.d2_INTERVAL_1=df.query('x >= 15.4 & x <= 15.44')#ST
            self.d2_INTERVAL_2=df.query('x >= 16.2 & x <= 16.4')#T
            self.d2_INTERVAL_3=df.query('x >= 16.6 & x <= 16.7')#P
            self.d2_INTERVAL_1_MAX= self.d2_INTERVAL_1[self.D2_].max()
            self.d2_INTERVAL_2_MAX= self.d2_INTERVAL_2[self.D2_].max()
            self.d2_INTERVAL_3_MAX= self.d2_INTERVAL_3[self.D2_].max()

            self.d3_INTERVAL_1=df.query('x >= 67.01 & x <= 67.05')#st
            self.d3_INTERVAL_2=df.query('x >= 49.85 & x <= 50')#t
            self.d3_INTERVAL_3=df.query('x >= 50.35 & x <= 50.45')#p
            self.d3_INTERVAL_1_MAX= self.d3_INTERVAL_1[self.D3_].max()
            self.d3_INTERVAL_2_MAX= self.d3_INTERVAL_2[self.D3_].max()
            self.d3_INTERVAL_3_MAX= self.d3_INTERVAL_3[self.D3_].max()

            self.avf_INTERVAL_1=df.query('x >= 111.635    & x <= 111.7')#st
            self.avf_INTERVAL_2=df.query('x >= 113.82 & x <= 114')#t
            self.avf_INTERVAL_3=df.query('x >= 153.4 & x <= 153.545')#p
            self.avf_INTERVAL_1_MAX= self.avf_INTERVAL_1[self.AVF_].max()
            self.avf_INTERVAL_2_MAX= self.avf_INTERVAL_2[self.AVF_].max()
            self.avf_INTERVAL_3_MAX= self.avf_INTERVAL_3[self.AVF_].max()

            self.avr_INTERVAL_1=df.query('x >= 99.27 & x <= 99.29')#st
            self.avr_INTERVAL_2=df.query('x >= 102.06& x <= 102.26')#t
            self.avr_INTERVAL_3=df.query('x >= 105.95 & x <= 106.09')#p
            self.avr_INTERVAL_1_MAX= self.avr_INTERVAL_1[self.AVR_].min()
            self.avr_INTERVAL_2_MAX= self.avr_INTERVAL_2[self.AVR_].min()
            self.avr_INTERVAL_3_MAX= self.avr_INTERVAL_3[self.AVR_].min()

            self.avl_INTERVAL_1=df.query('x >= 95.93 & x <= 96.12')#st
            self.avl_INTERVAL_2=df.query('x >= 104.75 & x <= 104.8')#t
            self.avl_INTERVAL_3=df.query('x >= 130.67 & x <= 130.81')#p
            self.avl_INTERVAL_1_MAX= self.avl_INTERVAL_1[self.AVL_].max()
            self.avl_INTERVAL_2_MAX= self.avl_INTERVAL_2[self.AVL_].max()
            self.avl_INTERVAL_3_MAX= self.avl_INTERVAL_3[self.AVL_].max()


            #VALORES ST Y T

            values_ST_T ={  self.D1_:
                                {
                                    "d1_INTERVAL_1_MAX":self.d1_INTERVAL_1_MAX,
                                    "d1_INTERVAL_2_MAX":self.d1_INTERVAL_2_MAX,
                                    "d1_INTERVAL_3_MAX":self.d1_INTERVAL_3_MAX
                                },
                            self.D2_:
                                {
                                    "d2_INTERVAL_1_MAX":self.d2_INTERVAL_1_MAX,
                                    "d2_INTERVAL_2_MAX":self.d2_INTERVAL_2_MAX,
                                    "d2_INTERVAL_3_MAX":self.d2_INTERVAL_3_MAX
                                },
                            self.D3_:
                                {
                                    "d3_INTERVAL_1_MAX":self.d3_INTERVAL_1_MAX,
                                    "d3_INTERVAL_2_MAX":self.d3_INTERVAL_2_MAX,
                                    "d3_INTERVAL_3_MAX":self.d3_INTERVAL_3_MAX

                                },
                            self.AVF_:
                                {
                                    "avf_INTERVAL_1_MAX":self.avf_INTERVAL_1_MAX,
                                    "avf_INTERVAL_2_MAX":self.avf_INTERVAL_2_MAX,
                                    "avf_INTERVAL_3_MAX":self.avf_INTERVAL_3_MAX

                                },
                            self.AVR_:
                                {
                                    "avr_INTERVAL_1_MAX":self.avr_INTERVAL_1_MAX,
                                    "avr_INTERVAL_2_MAX":self.avr_INTERVAL_2_MAX,
                                    "avr_INTERVAL_3_MAX":self.avr_INTERVAL_3_MAX
                                },
                            self.AVL_:
                                {
                                    "avl_INTERVAL_1_MAX":self.avl_INTERVAL_1_MAX,
                                    "avl_INTERVAL_2_MAX":self.avl_INTERVAL_2_MAX,
                                    "avl_INTERVAL_3_MAX":self.avl_INTERVAL_3_MAX,
                                }
                        }

            #Intervalo general
            limit=16
            GENER_INTERVAL=df.query('x >= 236 & x <= 243')
            print(GENER_INTERVAL)
            contPuls=0
            bandera = True


            for index, row in GENER_INTERVAL.iterrows():
                if int(row[self.GENRAL_]) >= limit and bandera==True:
                    contPuls = contPuls + 1
                    bandera = False
                elif  int(row[self.GENRAL_])<limit and bandera == False:
                    contPuls = contPuls + 1
                    bandera = True


            #Graficar valores
            
            

            self.graphicD1.plot(x=df['x'], y=df[self.D1_], pen='#2196F3')

            self.graphicD2.plot(x=(df['x']), y=df[self.D2_], pen='#2196F3')

            self.graphicD3.plot(x=(df['x']), y=df[self.D3_], pen='#2196F3')

            self.graphicD3_2.plot(x=(df['x']), y=df[self.AVF_], pen='#2196F3')

            self.graphicD3_3.plot(x=(df['x']), y=df[self.AVR_], pen='#2196F3')

            self.graphicD3_4.plot(x=(df['x']), y=df[self.AVL_], pen='#2196F3')

            self.graphicsView.plot(x=(df['x']), y=df[self.GENRAL_], pen='#2196F3')

            self.graphicsView.setLabel("bottom", "Time / s")

            self.generatedReport(df,persona,values_ST_T,contPuls/2)
        except NameError:
            print("error: "+NameError)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RECAHOLT"))
        MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Open file and report generator"))
        #self.pushButton_2.setText(_translate("MainWindow", "Generar Reporte"))
        self.label_9.setText(_translate("MainWindow", "by Jonathan Recalde"))
        self.label_9.setFont(QtGui.QFont('Times', 20))
        self.label_10.setText(_translate("MainWindow", "RECAHOLT"))
        self.label_10.setFont(QtGui.QFont('Times', 20))
        self.groupBox.setTitle(_translate("MainWindow", "Graphics"))
        self.groupBox.setFont(QtGui.QFont('Times', 20))
        self.label.setText(_translate("MainWindow", "D1"))
        self.label_2.setText(_translate("MainWindow", "D2"))
        self.label_3.setText(_translate("MainWindow", "D3"))
        self.label_4.setText(_translate("MainWindow", "aVF"))
        self.label_5.setText(_translate("MainWindow", "aVR"))
        self.label_6.setText(_translate("MainWindow", "aVL"))
        self.label_nom.setText(_translate("MainWindow", "Name:"))
        self.label_edad.setText(_translate("MainWindow", "Age:"))
        self.label_sexo.setText(_translate("MainWindow", "Gender:"))

        self.graphicD1 = self.graphicD1.addPlot(row=1, col=1)
        self.graphicD2 = self.graphicD2.addPlot(row=1, col=1)
        self.graphicD3 = self.graphicD3.addPlot(row=1, col=1)
        self.graphicD3_2 = self.graphicD3_2.addPlot(row=1, col=1)
        self.graphicD3_3 = self.graphicD3_3.addPlot(row=1, col=1)
        self.graphicD3_4 = self.graphicD3_4.addPlot(row=1, col=1)
        self.graphicsView = self.graphicsView.addPlot(row=1, col=1)



    def generatedReport(self,df,persona,values_ST_T,contPuls):
        #Valores D1
        D1_max= df[self.D1_].max()
        Time_D1=df.query("D1 == '{0}'".format(D1_max))
        int_timeD1= float(Time_D1["x"].values[0])

        ST_D1= values_ST_T[self.D1_]['d1_INTERVAL_1_MAX']
        Time_ST_D1=self.d1_INTERVAL_1.query("D1 == '{0}'".format(ST_D1))
        int_time_ST_D1= float(Time_ST_D1["x"].values[0])

        T_D1= values_ST_T[self.D1_]['d1_INTERVAL_2_MAX']
        Time_T_D1=self.d1_INTERVAL_2.query("D1 == '{0}'".format(T_D1))
        int_time_T_D1= float(Time_T_D1["x"].values[0])

        P_D1= values_ST_T[self.D1_]['d1_INTERVAL_3_MAX']
        Time_P_D1=self.d1_INTERVAL_3.query("D1 == '{0}'".format(P_D1))
        int_time_P_D1= float(Time_P_D1["x"].values[0])
        
        #Valores D2

        D2_max= df[self.D2_].max()
        Time_D2=df.query("D2 == '{0}'".format(D2_max))
        int_timeD2= float(Time_D2["x"].values[0])

        ST_D2= values_ST_T[self.D2_]['d2_INTERVAL_1_MAX']
        Time_ST_D2=self.d2_INTERVAL_1.query("D2 == '{0}'".format(ST_D2))
        int_time_ST_D2= float(Time_ST_D2["x"].values[0])
        
        T_D2= values_ST_T[self.D2_]['d2_INTERVAL_2_MAX']        
        Time_T_D2=self.d2_INTERVAL_2.query("D2 == '{0}'".format(T_D2))
        int_time_T_D2= float(Time_T_D2["x"].values[0])

        P_D2= values_ST_T[self.D2_]['d2_INTERVAL_3_MAX']        
        Time_P_D2=self.d2_INTERVAL_3.query("D2 == '{0}'".format(P_D2))
        int_time_P_D2= float(Time_P_D2["x"].values[0])

        #Valores D3

        D3_max= df[self.D3_].max()
        Time_D3=df.query("D3 == '{0}'".format(D3_max))
        int_timeD3= float(Time_D3["x"].values[0])

        ST_D3= values_ST_T[self.D3_]['d3_INTERVAL_1_MAX']
        Time_ST_D3=self.d3_INTERVAL_1.query("D3 == '{0}'".format(ST_D3))
        int_time_ST_D3= float(Time_ST_D3["x"].values[0])
        
        T_D3= values_ST_T[self.D3_]['d3_INTERVAL_2_MAX']        
        Time_T_D3=self.d3_INTERVAL_2.query("D3 == '{0}'".format(T_D3))
        int_time_T_D3= float(Time_T_D3["x"].values[0])

        P_D3= values_ST_T[self.D3_]['d3_INTERVAL_3_MAX']        
        Time_P_D3=self.d3_INTERVAL_3.query("D3 == '{0}'".format(P_D3))
        int_time_P_D3= float(Time_P_D3["x"].values[0])

        #Valores AVF

        AVF_max= df[self.AVF_].max()
        Time_AVF=df.query("AVF == '{0}'".format(AVF_max))
        int_timeAVF= float(Time_AVF["x"].values[0])

        ST_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_1_MAX']
        Time_ST_AVF=self.avf_INTERVAL_1.query("AVF == '{0}'".format(ST_AVF))
        int_time_ST_AVF= float(Time_ST_AVF["x"].values[0])
        
        T_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_2_MAX']        
        Time_T_AVF=self.avf_INTERVAL_2.query("AVF == '{0}'".format(T_AVF))
        int_time_T_AVF= float(Time_T_AVF["x"].values[0])

        P_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_3_MAX']        
        Time_P_AVF=self.avf_INTERVAL_3.query("AVF == '{0}'".format(P_AVF))
        int_time_P_AVF= float(Time_P_AVF["x"].values[0])

        #Valores AVR

        AVR_max= df[self.AVR_].min()
        Time_AVR=df.query("AVR == '{0}'".format(AVR_max))
        int_timeAVR= float(Time_AVR["x"].values[0])

        ST_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_1_MAX']
        Time_ST_AVR=self.avr_INTERVAL_1.query("AVR == '{0}'".format(ST_AVR))
        int_time_ST_AVR= float(Time_ST_AVR["x"].values[0])
        

        T_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_2_MAX']      
        Time_T_AVR=self.avr_INTERVAL_2.query("AVR == '{0}'".format(T_AVR))
        int_time_T_AVR= float(Time_T_AVR["x"].values[0])

        P_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_3_MAX']      
        Time_P_AVR=self.avr_INTERVAL_3.query("AVR == '{0}'".format(P_AVR))
        int_time_P_AVR= float(Time_P_AVR["x"].values[0])

        #Valores AVL

        AVL_max= df[self.AVL_].max()
        Time_AVL=df.query("AVL == '{0}'".format(AVL_max))
        int_timeAVL= float(Time_AVL["x"].values[0])

        ST_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_1_MAX']
        Time_ST_AVL=self.avl_INTERVAL_1.query("AVL == '{0}'".format(ST_AVL))
        int_time_ST_AVL= float(Time_ST_AVL["x"].values[0])
        
        T_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_2_MAX']        
        Time_T_AVL=self.avl_INTERVAL_2.query("AVL == '{0}'".format(T_AVL))
        int_time_T_AVL= float(Time_T_AVL["x"].values[0])

        P_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_3_MAX']        
        Time_P_AVL=self.avl_INTERVAL_3.query("AVL == '{0}'".format(P_AVL))
        int_time_P_AVL= float(Time_P_AVL["x"].values[0])
        
        # ###################################
        # Content
        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")

        path5 = os.path.join(base_path, 'Report.pdf')

        fileName = path5

        documentTitle = 'ECG REPORT'
        title = 'ECG REPORT'
        subTitle = 'Name:'+persona["Nombre"] +" Age:"+persona["Edad"] +" Gender:"+persona["Genero"]

        textLines = [
        'D1 / R:'+str(float(D1_max))+'     ST: '+str(float(ST_D1))+'     T: '+str(float(T_D1))+'     P: '+str(float(P_D1)),
        'Time: '+str(float(int_timeD1)) +'  Time: '+str(float(int_time_ST_D1))+'  Time: '+str(float(int_time_T_D1))+'  Time: '+str(float(int_time_P_D1)),
        'D2 / R:'+str(float(D2_max))+'     ST: '+str(float(ST_D2))+'     T: '+str(float(T_D2)) +'     P: '+str(float(P_D2)),
        'Time: '+str(float(int_timeD2)) +'  Time: '+str(float(int_time_ST_D2))+'  Time: '+str(float(int_time_T_D2))+'  Time: '+str(float(int_time_P_D2)),
        'D3 / R:'+str(float(D3_max))+'     ST: '+str(float(ST_D3))+'     T: '+str(float(T_D3))+'     P: '+str(float(P_D3)),
        'Time: '+str(float(int_timeD3)) +'  Time: '+str(float(int_time_ST_D3))+'  Time: '+str(float(int_time_T_D3))+'  Time: '+str(float(int_time_P_D3)),
        'aVF / R:'+str(float(AVF_max)) +'     ST: '+str(float(ST_AVF))+'     T: '+str(float(T_AVF))+'     P: '+str(float(P_AVF)),
        'Time: '+str(float(int_timeAVF)) +'  Time: '+str(float(int_time_ST_AVF))+'  Time: '+str(float(int_time_T_AVF))+'  Time: '+str(float(int_time_P_AVF)),
        'aVR / R:'+str(float(AVR_max)) +'     ST: '+str(float(ST_AVR))+'     T: '+str(float(T_AVR))+'     P: '+str(float(P_AVR)),
        'Time: '+str(float(int_timeAVR)) +'  Time: '+str(float(int_time_ST_AVR))+'  Time: '+str(float(int_time_T_AVR))+'  Time: '+str(float(int_time_P_AVR)),
        'aVL / R:'+str(float(AVL_max)) +'     ST: '+str(float(T_AVL))+'     T: '+str(float(ST_AVL))+'     P: '+str(float(P_AVL)),
        'Time: '+str(float(int_timeAVL)) +'  Time: '+str(float(int_time_ST_AVL))+'  Time: '+str(float(int_time_T_AVL))+'  Time: '+str(float(int_time_P_AVL)),
        ]
        # ###################################
        # 0) Create document 
        from reportlab.pdfgen import canvas 

        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        #self.drawMyRuler#(pdf)
        # ###################################
        # 1) Title :: Set fonts 
        # # Print available fonts
        # for font in pdf.getAvailableFonts():
        #     print(font)

        # Register a new font
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics

        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")
        


        path4 = os.path.join(base_path, 'SakBunderan.ttf')
        print(path4)


        pdfmetrics.registerFont(
            TTFont('abc', path4)
        )
        pdf.setFont('abc', 36)
        pdf.drawCentredString(300, 770, title)

        # ###################################
        # 2) Sub Title 
        # RGB - Red Green and Blue
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290,720, subTitle)

        # ###################################
        # 3) Draw a line
        pdf.line(30, 710, 550, 710)

        # ###################################
        # 4) Text object :: for large amounts of text
        from reportlab.lib import colors

        text = pdf.beginText(40, 680)
        text.setFont("Courier", 13)
        text.setFillColor(colors.red)
        val=True
        for line in textLines:
            text.textLine(line)
            if val:
                text.setFillColor(colors.black)
                val=False
            else :
                text.setFillColor(colors.red)
                val=True
                text.textLine("")

        #Valor maximo de X
        value_max_X=float(df["x"].max())/3600
        text.textLine("")
        text.textLine("")
        text.textLine("")
        text.textLine("")
        text.setFillColor(colors.blue)
        truncate = "%.6f" % value_max_X
        text.textLine('Connetion time: '+str(truncate) +" h")
        text.textLine("")
        text.textLine('Heart rate: '+str(round(contPuls)*10) +" bpm")
    

        pdf.drawText(text)
        pdf.save()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


 
 
   


 