from models.producto import Producto
from flask import Blueprint, render_template

producto_bp = Blueprint('producto_bp',__name__, url_prefix='/productos')

@producto_bp.route('/lista_productos')
def lista_productos():
    productos = Producto.query.all()
    # for producto in productos:
    #     print(f'{producto.nombre} costo = {producto.calcular_costo()}')
    #     print(f'{producto.nombre} calorias = {producto.calcular_calorias()}')
    #     print(f'{producto.nombre} rentabilidad = {producto.calcular_rentabilidad()}')
    return render_template('lista_productos.html', productos = productos)

@producto_bp.route('/ver_producto/<int:id>')
def ver_producto(id):
    producto = Producto.query.get(id)
    return render_template('ver_producto.html', producto=producto)