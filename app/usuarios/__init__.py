from flask import Blueprint

usuarios = Blueprint('usuarios',
                      __name__,
                      url_prefix= "/usuarios",
                      template_folder= 'templates'
                      )

# El punto es para importar todo lo que haya en routes
from . import routes