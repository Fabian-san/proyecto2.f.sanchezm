from db import db
from funciones import es_sano

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    calorias = db.Column(db.Integer, nullable = False)
    contador_inventario = db.Column(db.Float, nullable = False)
    es_vegetariano = db.Column(db.Boolean, nullable = False)
    sabor = db.Column(db.String(50))
    tipo_ingrediente = db.Column(db.String(20), nullable = False)
    id_heladeria = db.Column(db.Integer, db.ForeignKey('heladerias.id'))
    # id_producto = db.Column(db.Integer, db.ForeignKey('productos.id')) #uno a muchos 

    def es_sano(self) -> bool:
        return es_sano(self.calorias,self.es_vegetariano)

    def abastecer(self):
        if self.tipo_ingrediente == 'base':
            self.contador_inventario += 5
        else:
            self.contador_inventario += 10

    def rotacion_ingrediente(self):
        if self.tipo_ingrediente == 'complemento':
            self.contador_inventario = 0.0

