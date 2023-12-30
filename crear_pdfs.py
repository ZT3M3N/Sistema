from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io

# Ruta del archivo PDF existente
pdf_existing_path = "C:\\Users\\stejo\\OneDrive\\Escritorio\\Administrativo\\TecNM-AD-PO-001-02.pdf"

# Ruta del nuevo archivo PDF que se generará
pdf_new_path = "C:\\Users\\stejo\\OneDrive\\Escritorio\\Administrativo\\nuevo_archivo.pdf"

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
    can = canvas.Canvas(packet, pagesize=(612,792))
    
    # Aquí es donde puedes agregar tu contenido al lienzo
    can.drawString(350, 648,  "Biblioteca")
    can.drawString(350, 630,  "Penjamo")
    
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
