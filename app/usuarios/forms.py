from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, EmailField, PasswordField
from wtforms.validators import InputRequired, NumberRange


class UserForm():
    nombre = StringField("Nombre del usuario:", validators = [InputRequired(message= 'Este campo es obligatorio')])
    correo = EmailField("Correo del usuario:", validators = [InputRequired(message= 'El campo del correo es obligatorio')])
    password = PasswordField("Contraseña:", validators = [InputRequired(message= 'Campo de contraseña obligatorio')])

class NewUserForm(FlaskForm, UserForm):
    submit = SubmitField("Registrar usuario")
    
class EditUserForm(FlaskForm, ProductForm):
    submit = SubmitField("Actualizar usuario")
