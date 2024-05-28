from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog
import io

class Ui_RealizarSolicitud(object):
    def setupUi(self, RealizarSolicitud):
        RealizarSolicitud.setObjectName("RealizarSolicitud")
        RealizarSolicitud.resize(1116, 600)
        RealizarSolicitud.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RealizarSolicitud)
        self.centralwidget.setObjectName("centralwidget")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(50, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(110, 50, 171, 20))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(50, 90, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(50, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(200, 130, 171, 20))
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(420, 90, 271, 20))
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(740, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.dateEdit_7 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_7.setGeometry(QtCore.QRect(950, 50, 110, 22))
        self.dateEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(420, 130, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(700, 130, 361, 20))
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(50, 200, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 240, 1051, 261))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 540, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 540, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        RealizarSolicitud.setCentralWidget(self.centralwidget)

        self.retranslateUi(RealizarSolicitud)
        QtCore.QMetaObject.connectSlotsByName(RealizarSolicitud)
        
        self.pushButton_3.clicked.connect(lambda:self.regresar(RealizarSolicitud))
        self.pushButton_4.clicked.connect(self.guardar_datos)
        
        # Fetch the next available ID and set it in the Folio field
        next_id = self.get_next_id()
        self.lineEdit_12.setText(str(next_id))

        
    def regresar(self, main_window):
        from SolicitudDeMantenimiento import Ui_MainWindow as Ui_SolicitudDeMantenimiento
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_SolicitudDeMantenimiento()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def guardar_datos(self):
        # Obtain data from the user interface
        folio = self.lineEdit_12.text()
        departamento_dirigido = self.lineEdit_14.text()
        area_solicitante = self.lineEdit_13.text()
        nombre_y_firma = self.lineEdit_15.text()
        fecha = self.dateEdit_7.date().toString("yyyy-MM-dd")
        descripcion_problema = self.textEdit_2.toPlainText()
        
        # Obtener la ruta y el nombre del archivo mediante un cuadro de diálogo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_new_path, _ = QFileDialog.getSaveFileName(self.centralwidget, "Guardar PDF", "", "Archivos PDF (*.pdf);;Todos los archivos (*)", options=options)

    # Verificar si el usuario canceló la operación
        if pdf_new_path:
        # Generar el PDF
            self.generar_pdf(folio, departamento_dirigido, area_solicitante, nombre_y_firma, fecha, descripcion_problema, pdf_new_path)

        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Enter your MySQL password
            database="sistema_administrativo"
        )

        cursor = connection.cursor()

        # SQL query to insert data into the solicitud_mantenimiento table
        insert_query = (
            "INSERT INTO solicitud_mantenimiento "
            "(departamentoDirigido, AreaSolicitante, NombreYFirma, Fecha, DescripcionProblema) "
            "VALUES (%s, %s, %s, %s, %s)"
        )

        # Data to be inserted
        data = (departamento_dirigido, area_solicitante, nombre_y_firma, fecha, descripcion_problema)

        # Execute the query
        cursor.execute(insert_query, data)
        
        # Generar el PDF
        self.generar_pdf(folio, departamento_dirigido, area_solicitante, nombre_y_firma, fecha, descripcion_problema, pdf_new_path)

        # Confirm the transaction and close the connection
        connection.commit()
        connection.close()
        
    def get_next_id(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Enter your MySQL password
            database="sistema_administrativo"
            )
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) + 1 FROM solicitud_mantenimiento")
        next_id = cursor.fetchone()[0]
        connection.close()
        return next_id if next_id is not None else 1
        
    def generar_pdf(self, folio, departamento_dirigido, area_solicitante, nombre_y_firma, fecha, descripcion_problema, pdf_new_path):
        # Ruta del archivo PDF existente
        pdf_existing_path = "FORMATOS/TecNM-AD-PO-001-02.pdf"

        # Crear un objeto PdfWriter para el nuevo archivo PDF
        pdf_writer = PdfWriter()

        # Leer el archivo PDF existente
        pdf_reader = PdfReader(pdf_existing_path)

        # Obtener el número de páginas en el PDF existente
        num_pages = len(pdf_reader.pages)
        
        def dividir_texto(texto, longitud_maxima=30):
            palabras = texto.split()
            lineas = []
            linea_actual = ''
            for palabra in palabras:
                if len(linea_actual) + len(palabra) <= longitud_maxima:
                    linea_actual += ' ' + palabra
                else:
                    lineas.append(linea_actual.strip())
                    linea_actual = palabra
            lineas.append(linea_actual.strip())
            return lineas

        # Iterar a través de cada página del PDF existente
        for page_num in range(num_pages):
            # Crear un lienzo para la página actual
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(612, 792))

            # Agregar contenido al lienzo
            can.drawString(445, 582, folio)
            can.drawString(250, 608, departamento_dirigido)
            can.drawString(160, 545, area_solicitante)
            can.drawString(65, 480, nombre_y_firma)
            can.drawString(65, 435, fecha)
            # Iterar sobre las líneas del trabajo realizado y agregarlas al lienzo
            lineas_problema = dividir_texto(descripcion_problema)
            y_position = 375
            for linea in lineas_problema:
                can.drawString(65, y_position, linea)
                y_position -= 14  # Incremento fijo para el espaciado entre líneas

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

    def retranslateUi(self, RealizarSolicitud):
        _translate = QtCore.QCoreApplication.translate
        RealizarSolicitud.setWindowTitle(_translate("RealizarSolicitud", "Realizar Solicitud"))
        self.label_20.setText(_translate("RealizarSolicitud", "Folio:"))
        self.label_21.setText(_translate("RealizarSolicitud", "Departamento al que se dirige la solicitud: "))
        self.label_22.setText(_translate("RealizarSolicitud", "Área solicitante: "))
        self.label_23.setText(_translate("RealizarSolicitud", "Fecha de elaboración:"))
        self.label_24.setText(_translate("RealizarSolicitud", "Nombre y firma del solicitante:"))
        self.label_25.setText(_translate("RealizarSolicitud", "Descripción del servicio o falla a reparar:"))
        self.textEdit_2.setHtml(_translate("RealizarSolicitud", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("RealizarSolicitud", "Regresar"))
        self.pushButton_4.setText(_translate("RealizarSolicitud", "Guardar y Generar Reporte"))
        
        # List of QDateEdit widgets
        date_edit_widgets = [self.dateEdit_7]

        # Set the default date to the current date for all QDateEdit widgets
        for date_edit in date_edit_widgets:
            date_edit.setDate(QtCore.QDate.currentDate())

    def retranslateUi(self, RealizarSolicitud):
        _translate = QtCore.QCoreApplication.translate
        RealizarSolicitud.setWindowTitle(_translate("RealizarSolicitud", "Realizar Solicitud"))
        self.label_20.setText(_translate("RealizarSolicitud", "Folio:"))
        self.label_21.setText(_translate("RealizarSolicitud", "Departamento al que se dirige la solicitud: "))
        self.label_22.setText(_translate("RealizarSolicitud", "Área solicitante: "))
        self.label_23.setText(_translate("RealizarSolicitud", "Fecha de elaboración:"))
        self.label_24.setText(_translate("RealizarSolicitud", "Nombre y firma del solicitante:"))
        self.label_25.setText(_translate("RealizarSolicitud", "Descripción del servicio o falla a reparar:"))
        self.textEdit_2.setHtml(_translate("RealizarSolicitud", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("RealizarSolicitud", "Regresar"))
        self.pushButton_4.setText(_translate("RealizarSolicitud", "Guardar y Generar Reporte"))
        
        # List of QDateEdit widgets
        date_edit_widgets = [self.dateEdit_7]

        # Set the default date to the current date for all QDateEdit widgets
        for date_edit in date_edit_widgets:
            date_edit.setDate(QtCore.QDate.currentDate())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RealizarSolicitud = QtWidgets.QMainWindow()
    ui = Ui_RealizarSolicitud()
    ui.setupUi(RealizarSolicitud)
    RealizarSolicitud.show()
    sys.exit(app.exec_())

