import unittest
from models.ingrediente import Ingrediente
from models.producto import Producto
from models.heladeria import Heladeria


class test_heladeria(unittest.TestCase):
    def test_es_sano(self):
        test_ingrediente1 = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base') 
        self.assertTrue(test_ingrediente1.es_sano(),"Correcto")
        
    def test_abastecer(self):
        test_abastecer = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base')
        self.assertNotIn(test_abastecer.abastecer())
    
    def test_Renovar(self):
        test_Renovar = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base')
        self.assertIsInstance(test_Renovar.rotacion_ingrediente(),str)
        
    def test_calorias(self):
        test_calorias = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base')
        self.assertFalse(test_calorias.calorias(),"Correcto")
    
    def test_costo(self):
        test_costo = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base')
        self.assertEqual()
         
    def test_rentabilidad(self):
        test_rentabilidad =  Producto(nombre="Fresa Explosión", precio_publico=7000, tipo_vaso="Vaso de plástico", volumen=None, tipo_producto='copa')
        self.assertIsInstance(test_rentabilidad.calcular_rentabilidad,str)

    def test_mas_rentable(self):
        prod_1 = Producto(nombre="Fresa Explosión", precio_publico=7000, tipo_vaso="Vaso de plástico", volumen=None, tipo_producto='copa')
        prod_2 = Producto(nombre="Delicia de Mandarina", precio_publico=6500, tipo_vaso="Vaso de vidrio", volumen=None, tipo_producto='copa')
        prod_3 = Producto(nombre="Galaxia de Chocolate", precio_publico=14000, tipo_vaso=None, volumen=300.0, tipo_producto='malteada')
        heladeria = Heladeria('Heladería Don Fabian')
        heladeria.productos.append(prod_1 )
        heladeria.productos.append(prod_2)
        heladeria.productos.append(prod_3)
        self.assertIsInstance(heladeria.mas_rentable(prod_1,prod_2,prod_3),str)
        

