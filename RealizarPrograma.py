from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog
import io

class Ui_RealizarPrograma(object):
    def setupUi(self, RealizarPrograma):
        RealizarPrograma.setObjectName("RealizarPrograma")
        RealizarPrograma.resize(1115, 600)
        RealizarPrograma.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RealizarPrograma)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 70, 221, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 30, 221, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 70, 221, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(700, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 70, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(950, 30, 101, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_3.setGeometry(QtCore.QRect(950, 70, 101, 22))
        self.dateEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 120, 1051, 401))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(15)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(14, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(68)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 550, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 550, 321, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_semestre = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_semestre.setGeometry(QtCore.QRect(130, 30, 221, 22))
        self.comboBox_semestre.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_semestre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_semestre.setObjectName("comboBox_semestre")
        self.comboBox_semestre.addItem("")
        self.comboBox_semestre.addItem("")
        RealizarPrograma.setCentralWidget(self.centralwidget)

        self.retranslateUi(RealizarPrograma)
        QtCore.QMetaObject.connectSlotsByName(RealizarPrograma)
        
        self.pushButton_3.clicked.connect(lambda:self.regresar(RealizarPrograma))
        
        # Connect the button click event to the guardar_datos method
        self.pushButton_4.clicked.connect(self.guardar_datos)
        
        # List of QLineEdit widgets
        self.line_edits = [self.comboBox_semestre, self.lineEdit_4, self.lineEdit_5, self.lineEdit_6]
        
    def regresar(self, main_window):
        from ElaborarProgramadeMantenimientoPreventivo import Ui_MainWindow as Ui_ElaborarProgramaDeMantenimiento
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_ElaborarProgramaDeMantenimiento()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def obtener_texto_celda(self, fila, columna):
    # Obtener texto de una celda de la tabla
        item = self.tableWidget_3.item(fila, columna)
        if item is not None:
            return item.text()
        return ""
        
    def guardar_datos(self):
        # Obtener datos de los QLineEdit
        semestre = self.comboBox_semestre.currentText()
        elaboro = self.lineEdit_4.text()
        anio = self.lineEdit_5.text()
        aprobo = self.lineEdit_6.text()

        # Obtener datos de los QDateEdit
        fecha_aprobacion = self.dateEdit_3.date().toString("yyyy-MM-dd")
        
        numero = self.obtener_texto_celda(0,0)
        servicio = self.obtener_texto_celda(0,1)
        tipo = self.obtener_texto_celda(0,2)
        Ee = self.obtener_texto_celda(0,3)
        
        # Obtener la ruta y el nombre del archivo mediante un cuadro de diálogo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_new_path, _ = QFileDialog.getSaveFileName(self.centralwidget, "Guardar PDF", "", "Archivos PDF (*.pdf);;Todos los archivos (*)", options=options)

    # Verificar si el usuario canceló la operación
        if pdf_new_path:
        # Generar el PDF
            self.generar_pdf(semestre, anio, fecha_aprobacion, elaboro, aprobo, numero, servicio, tipo, Ee, pdf_new_path)

        # Configurar la conexión a la base de datos
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='sistema_administrativo'
            )

            cursor = connection.cursor()

            # Ejecutar la consulta de inserción
            insert_query = "INSERT INTO programas_realizados (Semestre, Año, Fecha, Elaboro, Aprobo, Numero, Servicio, Tipo, E) " \
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (semestre, anio, fecha_aprobacion, elaboro, aprobo, numero, servicio, tipo, Ee)
            cursor.execute(insert_query, data)

            # Confirmar la transacción y cerrar la conexión
            connection.commit()
            connection.close()

            print("Datos guardados correctamente en la base de datos.")

        except Exception as e:
            print("Error al intentar guardar los datos:", str(e))
            
    def generar_pdf(self, semestre, anio, fecha_aprobacion, elaboro, aprobo, numero, servicio, tipo, Ee, pdf_new_path):
        # Ruta del nuevo archivo PDF que se generará
        pdf_existing_path = "Formatos/TecNM-AD-PO-001-03.pdf"

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

            # Aquí es donde puedes agregar tu contenido al lienzo
            can.drawString(155, 465,semestre)
            can.drawString(435, 465,anio)
            can.drawString(200, 100,fecha_aprobacion)
            can.drawString(200, 125,fecha_aprobacion)
            can.drawString(475, 100,elaboro)
            can.drawString(475, 125,aprobo)
            can.drawString(60, 415,numero)
            
            # Iterar sobre las líneas del trabajo realizado y agregarlas al lienzo
            lineas_servicio = dividir_texto(servicio)
            y_position = 420
            for linea in lineas_servicio:
                can.drawString(85, y_position, linea)
                y_position -= 14
            
            can.drawString(295, 420,tipo)
            can.drawString(400, 420, Ee)

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


    def retranslateUi(self, RealizarPrograma):
        _translate = QtCore.QCoreApplication.translate
        RealizarPrograma.setWindowTitle(_translate("RealizarPrograma", "Realizar Programa de Mantenimiento"))
        self.label_4.setText(_translate("RealizarPrograma", "Semestre:"))
        self.label_5.setText(_translate("RealizarPrograma", "Elaboró:"))
        self.label_6.setText(_translate("RealizarPrograma", "Año:"))
        self.label_7.setText(_translate("RealizarPrograma", "Aprobó:"))
        self.label_8.setText(_translate("RealizarPrograma", "Fecha de elaboración:"))
        self.label_9.setText(_translate("RealizarPrograma", "Fecha de elaboración:"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("RealizarPrograma", "No."))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("RealizarPrograma", "Servicio"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("RealizarPrograma", "Tipo"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("RealizarPrograma", "E"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("RealizarPrograma", "Ene"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("RealizarPrograma", "Mar"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("RealizarPrograma", "Abr"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("RealizarPrograma", "May"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("RealizarPrograma", "Jun"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("RealizarPrograma", "Jul"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("RealizarPrograma", "Ago"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("RealizarPrograma", "Sep"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("RealizarPrograma", "Oct"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("RealizarPrograma", "Nov"))
        item = self.tableWidget_3.horizontalHeaderItem(14)
        item.setText(_translate("RealizarPrograma", "Dic"))
        self.pushButton_3.setText(_translate("RealizarPrograma", "Regresar"))
        self.pushButton_4.setText(_translate("RealizarPrograma", "Guardar y Generar Reporte"))
        self.comboBox_semestre.setItemText(0, _translate("RealizarPrograma", "Enero - Junio"))
        self.comboBox_semestre.setItemText(1, _translate("RealizarPrograma", "Agosto - Diciembre"))
        
        # List of QDateEdit widgets
        date_edit_widgets = [self.dateEdit_2, self.dateEdit_3]

        # Set the default date to the current date for all QDateEdit widgets
        for date_edit in date_edit_widgets:
            date_edit.setDate(QtCore.QDate.currentDate())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RealizarPrograma = QtWidgets.QMainWindow()
    ui = Ui_RealizarPrograma()
    ui.setupUi(RealizarPrograma)
    RealizarPrograma.show()
    sys.exit(app.exec_())
