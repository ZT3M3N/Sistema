# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElaborarProgramaDeMantenimiento.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_ProgramaDeMantenimiento(object):
    def setupUi(self, Form_ProgramaDeMantenimiento):
        Form_ProgramaDeMantenimiento.setObjectName("Form_ProgramaDeMantenimiento")
        Form_ProgramaDeMantenimiento.resize(737, 404)
        Form_ProgramaDeMantenimiento.setStyleSheet("background-color: rgb(255, 249, 171);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Form_ProgramaDeMantenimiento)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 701, 340))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 7)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 5, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout.addWidget(self.dateEdit_3, 2, 6, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(15)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(14, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(46)
        self.gridLayout.addWidget(self.tableWidget_3, 3, 0, 1, 7)
        Form_ProgramaDeMantenimiento.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form_ProgramaDeMantenimiento)
        self.statusbar.setObjectName("statusbar")
        Form_ProgramaDeMantenimiento.setStatusBar(self.statusbar)

        self.retranslateUi(Form_ProgramaDeMantenimiento)
        QtCore.QMetaObject.connectSlotsByName(Form_ProgramaDeMantenimiento)

    def retranslateUi(self, Form_ProgramaDeMantenimiento):
        _translate = QtCore.QCoreApplication.translate
        Form_ProgramaDeMantenimiento.setWindowTitle(_translate("Form_ProgramaDeMantenimiento", "MainWindow"))
        self.label_10.setWhatsThis(_translate("Form_ProgramaDeMantenimiento", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_10.setText(_translate("Form_ProgramaDeMantenimiento", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">ELABORAR PROGRAMA DE</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">MANTENIMIENTO PREVENTIVO</span></p></body></html>"))
        self.label_4.setText(_translate("Form_ProgramaDeMantenimiento", "Semestre:"))
        self.label_5.setText(_translate("Form_ProgramaDeMantenimiento", "Año:"))
        self.label_6.setText(_translate("Form_ProgramaDeMantenimiento", "Fecha de elaboración:"))
        self.label_7.setText(_translate("Form_ProgramaDeMantenimiento", "Elaboró:"))
        self.label_8.setText(_translate("Form_ProgramaDeMantenimiento", "Aprobó:"))
        self.label_9.setText(_translate("Form_ProgramaDeMantenimiento", "Fecha de aprobación:"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "No"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Servicio"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Tipo"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "E"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Ene"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Mar"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Abr"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "May"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Jun"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Jul"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Ago"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Sep"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Oct"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Nov"))
        item = self.tableWidget_3.horizontalHeaderItem(14)
        item.setText(_translate("Form_ProgramaDeMantenimiento", "Dic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_ProgramaDeMantenimiento = QtWidgets.QMainWindow()
    ui = Ui_Form_ProgramaDeMantenimiento()
    ui.setupUi(Form_ProgramaDeMantenimiento)
    Form_ProgramaDeMantenimiento.show()
    sys.exit(app.exec_())
