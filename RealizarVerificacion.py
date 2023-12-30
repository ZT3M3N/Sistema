from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io


class Ui_RealizarVerificacion(object):
    def setupUi(self, RealizarVerificacion):
        RealizarVerificacion.setObjectName("RealizarVerificacion")
        RealizarVerificacion.resize(1127, 667)
        RealizarVerificacion.setStyleSheet("QWidget{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RealizarVerificacion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 37, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 77, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(291, 41, 201, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 87, 201, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(909, 37, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(970, 40, 110, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 1051, 411))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScroll(True)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(334)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 600, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 600, 441, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        RealizarVerificacion.setCentralWidget(self.centralwidget)

        self.retranslateUi(RealizarVerificacion)
        QtCore.QMetaObject.connectSlotsByName(RealizarVerificacion)
        
        self.pushButton_4.clicked.connect(lambda:self.regresar(RealizarVerificacion))
        
        self.pushButton_5.clicked.connect(lambda: self.guardar_datos())
        

        
    def regresar(self, main_window):
        from VerificarInfraestructura import Ui_MainWindow as Ui_VerificarInfraestructura
        # Abre la ventana de servicios utilizando la referencia a la clase Ui_ServiciosAdmin
        self.back_window = QtWidgets.QMainWindow()
        ui = Ui_VerificarInfraestructura()
        ui.setupUi(self.back_window)
        self.back_window.show()
        main_window.close()
        
    def guardar_datos(self):
    # Obtener datos de la interfaz
        jefe_departamento = self.lineEdit.text()
        jefe_area = self.lineEdit_2.text()
        fecha = self.dateEdit.date().toString("yyyy-MM-dd")
        espacio_revisado = self.obtener_texto_celda(0, 0)  # Ejemplo, obtén el texto de una celda de la tabla
        hallazgos = self.obtener_texto_celda(0, 1)  # Ejemplo, obtén el texto de una celda de la tabla
        atendido = "Sí" if self.obtener_estado_atendido(0, 2) == "Sí" else "No"
        

        
    # Conectar a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema-administrativo"
    )

        cursor = connection.cursor()

    # Insertar datos en la tabla infraestructura_y_equipo
        query = ("INSERT INTO infraestructura_y_equipo "
          "(jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido) "
             "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido)

        cursor.execute(query, data)
        connection.commit()
        
        # Generar el PDF
        self.generar_pdf(jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido)

    # Cerrar la conexión
        cursor.close()
        connection.close()
        
    def generar_pdf(self, jefe_departamento, jefe_area, fecha, espacio_revisado, hallazgos, atendido):
        # Ruta del nuevo archivo PDF que se generará
        pdf_existing_path = "C:\\Users\\stejo\\OneDrive\\Escritorio\\Administrativo\\TecNM-AD-PO-001-01.pdf"

        # Ruta del nuevo archivo PDF que se generará
        pdf_new_path = "C:\\Users\\stejo\\OneDrive\\Escritorio\\Administrativo\\Realizar_Verificacion.pdf"

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

            # Aquí es donde puedes agregar tu contenido al lienzo
            can.drawString(350, 648,jefe_departamento)
            can.drawString(350, 630,jefe_area)
            can.drawString(535, 603,fecha)
            can.drawString(75, 555,espacio_revisado)
            can.drawString(205, 555,hallazgos)
            can.drawString(500, 555,atendido)

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

        
    def obtener_texto_celda(self, fila, columna):
    # Obtener texto de una celda de la tabla
        item = self.tableWidget.item(fila, columna)
        if item is not None:
            return item.text()
        return ""

    def obtener_estado_atendido(self, fila, columna):
    # Obtener el texto de una celda específica de la tabla
        item = self.tableWidget.item(fila, columna)
        if item is not None:
            return item.text()
        return ""
    
   

    def retranslateUi(self, RealizarVerificacion):
        _translate = QtCore.QCoreApplication.translate
        RealizarVerificacion.setWindowTitle(_translate("RealizarVerificacion", "Realizar Verificación"))
        self.label.setText(_translate("RealizarVerificacion", "Jefe(a) del departamento de:"))
        self.label_2.setText(_translate("RealizarVerificacion", "Jefe(a) del área verificada:"))
        self.label_3.setText(_translate("RealizarVerificacion", "Fecha:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RealizarVerificacion", "Espacio revisado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RealizarVerificacion", "Hallazgos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RealizarVerificacion", "Atendido"))
        self.pushButton_4.setText(_translate("RealizarVerificacion", "Regresar"))
        self.pushButton_5.setText(_translate("RealizarVerificacion", "Guardar y Generar Reporte"))
        
        # List of QDateEdit widgets
        date_edit_widgets = [self.dateEdit]

        # Set the default date to the current date for all QDateEdit widgets
        for date_edit in date_edit_widgets:
            date_edit.setDate(QtCore.QDate.currentDate())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RealizarVerificacion = QtWidgets.QMainWindow()
    ui = Ui_RealizarVerificacion()
    ui.setupUi(RealizarVerificacion)
    RealizarVerificacion.show()
    sys.exit(app.exec_())
