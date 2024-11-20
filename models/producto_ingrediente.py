from db import db

producto_ingrediente = db.Table(
    'producto_ingrediente',
    db.Column('id_producto', db.Integer, db.ForeignKey('productos.id')),
    db.Column('id_ingrediente', db.Integer, db.ForeignKey('ingredientes.id'))
)

