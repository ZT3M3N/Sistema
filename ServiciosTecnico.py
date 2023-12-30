from PyQt5 import QtCore, QtGui, QtWidgets
from VerificarInfraestructura import Ui_MainWindow as Ui_VerificarInfraestructura
from OrdenesDeTrabajo import Ui_MainWindow as Ui_OrdenesTrabajo
from SolicitudDeMantenimiento import Ui_MainWindow as Ui_SolicitudMantenimiento

class Ui_ServiciosTecnico(object):
    def setupUi(self, ServiciosTecnico):
        ServiciosTecnico.setObjectName("ServiciosTecnico")
        ServiciosTecnico.resize(1132, 600)
        ServiciosTecnico.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ServiciosTecnico)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 315, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 314, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 430, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 50, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        ServiciosTecnico.setCentralWidget(self.centralwidget)

        self.retranslateUi(ServiciosTecnico)
        QtCore.QMetaObject.connectSlotsByName(ServiciosTecnico)
        
        # Añade esta línea para crear y asignar la referencia a la ventana principal
        self.main_window = ServiciosTecnico

    # Conecta los botones después de asignar self.main_window
        self.pushButton.clicked.connect(lambda: self.abrir_verificar_infraestructura(ServiciosTecnico)) #1
        self.pushButton_3.clicked.connect(lambda: self.abrir_ordenes_trabajo(ServiciosTecnico)) #3
        self.pushButton_4.clicked.connect(lambda: self.abrir_solicitudes_mantenimiento(ServiciosTecnico)) #4
        
    #1
    def abrir_verificar_infraestructura(self, main_window):
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.verificar_infraestructura_window = QtWidgets.QMainWindow()
        verificar_infraestructura_ui = Ui_VerificarInfraestructura()
        verificar_infraestructura_ui.setupUi(self.verificar_infraestructura_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.verificar_infraestructura_window.show()
        main_window.close()
        
    #3
    def abrir_ordenes_trabajo(self, main_window):
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.ordenes_trabajo_window = QtWidgets.QMainWindow()
        ordenes_trabajo_ui = Ui_OrdenesTrabajo()
        ordenes_trabajo_ui.setupUi(self.ordenes_trabajo_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.ordenes_trabajo_window.show()
        main_window.close()
        
    #4
    def abrir_solicitudes_mantenimiento(self, main_window):
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.solicitudes_mantenimiento_window = QtWidgets.QMainWindow()
        solicitudes_mantenimiento_ui = Ui_SolicitudMantenimiento()
        solicitudes_mantenimiento_ui.setupUi(self.solicitudes_mantenimiento_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.solicitudes_mantenimiento_window.show()
        main_window.close()

    def retranslateUi(self, ServiciosTecnico):
        _translate = QtCore.QCoreApplication.translate
        ServiciosTecnico.setWindowTitle(_translate("ServiciosTecnico", "Inicio de sesión como: Técnico"))
        self.pushButton.setText(_translate("ServiciosTecnico", "Verificar Infraestructura y Equipo"))
        self.pushButton_3.setText(_translate("ServiciosTecnico", "Órdenes de Trabajo"))
        self.pushButton_4.setText(_translate("ServiciosTecnico", "Solicitudes de Mantenimiento"))
        self.label_4.setWhatsThis(_translate("ServiciosTecnico", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("ServiciosTecnico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000; vertical-align:super;\">Seleccione una opción</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServiciosTecnico = QtWidgets.QMainWindow()
    ui = Ui_ServiciosTecnico()
    ui.setupUi(ServiciosTecnico)
    ServiciosTecnico.show()
    sys.exit(app.exec_())
