from flask import render_template, redirect, url_for, flash
from app.productos import productos
import app
import os
from .forms import NewProductForm, EditProductForm

# Ruta de productos
@productos.route('/create', methods = ['GET', 'POST'])
def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        # Subir imagen a carpeta de imagenes
        # Campo de imagen (filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + '/app/productos/imagenes/' + p.imagen))
        
        flash('Producto registrado con éxito')
        return redirect(url_for('productos.listar'))
    return render_template('new.html', form = form)


@productos.route('/listar')
def listar():
    productos = app.models.Producto.query.all()
    return render_template("listar.html", productos = productos)

@productos.route('/update/<id_producto>', methods = ['GET', 'POST'])
def actualizar(id_producto):
    p = app.models.Producto.query.get(id_producto)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Producto actualizado')
        return redirect('productos/listar')
    return render_template('new.html', form = form)

@productos.route('/delete/<id_producto>')
def eliminar(id_producto):
    p = app.models.Producto.query.get(id_producto)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Producto eliminado')
    return 'Aqui vamos a eliminar productos con el id ' + id_producto

#Ruta de clientes