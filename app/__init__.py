from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

# Crea la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración
app.config.from_object('config.Config')

# Crear las instancias de la base de datos y el login manager
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Importar modelos y rutas después de la inicialización
from app import models
from app import routes

# Función user_loader para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from app.models import Usuario
    return Usuario.query.get(int(user_id))



