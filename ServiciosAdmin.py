from PyQt5 import QtCore, QtGui, QtWidgets
from VerificarInfraestructura import Ui_MainWindow as Ui_VerificarInfraestructura
from ElaborarProgramadeMantenimientoPreventivo import Ui_MainWindow as Ui_ProgramaMantenimiento
from OrdenesDeTrabajo import Ui_MainWindow as Ui_OrdenesTrabajo
from SolicitudDeMantenimiento import Ui_MainWindow as Ui_SolicitudMantenimiento


class Ui_ServiciosAdmin(object):
    def setupUi(self, ServiciosAdmin):
        ServiciosAdmin.setObjectName("ServiciosAdmin")
        ServiciosAdmin.resize(1124, 559)
        ServiciosAdmin.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ServiciosAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 164, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 165, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 314, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 314, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 450, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    rgb(170, 0, 0)\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        ServiciosAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(ServiciosAdmin)
        QtCore.QMetaObject.connectSlotsByName(ServiciosAdmin)
        
        # Añade esta línea para crear y asignar la referencia a la ventana principal
        self.main_window = ServiciosAdmin

    # Conecta los botones después de asignar self.main_window
        self.pushButton.clicked.connect(lambda: self.abrir_verificar_infraestructura(ServiciosAdmin)) #1
        self.pushButton_2.clicked.connect(lambda: self.abrir_programa_mantenimiento(ServiciosAdmin)) #2
        self.pushButton_3.clicked.connect(lambda: self.abrir_ordenes_trabajo(ServiciosAdmin)) #3
        self.pushButton_4.clicked.connect(lambda: self.abrir_solicitudes_mantenimiento(ServiciosAdmin)) #4
        self.pushButton_5.clicked.connect(lambda: self.abrir_registro_usuario(ServiciosAdmin)) #5
        
    #1
    def abrir_verificar_infraestructura(self, main_window):
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.verificar_infraestructura_window = QtWidgets.QMainWindow()
        verificar_infraestructura_ui = Ui_VerificarInfraestructura()
        verificar_infraestructura_ui.setupUi(self.verificar_infraestructura_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.verificar_infraestructura_window.show()
        main_window.close()
        
    #2
    def abrir_programa_mantenimiento(self, main_window):
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.programa_mantenimiento_window = QtWidgets.QMainWindow()
        programa_mantenimiento_ui = Ui_ProgramaMantenimiento()
        programa_mantenimiento_ui.setupUi(self.programa_mantenimiento_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.programa_mantenimiento_window.show()
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
        
    #5
    def abrir_registro_usuario(self, main_window):
        from registro import Ui_registro
        # Crea una instancia de la ventana de VerificarInfraestructura
        self.registro_usuario_window = QtWidgets.QMainWindow()
        registro_usuario_ui = Ui_registro()
        registro_usuario_ui.setupUi(self.registro_usuario_window)

        # Muestra la ventana de VerificarInfraestructura y cierra la ventana actual
        self.registro_usuario_window.show()
        main_window.close()



    def retranslateUi(self, ServiciosAdmin):
        _translate = QtCore.QCoreApplication.translate
        ServiciosAdmin.setWindowTitle(_translate("ServiciosAdmin", "Inicio de sesión como: Administrador"))
        self.pushButton.setText(_translate("ServiciosAdmin", "Verificar Infraestructura y Equipo"))
        self.pushButton_2.setText(_translate("ServiciosAdmin", "Elaborar Programa de Mantenimiento Preventivo"))
        self.pushButton_3.setText(_translate("ServiciosAdmin", "Órdenes de Trabajo"))
        self.pushButton_4.setText(_translate("ServiciosAdmin", "Solicitudes de Mantenimiento"))
        self.pushButton_5.setText(_translate("ServiciosAdmin", "Registrar Usuario"))
        self.label_4.setWhatsThis(_translate("ServiciosAdmin", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("ServiciosAdmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000; vertical-align:super;\">Seleccione una opción</span></p></body></html>"))
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServiciosAdmin = QtWidgets.QMainWindow()
    ui = Ui_ServiciosAdmin()
    ui.setupUi(ServiciosAdmin)
    ServiciosAdmin.show()
    sys.exit(app.exec_())
