from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_OrdenesDeTrabajoAsignadas(object):
    def setupUi(self, OrdenesDeTrabajoAsignadas):
        OrdenesDeTrabajoAsignadas.setObjectName("OrdenesDeTrabajoAsignadas")
        OrdenesDeTrabajoAsignadas.resize(1129, 600)
        OrdenesDeTrabajoAsignadas.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(OrdenesDeTrabajoAsignadas)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(30, 70, 1051, 401))
        self.tableWidget_6.setRowCount(10)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(255)
        self.tableWidget_6.horizontalHeader().setHighlightSections(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 510, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        OrdenesDeTrabajoAsignadas.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrdenesDeTrabajoAsignadas)
        QtCore.QMetaObject.connectSlotsByName(OrdenesDeTrabajoAsignadas)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(OrdenesDeTrabajoAsignadas))
        
        self.retranslateUi(OrdenesDeTrabajoAsignadas)
        QtCore.QMetaObject.connectSlotsByName(OrdenesDeTrabajoAsignadas)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(OrdenesDeTrabajoAsignadas))

        # Llamar a cargar_ordenes para cargar los datos al inicializar la interfaz
        self.cargar_ordenes()
        
    def regresar(self, main_window):
        from OrdenesDeTrabajo import Ui_MainWindow as Ui_OrdenesDeTrabajo
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_OrdenesDeTrabajo()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def cargar_ordenes(self):
        # Conectar a la base de datos y obtener las órdenes asignadas
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema_administrativo"
        )

        cursor = connection.cursor()

        select_query = (
            "SELECT NControl, TipoServicio, AsignadoA, Fecha FROM orden_trabajo"
        )

        print("Consultando órdenes asignadas...")
        cursor.execute(select_query)

        # Obtener todos los resultados
        ordenes_asignadas = cursor.fetchall()

        print("Datos recuperados:", ordenes_asignadas)
        connection.close()

        # Llenar la tabla con los datos obtenidos
        self.tableWidget_6.setRowCount(len(ordenes_asignadas))
        for row, orden in enumerate(ordenes_asignadas):
            for col, value in enumerate(orden):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_6.setItem(row, col, item)

    def retranslateUi(self, OrdenesDeTrabajoAsignadas):
        _translate = QtCore.QCoreApplication.translate
        OrdenesDeTrabajoAsignadas.setWindowTitle(_translate("OrdenesDeTrabajoAsignadas", "Órdenes de Trabajo Asignadas"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("OrdenesDeTrabajoAsignadas", "No. Control"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("OrdenesDeTrabajoAsignadas", "Tipo de servicio"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("OrdenesDeTrabajoAsignadas", "Asignado"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("OrdenesDeTrabajoAsignadas", "Fecha de aprobación"))
        self.pushButton_4.setText(_translate("OrdenesDeTrabajoAsignadas", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrdenesDeTrabajoAsignadas = QtWidgets.QMainWindow()
    ui = Ui_OrdenesDeTrabajoAsignadas()
    ui.setupUi(OrdenesDeTrabajoAsignadas)
    OrdenesDeTrabajoAsignadas.show()
    sys.exit(app.exec_())
