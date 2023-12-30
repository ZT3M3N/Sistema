from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgramasRealizados(object):
    def setupUi(self, ProgramasRealizados):
        ProgramasRealizados.setObjectName("ProgramasRealizados")
        ProgramasRealizados.resize(1113, 600)
        ProgramasRealizados.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ProgramasRealizados)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 100, 1051, 401))
        self.tableWidget_4.setRowCount(10)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(340)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 530, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        ProgramasRealizados.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgramasRealizados)
        QtCore.QMetaObject.connectSlotsByName(ProgramasRealizados)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(ProgramasRealizados))
        
    def regresar(self, main_window):
        from ElaborarProgramadeMantenimientoPreventivo import Ui_MainWindow as Ui_ElaborarProgramaDeMantenimientoPreventivo
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_ElaborarProgramaDeMantenimientoPreventivo()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()

    def retranslateUi(self, ProgramasRealizados):
        _translate = QtCore.QCoreApplication.translate
        ProgramasRealizados.setWindowTitle(_translate("ProgramasRealizados", "Programas Realizados"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("ProgramasRealizados", "Folio"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("ProgramasRealizados", "Semestre"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("ProgramasRealizados", "Año"))
        self.pushButton_4.setText(_translate("ProgramasRealizados", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgramasRealizados = QtWidgets.QMainWindow()
    ui = Ui_ProgramasRealizados()
    ui.setupUi(ProgramasRealizados)
    ProgramasRealizados.show()
    sys.exit(app.exec_())
