from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

#modelos - entidades del proyecto
"""class Cliente(db.Model):
    # Creando las columnas de la base de datos
    __tablename__ = "clientes" # Nombre que va a tener la tabla
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(180), unique = True)
    password = db.Column(db.String(180))
    email= db.Column(db.String(180), unique = True)"""

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric( precision = 10, scale = 2 ))
    imagen = db.Column(db.String(120), unique = True)

class Ventas(db.Model):
    __tablename__= "ventas"
    id= db.Column(db.Integer,primary_key=True)
    fecha= db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id=db.Column(db.Integer, db.ForeignKey('usuarios.id'))

class Detalles(db.Model):
    __tablename__= "detalles"
    id= db.Column(db.Integer,primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id=db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

class Usuario(db.Model, UserMixin):
    __tablename__="usuarios"
    id= db.Column(db.Integer, primary_key= True)
    user_name= db.Column(db.String(128))
    email= db.Column(db.String(120))
    password= db.Column(db.String(180))

    def set_password(self, password):
        self.password = generate_password_hash(password = password)
    
    def chack_password(self, password):
        return check_password_hash(self.password, password)

# Loader traerá el id del usuario que se logeo
@login.user_loader
def load_user(id):
    return Usuario.query.get(id)