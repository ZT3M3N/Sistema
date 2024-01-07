from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog
import io


class Ui_AsignarOrdenDeTrabajo(object):
    def setupUi(self, AsignarOrdenDeTrabajo):
        AsignarOrdenDeTrabajo.setObjectName("AsignarOrdenDeTrabajo")
        AsignarOrdenDeTrabajo.resize(1115, 600)
        AsignarOrdenDeTrabajo.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(AsignarOrdenDeTrabajo)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 30, 181, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 90, 281, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(530, 30, 101, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(660, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(660, 90, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(850, 30, 181, 20))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 190, 981, 181))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 430, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 490, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_4.setGeometry(QtCore.QRect(930, 90, 101, 22))
        self.dateEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(670, 430, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(670, 490, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_5.setGeometry(QtCore.QRect(930, 430, 101, 22))
        self.dateEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_6.setGeometry(QtCore.QRect(930, 490, 101, 22))
        self.dateEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(280, 430, 321, 20))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(280, 490, 321, 20))
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 550, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 550, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        AsignarOrdenDeTrabajo.setCentralWidget(self.centralwidget)

        self.retranslateUi(AsignarOrdenDeTrabajo)
        QtCore.QMetaObject.connectSlotsByName(AsignarOrdenDeTrabajo)
        
        self.pushButton_3.clicked.connect(lambda:self.regresar(AsignarOrdenDeTrabajo))
        
        self.pushButton_4.clicked.connect(self.guardar_datos)
        
    def regresar(self, main_window):
        from OrdenesDeTrabajo import Ui_MainWindow as Ui_OrdenesDeTrabajo
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_OrdenesDeTrabajo()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def guardar_datos(self):
        # Obtener datos de la interfaz de usuario
        n_control = self.lineEdit_7.text()
        tipo_mantenimiento = self.comboBox.currentText()
        tipo_servicio = self.lineEdit_10.text()
        asignado_a = self.lineEdit_8.text()
        fecha = self.dateEdit_4.date().toString("yyyy-MM-dd")
        trabajo_realizado = self.plainTextEdit.toPlainText()
        verificado_por = self.lineEdit_9.text()
        aprobado_por = self.lineEdit_11.text()
        
        # Obtener la ruta y el nombre del archivo mediante un cuadro de diálogo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_new_path, _ = QFileDialog.getSaveFileName(self.centralwidget, "Guardar PDF", "", "Archivos PDF (*.pdf);;Todos los archivos (*)", options=options)
        
        # Verificar si el usuario canceló la operación
        if pdf_new_path:
        # Generar el PDF
            self.generar_pdf(n_control, tipo_mantenimiento, tipo_servicio, asignado_a, fecha, trabajo_realizado, verificado_por, aprobado_por, pdf_new_path)

        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema_administrativo"
        )

        cursor = connection.cursor()

        # Consulta SQL para insertar datos en la tabla solicitud_mantenimiento
        insert_query = (
            "INSERT INTO orden_trabajo "
            "(NControl, TipoMantenimiento, TipoServicio, AsignadoA, Fecha, TrabajoRealizado, VerificadoPor, AprobadoPor) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )

        # Datos a insertar
        data = (n_control, tipo_mantenimiento, tipo_servicio, asignado_a, fecha, trabajo_realizado, verificado_por, aprobado_por)

        # Ejecutar la consulta
        cursor.execute(insert_query, data)

        # Confirmar la transacción y cerrar la conexión
        connection.commit()
        connection.close()
        
        # Generar PDF
        self.generar_pdf(n_control, tipo_mantenimiento, tipo_servicio, asignado_a, fecha, trabajo_realizado, verificado_por, aprobado_por, pdf_new_path)
        
    def generar_pdf(self, n_control, tipo_mantenimiento, tipo_servicio, asignado_a, fecha, trabajo_realizado, verificado_por, aprobado_por, pdf_new_path):
        # Ruta del archivo PDF existente
        pdf_existing_path = "FORMATOS/TecNM-AD-PO-001-04.pdf"

        # Crear un objeto PdfWriter para el nuevo archivo PDF
        pdf_writer = PdfWriter()

        # Leer el archivo PDF existente
        pdf_reader = PdfReader(pdf_existing_path)

        # Obtener el número de páginas en el PDF existente
        num_pages = len(pdf_reader.pages)

        # Iterar a través de cada página del PDF existente
        for page_num in range(num_pages):
            # Crear un lienzo para la página actual
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(612, 792))

            # Agregar contenido al lienzo con los datos obtenidos de la interfaz
            can.drawString(450, 605, n_control)
            can.drawString(265, 570, tipo_mantenimiento)
            can.drawString(175, 545, tipo_servicio)
            can.drawString(150, 520, asignado_a)
            can.drawString(220, 470, fecha)
            can.drawString(75, 430, trabajo_realizado)
            can.drawString(75, 298, verificado_por)
            can.drawString(75, 267, aprobado_por)
            can.drawString(450, 298, fecha)
            can.drawString(450, 267, fecha)
            

            # Guardar el lienzo en el paquete
            can.save()

            # Mover el paquete al inicio antes de escribir en el nuevo archivo
            packet.seek(0)

            # Crear un objeto PdfReader para la página actual
            new_pdf = PdfReader(packet)
            page = pdf_reader.pages[page_num]

            # Fusionar el contenido de la página existente con el contenido nuevo
            page.merge_page(new_pdf.pages[0])

            # Agregar la página fusionada al nuevo archivo PDF
            pdf_writer.add_page(page)

        # Guardar el nuevo archivo PDF
        with open(pdf_new_path, "wb") as new_pdf_file:
            pdf_writer.write(new_pdf_file)

    def retranslateUi(self, AsignarOrdenDeTrabajo):
        _translate = QtCore.QCoreApplication.translate
        AsignarOrdenDeTrabajo.setWindowTitle(_translate("AsignarOrdenDeTrabajo", "Asignar Orden de Trabajo"))
        self.label_10.setText(_translate("AsignarOrdenDeTrabajo", "No. de control:"))
        self.label_11.setText(_translate("AsignarOrdenDeTrabajo", "Asignado a:"))
        self.label_12.setText(_translate("AsignarOrdenDeTrabajo", "Mantenimiento:"))
        self.comboBox.setItemText(0, _translate("AsignarOrdenDeTrabajo", "Interno"))
        self.comboBox.setItemText(1, _translate("AsignarOrdenDeTrabajo", "Externo"))
        self.label_13.setText(_translate("AsignarOrdenDeTrabajo", "Tipo de servicio:"))
        self.label_14.setText(_translate("AsignarOrdenDeTrabajo", "Fecha de realización:"))
        self.label_15.setText(_translate("AsignarOrdenDeTrabajo", "Trabajo realizado:"))
        self.label_16.setText(_translate("AsignarOrdenDeTrabajo", "Verificado y realizado por:"))
        self.label_17.setText(_translate("AsignarOrdenDeTrabajo", "Aprobado por: "))
        self.label_18.setText(_translate("AsignarOrdenDeTrabajo", "Fecha y firma:"))
        self.label_19.setText(_translate("AsignarOrdenDeTrabajo", "Fecha y firma:"))
        self.pushButton_3.setText(_translate("AsignarOrdenDeTrabajo", "Regresar"))
        self.pushButton_4.setText(_translate("AsignarOrdenDeTrabajo", "Guardar y Generar Reporte"))
        
        # List of QDateEdit widgets
        date_edit_widgets = [self.dateEdit_4, self.dateEdit_5,self.dateEdit_6]

        # Set the default date to the current date for all QDateEdit widgets
        for date_edit in date_edit_widgets:
            date_edit.setDate(QtCore.QDate.currentDate())
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AsignarOrdenDeTrabajo = QtWidgets.QMainWindow()
    ui = Ui_AsignarOrdenDeTrabajo()
    ui.setupUi(AsignarOrdenDeTrabajo)
    AsignarOrdenDeTrabajo.show()
    sys.exit(app.exec_())
