from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user  # Asegúrate de que login_user esté importado
from app import app, db
from app.models import Producto
from app.models import Usuario
from app.forms import ProductoForm
from app.forms import LoginForm 

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Verificar si el usuario existe y la contraseña es correcta
        usuario = Usuario.query.filter_by(username=form.usuario.data).first()
        if usuario and usuario.password == form.contrasena.data:  # En producción, usar un hash para las contraseñas
            login_user(usuario)  # Iniciar sesión
            return redirect(url_for('dashboard'))
        else:
            return 'Usuario o contraseña incorrectos', 401
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()  # Cerrar sesión
    return redirect(url_for('login'))

# Ruta del dashboard, donde se gestionan los productos
@app.route('/dashboard')
@login_required
def dashboard():
    productos = Producto.query.all()
    return render_template('dashboard.html', productos=productos)

# Ruta para agregar un nuevo producto
@app.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        nuevo_producto = Producto(
            nombre=form.nombre.data,
            categoria=form.categoria.data,
            talla=form.talla.data,
            color=form.color.data,
            cantidad_stock=form.cantidad_stock.data,
            precio=form.precio.data,
            proveedor=form.proveedor.data,
            fecha_entrada=form.fecha_entrada.data,
            valor_total=form.cantidad_stock.data * form.precio.data
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('product_form.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    producto = Producto.query.get_or_404(id)  # Obtener el producto por su ID
    form = ProductoForm(obj=producto)  # Prellenar el formulario con los datos del producto
    if form.validate_on_submit():
        producto.nombre = form.nombre.data
        producto.categoria = form.categoria.data
        producto.talla = form.talla.data
        producto.color = form.color.data
        producto.cantidad_stock = form.cantidad_stock.data
        producto.precio = form.precio.data
        producto.proveedor = form.proveedor.data
        producto.fecha_entrada = form.fecha_entrada.data
        producto.valor_total = form.cantidad_stock.data * form.precio.data

        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_product.html', form=form)

@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('dashboard'))