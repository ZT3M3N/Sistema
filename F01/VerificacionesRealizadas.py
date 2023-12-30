from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerificacionesRealizadas(object):
    def setupUi(self, VerificacionesRealizadas):
        VerificacionesRealizadas.setObjectName("VerificacionesRealizadas")
        VerificacionesRealizadas.resize(772, 372)
        VerificacionesRealizadas.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.centralwidget = QtWidgets.QWidget(VerificacionesRealizadas)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 30, 691, 290))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(227)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        VerificacionesRealizadas.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerificacionesRealizadas)
        QtCore.QMetaObject.connectSlotsByName(VerificacionesRealizadas)

    def retranslateUi(self, VerificacionesRealizadas):
        _translate = QtCore.QCoreApplication.translate
        VerificacionesRealizadas.setWindowTitle(_translate("VerificacionesRealizadas", "MainWindow"))
        self.label_4.setWhatsThis(_translate("VerificacionesRealizadas", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("VerificacionesRealizadas", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">VERIFICACIONES DE INFRAESTRUCTURA</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Y EQUIPO REALIZADAS</span></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("VerificacionesRealizadas", "Folio"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("VerificacionesRealizadas", "Departamento verificado"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("VerificacionesRealizadas", "Jefe del departamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VerificacionesRealizadas = QtWidgets.QMainWindow()
    ui = Ui_VerificacionesRealizadas()
    ui.setupUi(VerificacionesRealizadas)
    VerificacionesRealizadas.show()
    sys.exit(app.exec_())
