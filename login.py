import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from Controllers.LoginController import LoginController
from ServiciosAdmin import Ui_ServiciosAdmin
from ServiciosTecnico import Ui_ServiciosTecnico
from ServiciosCliente import Ui_ServicioCliente
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def __init__(self):
        self.login_controller = LoginController(self)
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1126, 544)
        Login.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(30, 470, 1071, 51))
        self.btn_login.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(213, 213, 213);")
        self.btn_login.setAutoDefault(False)
        self.btn_login.setDefault(True)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")
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
        self.label_3.setGeometry(QtCore.QRect(190, 330, 221, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_3.setObjectName("label_3")
        self.input_user = QtWidgets.QLineEdit(self.frame)
        self.input_user.setGeometry(QtCore.QRect(410, 230, 511, 31))
        self.input_user.setStyleSheet("font: 8pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(255, 255, 255);")
        self.input_user.setObjectName("input_user")
        self.input_password = QtWidgets.QLineEdit(self.frame)
        self.input_password.setGeometry(QtCore.QRect(410, 340, 511, 31))
        self.input_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 511, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 249, 171);")
        self.label_4.setObjectName("label_4")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        #-----------------EVENTS-------------------------
        self.x = self.btn_login.clicked.connect(self.handle_login)
        #---------------END EVENTS-----------------------
        
    def handle_login(self):
        username = self.input_user.text()
        password = self.input_password.text()

        # Llama a tu controlador de inicio de sesión para verificar las credenciales y obtener el rol
        role = self.login_controller.logIn(username, password, Ui_ServiciosAdmin, Login)

        # Redirige según el rol
        if role == 'Administrador':
            self.redirect_to_admin_interface()
        elif role == 'Técnico':
            self.redirect_to_tech_interface()
        elif role == 'Departamento':
            self.redirect_to_client_interface()

    def redirect_to_admin_interface(self):
        # Crea la instancia de la interfaz de administrador
        admin_interface = QtWidgets.QMainWindow()
        admin_ui = Ui_ServiciosAdmin()
        admin_ui.setupUi(admin_interface)
        admin_interface.show()

        # Cierra la ventana de inicio de sesión
        Login.close()

    def redirect_to_tech_interface(self):
        # Crea la instancia de la interfaz de técnico
        tech_interface = QtWidgets.QMainWindow()
        tech_ui = Ui_ServiciosTecnico()
        tech_ui.setupUi(tech_interface)
        tech_interface.show()

        # Cierra la ventana de inicio de sesión
        Login.close()

    def redirect_to_client_interface(self):
        # Crea la instancia de la interfaz de cliente
        client_interface = QtWidgets.QMainWindow()
        client_ui = Ui_ServicioCliente()
        client_ui.setupUi(client_interface)
        client_interface.show()

        # Cierra la ventana de inicio de sesión
        Login.close()
        


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Inicio de Sesión"))
        self.btn_login.setText(_translate("Login", "Iniciar sesión"))
        self.label_2.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Usuario:</span></p></body></html>"))
        self.label_3.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Contraseña:</span></p></body></html>"))
        self.label_4.setWhatsThis(_translate("Login", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; vertical-align:super;\">Iniciar Sesión</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
