from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from user import users, get_user, User, get_user_from_email, get_user_from_id
from werkzeug.utils import secure_filename
import os
from functions import obtener_ambiente_por_id

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = "devDynamo"

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = get_user(request.form['username'])
        if user and user.check_password(request.form['password']):
            login_user(user, remember=True)
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        succesful = True
        if get_user(request.form['username']):
            flash("Username already taken")
            succesful = False
        if get_user_from_email(request.form['email']):
            flash("Email is already used by other account")
            succesful = False
        if request.form['password'] != request.form['password-repeat']:
            flash("Both passwords must be the same")
            succesful = False
        if succesful:
            newUser = User(str(len(users)), request.form['username'], request.form['email'], request.form['password'])
            users.append(newUser)
            login_user(newUser, remember=True)
            return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/agregar_ambiente', methods=['GET', 'POST'])
@login_required  # Requiere que el usuario esté autenticado como administrador
def crear_ambiente():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        capacidad = request.form['capacidad']
        ubicacion = request.form['ubicacion']
        descripcion = request.form['descripcion']
        # Agregar lógica para manejar la creación de ambiente en la base de datos

        # Después de crear el ambiente, redirigir a la página de confirmación o inicio
        return redirect(url_for('index'))
    return render_template('agregar_ambiente.html')

@app.route('/editar_ambiente/<ambiente_id>', methods=['GET', 'POST'])
@login_required  # Requiere que el usuario esté autenticado como administrador
def editar_ambiente(ambiente_id):
    # Agregar lógica para cargar los datos del ambiente a editar
    ambiente = obtener_ambiente_por_id(ambiente_id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        capacidad = request.form['capacidad']
        ubicacion = request.form['ubicacion']
        descripcion = request.form['descripcion']
        # Agregar lógica para manejar la edición del ambiente en la base de datos

        # Después de editar el ambiente, redirigir a la página de confirmación o inicio
        return redirect(url_for('index'))

    return render_template('editar_ambiente.html', ambiente=ambiente)

@app.route('/actividades/')
def actividades():
    return render_template('actividades.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)