from flask import render_template, redirect, url_for, flash
from app.productos import productos
import app
import os
from .forms import NewUserForm, EditUserForm

# Ruta de productos
@productos.route('/registrate', methods = ['GET', 'POST'])
def crear():
    p = app.models.Usuario()
    form = NewUserForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        # Subir imagen a carpeta de imagenes
        # Campo de imagen (filestorage)
    
        flash('Usuario registrado con éxito')
        #return redirect(url_for('usuarios.listar'))
    return render_template('new.html', form = form)


@usuarios.route('/consultate')
def listar():
    usuarios = app.models.Usuario.query.all()
    return render_template("consultar.html", usuarios = usuarios)

@usuarios.route('/update/<id_producto>', methods = ['GET', 'POST'])
def actualizar(id_user):
    p = app.models.Usuario.query.get(id_user)
    form = EditUserForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Usuario actualizado')
        return redirect('usuarios/consultar')
    return render_template('new.html', form = form)

@productos.route('/delete/<id_producto>')
def eliminar(id_user):
    p = app.models.Usuario.query.get(id_user)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Usuario eliminado')
    return 'Se eliminó el usuario del id:  ' + id_user

#Ruta de clientes