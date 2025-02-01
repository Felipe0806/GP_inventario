from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, DateField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    categoria = SelectField('Categoría', choices=[('ropa_mujer', 'Ropa de Mujer'), ('ropa_hombre', 'Ropa de Hombre'), ('accesorios', 'Accesorios')], validators=[DataRequired()])
    talla = SelectField('Talla', choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    cantidad_stock = IntegerField('Cantidad en Stock', validators=[DataRequired()])
    precio = FloatField('Precio Unitario', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    fecha_entrada = DateField('Fecha de Entrada', validators=[DataRequired()])

