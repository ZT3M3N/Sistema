from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 639)
        MainWindow.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 834, 108))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 1041, 411))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(337)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
         # Llama a la función para cargar datos desde la base de datos
        self.load_data_from_database()
        
    def load_data_from_database(self):
        # Connect to the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )
        cursor = db_connection.cursor()

        # Execute a SELECT statement to retrieve data
        select_query = "SELECT id, jefe_departamento, jefe_area FROM infraestructura_y_equipo"
        cursor.execute(select_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
        
        # Rellena la primera fila con los datos del "id"
        for col_index, col_value in enumerate(rows[0]):
            item = QtWidgets.QTableWidgetItem(str(col_value))
            self.tableWidget.setItem(0, col_index, item)

        # Rellena las siguientes filas con los datos de "jefe_departamento" y "jefe_area"
        for row_index, row_data in enumerate(rows[1:]):
            for col_index, col_value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_value))
                self.tableWidget.setItem(row_index + 1, col_index, item)
        # Cierra las conexiones
        cursor.close()
        db_connection.close()

        print("Datos cargados desde la base de datos!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">VERIFICACIONES DE INFRAESTRUCTURA</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Y EQUIPO REALIZADAS</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folio"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Departamento Verificado"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Jefe del Departamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
