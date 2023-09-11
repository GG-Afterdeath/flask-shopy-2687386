from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class UserForm():
    nombre = StringField("Nombre del usuario:", validators = [InputRequired(message= 'Este campo es obligatorio')])
    email = EmailField("Correo del usuario:", validators = [InputRequired(message= 'El campo del correo es obligatorio'), Email(message='Correo inválido')])
    password = PasswordField("Contraseña:", validators = [InputRequired(message= 'Campo de contraseña obligatorio'), Length(min = 8, max = 30)])

class NewUserForm(FlaskForm, UserForm):
    submit = SubmitField("Registrar usuario")
    
class EditUserForm(FlaskForm, UserForm):
    submit = SubmitField("Actualizar usuario")
