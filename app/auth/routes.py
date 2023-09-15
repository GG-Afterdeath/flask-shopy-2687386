from flask_login import login_user, current_user, logout_user
from flask import render_template, redirect, url_for, flash
from app.auth import auth
from .forms import LoginForm
import app

@auth.route('/login',
            methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #Selecciona al usuario por nombre de usuario
        u = app.models.Usuario.query.filter_by(user_name = form.user_name.data).first
        if u is None or not u.check_password(form.password.data):
            flash('Usuario o clave incorrectos')
            return redirect('auth/login')
        else:
            login_user(u, remeber=True)
            return redirect('/productos/listar')
    return render_template('login.html', form = form)

@auth.route('/logout',
            methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect('auth/login')