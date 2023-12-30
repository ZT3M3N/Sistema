from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Form_VerificacionDeInfraestructura(object):
    def save_to_database(self):
        # Establish a connection to the MySQL database
        connection = pymysql.connect(host='localhost', user='root', password='', database='sistema-administrativo')
        cursor = connection.cursor()

        # Get data from the UI elements
        departamento = self.lineEdit.text()
        area_verificada = self.lineEdit_2.text()
        fecha = self.dateEdit.date().toString("yyyy-MM-dd")

        # Insert data into the database
        query = f"INSERT INTO infraestructura_y_equipo (departamento, area_verificada, fecha) VALUES ('{departamento}', '{area_verificada}', '{fecha}')"
        cursor.execute(query)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()
        
        # After saving data, update the table with the new data
        self.update_table()

    def update_table(self):
        # Clear existing data from the table
        self.tableWidget.clearContents()

        # Establish a connection to the MySQL database
        connection = pymysql.connect(host='localhost', user='root', password='', database='sistema-administrativo')
        cursor = connection.cursor()

        # Fetch data from the database
        query = "SELECT * FROM infraestructura_y_equipo"
        cursor.execute(query)
        data = cursor.fetchall()

        # Set the number of rows in the table based on the fetched data
        self.tableWidget.setRowCount(len(data))

        # Populate the table with the fetched data
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()
                
    def setupUi(self, Form_VerificacionDeInfraestructura):
        Form_VerificacionDeInfraestructura.setObjectName("Form_VerificacionDeInfraestructura")
        Form_VerificacionDeInfraestructura.resize(730, 384)
        Form_VerificacionDeInfraestructura.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.centralwidget = QtWidgets.QWidget(Form_VerificacionDeInfraestructura)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 691, 301))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(227)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 4)
        Form_VerificacionDeInfraestructura.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form_VerificacionDeInfraestructura)
        self.statusbar.setObjectName("statusbar")
        Form_VerificacionDeInfraestructura.setStatusBar(self.statusbar)

        self.retranslateUi(Form_VerificacionDeInfraestructura)
        QtCore.QMetaObject.connectSlotsByName(Form_VerificacionDeInfraestructura)
        
        # Add a button for saving data to the database
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 0, 1, 4)
        self.saveButton.setText("Save to Database")
        self.saveButton.clicked.connect(self.save_to_database)

    def retranslateUi(self, Form_VerificacionDeInfraestructura):
        _translate = QtCore.QCoreApplication.translate
        Form_VerificacionDeInfraestructura.setWindowTitle(_translate("Form_VerificacionDeInfraestructura", "MainWindow"))
        self.label_4.setWhatsThis(_translate("Form_VerificacionDeInfraestructura", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("Form_VerificacionDeInfraestructura", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">REALIZAR VERIFICACIÓN DE</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">INFRAESTRUCTURA Y EQUIPO</span></p></body></html>"))
        self.label.setText(_translate("Form_VerificacionDeInfraestructura", "Jefe(a) del departamento de:"))
        self.label_2.setText(_translate("Form_VerificacionDeInfraestructura", "Jefe(a) del área verificada:"))
        self.label_3.setText(_translate("Form_VerificacionDeInfraestructura", "Fecha:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_VerificacionDeInfraestructura", "Espacio revisado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_VerificacionDeInfraestructura", "Hallazgos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_VerificacionDeInfraestructura", "Atendido"))
        
# Add a placeholder function for fetching data from the database
def get_data_from_database():
    # You need to replace this function with actual code that fetches data from your database
    # For simplicity, I'll return a hardcoded list of tuples
    return [("Data 1", "Data 2", "Data 3"),
            ("Data 4", "Data 5", "Data 6"),
            ("Data 7", "Data 8", "Data 9")]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_VerificacionDeInfraestructura = QtWidgets.QMainWindow()
    ui = Ui_Form_VerificacionDeInfraestructura()
    ui.setupUi(Form_VerificacionDeInfraestructura)
    Form_VerificacionDeInfraestructura.show()
    sys.exit(app.exec_())
