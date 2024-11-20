def es_sano (calorias:int,es_vegetariano:bool)->bool:
    if calorias < 100 or es_vegetariano:
        return True
    else:
        return False
    
def calorias (calorias_list:list)->float:
    suma = 0
    for a in calorias_list:
        suma += a
    return round(suma*0.95,2)

def calcular_calorias (calorias_list:list)->float:
    suma = 0
    for a in calorias_list:
        suma += a
    return round(suma,2)

def costos (ingrediente_1:dict,ingrediente_2:dict,ingrediente_3:dict)->int:
    precio = ingrediente_1["precio"]+ingrediente_2["precio"]+ingrediente_3["precio"]
    return precio

def rentabilidad(precio_producto:int,ingrediente_1:dict,ingrediente_2:dict,ingrediente_3:dict)->int:
    rentabilidad=precio_producto-costos(ingrediente_1,ingrediente_2,ingrediente_3)
    return rentabilidad

def mas_rentable(producto_1:dict,producto_2:dict,producto_3:dict,producto_4:dict)->str:
    lista = [producto_1,producto_2,producto_3,producto_4]
    mas_rentable = ""
    valor = 0
    for producto in lista:
        if producto["rentabilidad"]> valor:
           mas_rentable = producto["nombre"]
           valor=producto["rentabilidad"]
    
    return mas_rentable
def replicate(cadena, veces):
    return cadena * veces