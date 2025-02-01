from flask_login import UserMixin
from app import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<Usuario {self.username}>"

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    cantidad_stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    proveedor = db.Column(db.String(100), nullable=False)
    fecha_entrada = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'
