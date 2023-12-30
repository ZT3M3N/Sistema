from PyQt5 import QtCore, QtGui, QtWidgets
from RealizarSolicitud import Ui_RealizarSolicitud
from SolicitudesRealizadas import Ui_SolicitudesRealizadas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 600)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 30, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 330, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 330, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 470, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(lambda: self.abrir_interfaz_realizar_solicitud(MainWindow))
        
        self.pushButton_2.clicked.connect(lambda:self.abrir_interfaz_solicitudes_realizadas(MainWindow))
        
        self.pushButton_3.clicked.connect(lambda: self.regresar_a_servicios(MainWindow))


    def regresar_a_servicios(self, main_window):
        from ServiciosAdmin import Ui_ServiciosAdmin

        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.servicios_admin_window = QtWidgets.QMainWindow()
        servicios_admin_ui = Ui_ServiciosAdmin()
        servicios_admin_ui.setupUi(self.servicios_admin_window)
        self.servicios_admin_window.show()
        main_window.close()
        
    def abrir_interfaz_realizar_solicitud(self, main_window):
        self.realizar_solicitud_window = QtWidgets.QMainWindow()
        realizar_solicitud_ui = Ui_RealizarSolicitud()
        realizar_solicitud_ui.setupUi(self.realizar_solicitud_window)
        self.realizar_solicitud_window.show()
        main_window.close()
        
    def abrir_interfaz_solicitudes_realizadas(self,main_window):
        self.solicitudes_realizadas_window = QtWidgets.QMainWindow()
        solicitudes_realizadas_ui = Ui_SolicitudesRealizadas()
        solicitudes_realizadas_ui.setupUi(self.solicitudes_realizadas_window)
        self.solicitudes_realizadas_window.show()
        main_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solicitud de Mantenimiento"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000; vertical-align:super;\">Solicitud de Mantenimiento</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Realizar Solicitud"))
        self.pushButton_2.setText(_translate("MainWindow", "Solicitudes Realizadas"))
        self.pushButton_3.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
