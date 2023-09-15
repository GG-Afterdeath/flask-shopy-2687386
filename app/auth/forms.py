from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField 
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    user_name = StringField(label = 'Nombre de usuario',validators = [
        InputRequired(message= 'Validar este campo')] )
    password = PasswordField(label = 'Contraseña', validators = [
        InputRequired(message= 'Validar este campo')])
    submit = SubmitField(label = 'Iniciar sesión')
