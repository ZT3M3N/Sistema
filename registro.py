import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from login import Ui_Login

class Ui_registro(object):
    def setupUi(self, registro):
        registro.setObjectName("registro")
        registro.resize(1126, 600)
        registro.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(registro)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_registro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registro.setGeometry(QtCore.QRect(30, 470, 1071, 51))
        self.btn_registro.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(213, 213, 213);")
        self.btn_registro.setAutoDefault(False)
        self.btn_registro.setDefault(True)
        self.btn_registro.setFlat(False)
        self.btn_registro.setObjectName("btn_registro")
        
        self.btn_regresar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_regresar.setGeometry(QtCore.QRect(30, 530, 1071, 51))
        self.btn_regresar.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 0);")
        self.btn_regresar.setAutoDefault(False)
        self.btn_regresar.setDefault(False)
        self.btn_regresar.setFlat(False)
        self.btn_regresar.setObjectName("btn_regresar")
        self.btn_regresar.setText("Regresar")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1071, 411))
        self.frame.setStyleSheet("QWidget#frame{\n"
"border-radius:10px;    \n"
"background-color: rgb(255, 249, 171);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 220, 151, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(190, 270, 221, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_3.setObjectName("label_3")
        self.user = QtWidgets.QLineEdit(self.frame)
        self.user.setGeometry(QtCore.QRect(410, 230, 511, 31))
        self.user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user.setAutoFillBackground(False)
        self.user.setStyleSheet("font: 10pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(255, 255, 255);")
        self.user.setText("")
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(410, 280, 511, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(270, 50, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(410, 332, 171, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(120, 320, 271, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_5.setObjectName("label_5")
        registro.setCentralWidget(self.centralwidget)

        self.retranslateUi(registro)
        QtCore.QMetaObject.connectSlotsByName(registro)
        
        self.btn_regresar.clicked.connect(lambda: self.regresar_a_servicios(registro))


    def regresar_a_servicios(self, main_window):
        from ServiciosAdmin import Ui_ServiciosAdmin

        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.servicios_admin_window = QtWidgets.QMainWindow()
        servicios_admin_ui = Ui_ServiciosAdmin()
        servicios_admin_ui.setupUi(self.servicios_admin_window)
        self.servicios_admin_window.show()
        main_window.close()
        
        

    def retranslateUi(self, registro):
        _translate = QtCore.QCoreApplication.translate
        registro.setWindowTitle(_translate("registro", "Registro de Usuario"))
        self.btn_registro.setText(_translate("registro", "Registrar datos"))
        self.label_2.setText(_translate("registro", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Usuario:</span></p></body></html>"))
        self.label_3.setText(_translate("registro", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Contraseña:</span></p></body></html>"))
        self.label_4.setWhatsThis(_translate("registro", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("registro", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; vertical-align:super;\">Registro de usuario</span></p></body></html>"))
        self.label_5.setText(_translate("registro", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Tipo de usuario:</span></p></body></html>"))
        
        #<---------------------CONEXIÓN PARA MOSTRAR LOS ROLES EN EL COMBO BOX---------------->
        # Create a connection to your MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Execute a query to retrieve data from your database
        query = "SELECT tipo FROM roles"
        cursor.execute(query)

        # Fetch all the results
        result = cursor.fetchall()

        # Populate the QComboBox with the retrieved data
        for row in result:
            self.comboBox.addItem(row[0])

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()
        #<------------FIN DE LA CONEXIÓN----------------------->
        
     # Connect the button click event to a method for saving data
        self.btn_registro.clicked.connect(self.save_data)

        # New code for saving data to the database
    def save_data(self):
        try:
            # Retrieve data from the form
            username = self.user.text()
            password = self.password.text()
            user_type = self.comboBox.currentText()

            # Create a connection to your MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sistema-administrativo"
            )

            # Create a cursor object to execute SQL queries
            cursor = db_connection.cursor()

            # Execute a query to insert data into your database
            query = "INSERT INTO usuarios (user_name, password, id_rol) VALUES (%s, %s, %s)"
            values = (username, password, user_type)
            cursor.execute(query, values)

            # Commit the changes and close the cursor and database connection
            db_connection.commit()
            cursor.close()
            db_connection.close()
            
           # Show a success message box
            QMessageBox.information(
                self.centralwidget,
                "",
                "Usuario registrado correctamente",
                QMessageBox.Ok
                )
            
            registro.close()
            
            # Redirect to the Ui_Login class
            self.redirect_to_login()
            
        except Exception as e:
                # Handle the exception (e.g., show an error message)
            print(f"Error: {e}")
    # Method to redirect to the Ui_Login class
    def redirect_to_login(self):
            # Create an instance of the Ui_Login class
        login_window = QtWidgets.QMainWindow()
        ui_login = Ui_Login()
        ui_login.setupUi(login_window)
        login_window.show()
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registro = QtWidgets.QMainWindow()
    ui = Ui_registro()
    ui.setupUi(registro)
    registro.show()
    sys.exit(app.exec_())
