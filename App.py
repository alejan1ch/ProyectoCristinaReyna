from flask import Flask, render_template, request, make_response
from reportlab.pdfgen import canvas
from io import BytesIO
from Supa import datos
import os
import dotenv

def create_app():
    app = Flask(__name__)
    dotenv.load_dotenv()


    # Variable global para almacenar los datos
    items = []

    # Función para cargar los datos antes de cada solicitud
    @app.before_request
    def cargar_datos():
        global items
        items = datos(os.environ.get('URL'),os.environ.get('KEY'))

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/contacto', methods=['GET', 'POST'])
    def contacto():
        if request.method == 'POST':
            # Obtener los datos del formulario
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            mensaje = request.form.get('mensaje')

            # Generar el archivo PDF
            response = generate_pdf(nombre, email, mensaje)
            response.headers['Content-Disposition'] = 'attachment; filename=contacto.pdf'
            return response

        return render_template('contacto.html')

    @app.route('/catalogo')
    def catalog():
        return render_template('catalogo.html', items=items)

    def generate_pdf(nombre, email, mensaje):
        # Crear un objeto PDFCanvas
        buffer = BytesIO()
        c = canvas.Canvas(buffer)

        # Agregar contenido al PDF
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, "Nombre: {}".format(nombre))
        c.drawString(100, 680, "Email: {}".format(email))
        c.drawString(100, 660, "Mensaje: {}".format(mensaje))

        # Finalizar y guardar el PDF
        c.showPage()
        c.save()

        # Obtener los datos del buffer y crear una respuesta Flask
        buffer.seek(0)
        response = make_response(buffer.getvalue())
        response.mimetype = 'application/pdf'
        return response
    return app
