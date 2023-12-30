from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 750)
        MainWindow.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 689, 108))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 1071, 411))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
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
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(340)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 130, 201, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 181, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 130, 546, 24))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 180, 546, 24))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 130, 51, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(870, 130, 101, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        
        # Set the current date for the QDateEdit
        current_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(current_date)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Add a QPushButton for saving data
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(480, 675, 161, 31))
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setText("Guardar Datos")

        # Connect the Save button click event to the save_data_to_database method
        self.pushButton_save.clicked.connect(self.save_data_to_database)
        # Load existing data when the application starts
        self.load_data_from_database()
        
    def load_data_from_database(self):
        import mysql.connector

        # Connect to the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )
        cursor = db_connection.cursor()

        # Select all data from the database
        select_query = "SELECT * FROM infraestructura_y_equipo"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Populate the table with data
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_num, col_num, item)

        # Close connections
        cursor.close()
        db_connection.close()
        
    def save_data_to_database(self):
        import mysql.connector

        # Connect to the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )
        cursor = db_connection.cursor()

        # Get data from the GUI
        jefe_departamento = self.lineEdit.text()
        jefe_area = self.lineEdit_2.text()
        fecha = self.dateEdit.date().toString("yyyy-MM-dd")
        
        # Get the current row
        current_row = self.tableWidget.currentRow()
        
        espacio_revisado = self.tableWidget.item(current_row, 0).text()
        hallazgos = self.tableWidget.item(current_row, 1).text()
        atendido = self.tableWidget.item(current_row, 2).text()

        # Insert data into the database
        insert_query = "INSERT INTO infraestructura_y_equipo (jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido)
        cursor.execute(insert_query, data)

        # Commit changes and close connections
        db_connection.commit()
        cursor.close()
        db_connection.close()

        print("Data saved to the database!")
        
    def load_data_from_database(self):
        import mysql.connector

        # Connect to the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )
        cursor = db_connection.cursor()

        # Execute a SELECT statement to retrieve data
        select_query = "SELECT espacio_revisado, hallazgos, atendido FROM infraestructura_y_equipo"
        cursor.execute(select_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Populate the table with the retrieved data
        for row_index, row_data in enumerate(rows):
            for col_index, col_value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_value))
                self.tableWidget.setItem(row_index, col_index, item)

        # Close connections
        cursor.close()
        db_connection.close()

        print("Data loaded from the database!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">REALIZAR VERIFICACIÓN DE</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">INFRAESTRUCTURA Y EQUIPO</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Espacio revisado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hallazgos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Atendido"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Jefe(a) del departamento de:"))
        self.label_2.setText(_translate("MainWindow", "Jefe(a) del área verificada:"))
        self.label_3.setText(_translate("MainWindow", "Fecha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
