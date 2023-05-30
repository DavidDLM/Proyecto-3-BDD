from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Página de inicio
@app.route('/')
def home():
    # Obtener datos de las películas desde el backend
    peliculas = obtener_peliculas()

    # Obtener datos de las recomendaciones desde el backend
    recomendaciones = [...]  # Lista de recomendaciones obtenidas del backend

    return render_template('index.html', peliculas=peliculas, recomendaciones=recomendaciones)


# Página de preferencias
@app.route('/preferencias', methods=['GET', 'POST'])
def preferencias():
    if request.method == 'POST':
        # Obtener las preferencias enviadas por el formulario
        generos = request.form.getlist('generos')
        actores = request.form.getlist('actores')
        # Procesar las preferencias y guardarlas en la base de datos o en una sesión
        # Aquí puedes agregar la lógica para almacenar las preferencias en el backend
        # redirigir a la página de recomendaciones
        return redirect(url_for('recomendaciones'))
    return render_template('preferencias.html')


# Página de recomendaciones
@app.route('/recomendaciones')
def recomendaciones():
    # Aquí puedes agregar la lógica para obtener las recomendaciones del backend
    # y pasarlas a la plantilla para mostrarlas en la página de recomendaciones
    # Lista de recomendaciones obtenidas del backend
    peliculas_recomendadas = obtener_peliculas_recomendadas()
    return render_template('recomendaciones.html', peliculas=peliculas_recomendadas)


# Ruta y función de vista para la página de actores
@app.route('/actores')
def actores():
    # Lógica para obtener la lista de actores
    actores = obtener_actores()

    # Renderiza el template 'actores.html' y pasa la lista de actores como argumento
    return render_template('actores.html', actores=actores)


# Ejemplo de función para obtener la lista de actores
def obtener_actores():
    # Lógica para obtener la lista de actores desde tu base de datos o cualquier otra fuente de datos
    actores = [
        {
            'nombre': 'Actor 1',
            'nacionalidad': 'Estadounidense',
            'edad': 30,
            'genero': 'Masculino',
            'nacimiento': '01/01/1990'
        },
        {
            'nombre': 'Actor 2',
            'nacionalidad': 'Británico',
            'edad': 35,
            'genero': 'Masculino',
            'nacimiento': '15/05/1985'
        },
        {
            'nombre': 'Actor 3',
            'nacionalidad': 'Francesa',
            'edad': 28,
            'genero': 'Femenino',
            'nacimiento': '10/12/1992'
        }
    ]

    return actores


def obtener_peliculas():
    # Lógica para obtener la lista de películas desde tu base de datos o cualquier otra fuente de datos
    peliculas = [
        {
            'titulo': 'Película 1',
            'genero': 'Drama',
            'duracion': '120 minutos',
            'calificacion': 7.5,
            'año': 2022
        },
        {
            'titulo': 'Película 2',
            'genero': 'Acción',
            'duracion': '110 minutos',
            'calificacion': 8.2,
            'año': 2021
        },
        {
            'titulo': 'Película 3',
            'genero': 'Comedia',
            'duracion': '95 minutos',
            'calificacion': 6.9,
            'año': 2020
        }
    ]
    return peliculas


def obtener_peliculas_recomendadas():
    # Lógica para obtener la lista de películas recomendadas desde tu base de datos o cualquier otra fuente de datos
    peliculas_recomendadas = [
        {
            'titulo': 'Película 1',
            'genero': 'Drama',
            'duracion': '120 minutos',
            'calificacion': 7.5,
            'año': 2022
        },
        {
            'titulo': 'Película 2',
            'genero': 'Acción',
            'duracion': '110 minutos',
            'calificacion': 8.2,
            'año': 2021
        },
        {
            'titulo': 'Película 3',
            'genero': 'Comedia',
            'duracion': '95 minutos',
            'calificacion': 6.9,
            'año': 2020
        }
    ]
    return peliculas_recomendadas


if __name__ == '__main__':
    app.run(debug=True)
