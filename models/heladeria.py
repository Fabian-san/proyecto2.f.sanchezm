from db import db
from sqlalchemy.orm import relationship
from funciones import mas_rentable
from flask import flash

class Heladeria(db.Model):
    __tablename__ = 'heladerias'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    venta_dia = db.Column(db.Integer, default=0)
    productos = relationship('Producto', backref='heladeria')
    ingredientes = relationship('Ingrediente', backref='heladeria')

    def __init__(self, nombre:str) -> None:
        super().__init__()
        self.nombre = nombre
          
    def vender(self,nombre_producto:str):
        existe = 0
        producto_validar=""
        for a in self.productos:
            if nombre_producto == a.nombre:
                producto_validar = a
                existe=1
        if existe == 0:
            return "El producto no existe !" 
        # 1 de cada complemento
        # 0.2 de base
        venta = 0
        for b in producto_validar.ingredientes:
            if b.tipo_ingrediente=="complemento":
                if b.contador_inventario>=1:
                    venta = 1
                else:
                    venta = 0
                    return  f"No hay suficientes ingredientes de ({b.nombre}) para este producto!\n" + "False"
                    
            elif b.tipo_ingrediente=="base":
                if b.contador_inventario>=0.2:
                    venta = 1
                else:
                    venta = 0
                    return f"No hay suficientes ingredientes de ({b.nombre}) para este producto!\n" + "False"
        if venta == 0:
            return "No hay suficientes ingredientes para este producto!" 

        if existe == 1 and  venta == 1:
            for c in producto_validar.ingredientes:
                if b.tipo_ingrediente=="complemento":
                    c.contador_inventario-=0.2
                else:
                    c.contador_inventario-=1
            self.venta_dia+=producto_validar.precio_publico 
            
            return True
        else:
            return False
        
    def mas_rentable(self,producto_1:dict,producto_2:dict,producto_3:dict,producto_4:dict)->str:
        mas_rentable(producto_1,producto_2,producto_3,producto_4)

    # def producto_mas_rentable(self):
    #     producto1 = {
    #                     "nombre" : self.productos[0].nombre,
    #                     "rentabilidad" : self.productos[0].calcular_rentabilidad()
    #                      }
        
    #     producto2 = {
    #                     "nombre" : self.productos[1].nombre,
    #                     "rentabilidad" : self.productos[1].calcular_rentabilidad()
    #                      }
        
    #     producto3 = {
    #                     "nombre" : self.productos[2].nombre,
    #                     "rentabilidad" : self.productos[2].calcular_rentabilidad()
    #                      }
        
    #     producto4 = {
    #                     "nombre" : self.productos[3].nombre,
    #                     "rentabilidad" : self.productos[3].calcular_rentabilidad()
    #                      }

    #     return producto_mas_rentable(producto1, producto2, producto3, producto4)
    
    def ventas_del_dia(self):
        return self.venta_dia
    
    # def vender(self, producto_vender:str) -> bool:
    #     existe_producto = ""
    #     for producto in self.productos:
    #         if producto.nombre == producto_vender:
    #             existe_producto = producto
        
    #     if not existe_producto:
    #         flash ("El producto no existe", category='error')
    #         return False
        
    #     for ingrediente in existe_producto.ingredientes:
    #         if ingrediente.tipo == 'base':
    #             if ingrediente.inventario < 0.2:
    #                 flash(f"No hay suficientes ingredientes ({ingrediente.nombre})", category='error')
    #                 return False
    #         elif ingrediente.tipo == 'complemento':
    #             if ingrediente.inventario < 1:
    #                 flash(f"No hay suficientes ingredientes ({ingrediente.nombre})", category='error')
    #                 return False
                
    #     for ingrediente in existe_producto.ingredientes:
    #         if ingrediente.tipo == 'base':
    #             ingrediente.inventario -= 0.2
    #         elif ingrediente.tipo == 'complemento':
    #             ingrediente.inventario -= 1

    #     self.venta_dia += existe_producto.precio_publico
    #     return True