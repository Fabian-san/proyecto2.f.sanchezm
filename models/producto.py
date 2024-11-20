from db import db
from sqlalchemy.orm import relationship
from models.iproducto import IProducto
from models.producto_ingrediente import producto_ingrediente
from funciones import costos, calcular_calorias, rentabilidad

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    precio_publico = db.Column(db.Integer, nullable = False)
    tipo_vaso = db.Column(db.String(50))
    volumen = db.Column(db.Float)
    tipo_producto = db.Column(db.String(10), nullable = False)
    id_heladeria = db.Column(db.Integer, db.ForeignKey('heladerias.id'))
    # ingredientes = relationship('Ingrediente', backref='producto') uno a muchos
    ingredientes = relationship('Ingrediente',secondary=producto_ingrediente, backref='producto') #muchos a muchos

    def calcular_costo(self,ingrediente_1:dict,ingrediente_2:dict,ingrediente_3:dict)->int:
        return costos(ingrediente_1,ingrediente_2,ingrediente_3)+500

    def calcular_calorias(self,lista_calorias:list):
        return calcular_calorias(lista_calorias)+200
    
    def calcular_rentabilidad(self,ingrediente_1:dict,ingrediente_2:dict,ingrediente_3:dict):
        return rentabilidad(self.precio_publico,ingrediente_1,ingrediente_2,ingrediente_3)
    