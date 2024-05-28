from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_VerificacionesRealizadas(object):
    def setupUi(self, VerificacionesRealizadas):
        VerificacionesRealizadas.setObjectName("VerificacionesRealizadas")
        VerificacionesRealizadas.resize(1105, 600)
        VerificacionesRealizadas.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VerificacionesRealizadas)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 100, 1051, 411))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(339)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 540, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        VerificacionesRealizadas.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerificacionesRealizadas)
        QtCore.QMetaObject.connectSlotsByName(VerificacionesRealizadas)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(VerificacionesRealizadas))
        
        # Configurar la tabla
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setHorizontalHeaderLabels(["Folio", "Jefe del departamento verificado", "Jefe del departamento"])

        # Cargar datos en la tabla
        self.cargar_datos()
        
    def regresar(self, main_window):
        from VerificarInfraestructura import Ui_MainWindow as Ui_VerificarInfraestructura
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_VerificarInfraestructura()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def cargar_datos(self):
        # Conectar a la base de datos
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='sistema_administrativo',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Seleccionar datos de la tabla infraestructura_y_equipo
                sql = "SELECT id, jefe_departamento, jefe_area FROM infraestructura_y_equipo"
                cursor.execute(sql)
                result = cursor.fetchall()

                # Limpiar la tabla antes de cargar nuevos datos
                self.tableWidget_2.setRowCount(0)

                # Cargar datos en la tabla
                for row_number, row_data in enumerate(result):
                    self.tableWidget_2.insertRow(row_number)
                    for column_number, data in enumerate(row_data.values()):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget_2.setItem(row_number, column_number, item)

        except Exception as e:
            print(f"Error al cargar datos: {e}")

        finally:
            connection.close()

    def retranslateUi(self, VerificacionesRealizadas):
        _translate = QtCore.QCoreApplication.translate
        VerificacionesRealizadas.setWindowTitle(_translate("VerificacionesRealizadas", "Verificaciones Realizadas"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("VerificacionesRealizadas", "Folio"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("VerificacionesRealizadas", "Jefe del departamento verificado"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("VerificacionesRealizadas", "Jefe del departamento"))
        self.pushButton_4.setText(_translate("VerificacionesRealizadas", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VerificacionesRealizadas = QtWidgets.QMainWindow()
    ui = Ui_VerificacionesRealizadas()
    ui.setupUi(VerificacionesRealizadas)
    VerificacionesRealizadas.show()
    sys.exit(app.exec_())
