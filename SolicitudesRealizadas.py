from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_SolicitudesRealizadas(object):
    def setupUi(self, SolicitudesRealizadas):
        SolicitudesRealizadas.setObjectName("SolicitudesRealizadas")
        SolicitudesRealizadas.resize(1120, 600)
        SolicitudesRealizadas.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SolicitudesRealizadas)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(20, 90, 1051, 401))
        self.tableWidget_5.setRowCount(10)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(255)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 530, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        SolicitudesRealizadas.setCentralWidget(self.centralwidget)

        self.retranslateUi(SolicitudesRealizadas)
        QtCore.QMetaObject.connectSlotsByName(SolicitudesRealizadas)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(SolicitudesRealizadas))
        
        # Conectar a la base de datos (asegúrate de tener los datos de conexión correctos)
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )
        cursor = db_connection.cursor()

        # Consulta para obtener datos de la tabla solicitud_mantenimiento
        query = "SELECT id, departamentoDirigido, AreaSolicitante, Fecha, DescripcionProblema FROM solicitud_mantenimiento"
        cursor.execute(query)
        data = cursor.fetchall()

        # Configurar la tabla y cargar los datos
        self.tableWidget_5.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_value))
                self.tableWidget_5.setItem(row_num, col_num, item)

        # Cerrar la conexión a la base de datos
        cursor.close()
        db_connection.close()
        
    def regresar(self, main_window):
        from SolicitudDeMantenimiento import Ui_MainWindow as Ui_SolicitudDeMantenimiento
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_SolicitudDeMantenimiento()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()

    def retranslateUi(self, SolicitudesRealizadas):
        _translate = QtCore.QCoreApplication.translate
        SolicitudesRealizadas.setWindowTitle(_translate("SolicitudesRealizadas", "Solicitudes Realizadas"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("SolicitudesRealizadas", "Folio"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("SolicitudesRealizadas", "Depto solicitante"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("SolicitudesRealizadas", "Fecha de realización"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("SolicitudesRealizadas", "Orden de trabajo"))
        self.pushButton_4.setText(_translate("SolicitudesRealizadas", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SolicitudesRealizadas = QtWidgets.QMainWindow()
    ui = Ui_SolicitudesRealizadas()
    ui.setupUi(SolicitudesRealizadas)
    SolicitudesRealizadas.show()
    sys.exit(app.exec_())
