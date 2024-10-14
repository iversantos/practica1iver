from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

# Ruta para la página de inicio
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# Ruta para la página "Quiénes Somos"
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Ruta para la página de servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para la página de noticias
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Ruta para la página de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje = None
    nombre = None

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje_usuario = request.form['mensaje']

        # Validar que los campos no estén vacíos
        if not nombre or not email or not mensaje_usuario:
            mensaje = 'Todos los campos son obligatorios'
        else:
            mensaje = f"Gracias {nombre}, hemos recibido tu mensaje."

    return render_template('contacto.html', mensaje=mensaje, nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)