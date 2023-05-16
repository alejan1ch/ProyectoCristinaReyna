from flask import Flask, render_template, request, make_response
from fpdf import FPDF
from Supa import datos
import os
import dotenv
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
    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()

    # Agregar contenido al PDF
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, txt="Nombre: {}".format(nombre), ln=1)
    pdf.cell(0, 10, txt="Email: {}".format(email), ln=1)
    pdf.cell(0, 10, txt="Mensaje: {}".format(mensaje), ln=1)

    # Obtener los datos del buffer y crear una respuesta Flask
    response = make_response(pdf.output(dest='S').encode('latin1'))
    response.headers.set('Content-Disposition', 'attachment', filename='contacto.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == '__main__':
    app.run(debug=True)
