from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServicioCliente(object):
    def setupUi(self, ServicioCliente):
        ServicioCliente.setObjectName("ServicioCliente")
        ServicioCliente.resize(1109, 600)
        ServicioCliente.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ServicioCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 270, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        ServicioCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(ServicioCliente)
        QtCore.QMetaObject.connectSlotsByName(ServicioCliente)

    def retranslateUi(self, ServicioCliente):
        _translate = QtCore.QCoreApplication.translate
        ServicioCliente.setWindowTitle(_translate("ServicioCliente", "Inicio de sesión como: Departamento"))
        self.label_4.setWhatsThis(_translate("ServicioCliente", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("ServicioCliente", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000; vertical-align:super;\">Seleccione una opción</span></p></body></html>"))
        self.pushButton_4.setText(_translate("ServicioCliente", "Solicitudes de Mantenimiento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServicioCliente = QtWidgets.QMainWindow()
    ui = Ui_ServicioCliente()
    ui.setupUi(ServicioCliente)
    ServicioCliente.show()
    sys.exit(app.exec_())
