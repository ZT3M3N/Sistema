import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User
from ServiciosAdmin import Ui_ServiciosAdmin
from ServiciosTecnico import Ui_ServiciosTecnico
from ServiciosCliente import Ui_ServicioCliente

class LoginController():

    def __init__(self, login):
        self.login = login
        self.user = User(connection())

    def logIn(self, user, password, Ui_Dialog, LogIn):
        if user and password:
            user_info = self.user.getUser(user, password)
            if user_info:
                user_id, username, _, role_id = user_info
                if role_id == 1:  # Administrator
                    LogIn.hide()
                    self.login.Form = QtWidgets.QMainWindow()
                    self.login.ui = Ui_Dialog()
                    self.login.ui.setupUi(self.login.Form)
                    self.login.Form.show()
                    print("Estás logeado como Administrador")
                elif role_id == 2:  # Technician
                    LogIn.hide()
                    self.login.Form = QtWidgets.QMainWindow()
                    self.login.ui = Ui_ServiciosTecnico()
                    self.login.ui.setupUi(self.login.Form)
                    self.login.Form.show()
                    print("Estás logeado como Técnico")    
                elif role_id == 3:  # Client
                    LogIn.hide()
                    self.login.Form = QtWidgets.QMainWindow()
                    self.login.ui = Ui_ServicioCliente()
                    self.login.ui.setupUi(self.login.Form)
                    self.login.Form.show()
                    print("Estás logeado como Cliente")
                else:
                    print("Role desconocido")
            else:
                print("No estás logeado")
