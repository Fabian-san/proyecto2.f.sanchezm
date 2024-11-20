from flask import Flask, render_template
from os import getenv
from dotenv import load_dotenv
from db import db, init_db
from models.producto import Producto
from models.ingrediente import Ingrediente
from models.heladeria import Heladeria
from controllers.producto_controller import producto_bp
from controllers.heladeria_controller import heladeria_bp
from controllers.ingrediente_controller import ingrediente_bp
import secrets

load_dotenv()

app = Flask(__name__, template_folder='views')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootadmin123*@localhost/proyecto_heladeria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

db.init_app(app)

def cargar_datos():

    # Creando la heladería
    heladeria = Heladeria('Heladería Don Fabian')

    # Creando los productos
    fresa_explosion  = Producto(nombre="Fresa Explosión", precio_publico=7000, tipo_vaso="Vaso de plástico", volumen=None, tipo_producto='copa')
    delicia_mandarina = Producto(nombre="Delicia de Mandarina", precio_publico=6500, tipo_vaso="Vaso de vidrio", volumen=None, tipo_producto='copa')
    galaxia_chocolate = Producto(nombre="Galaxia de Chocolate", precio_publico=14000, tipo_vaso=None, volumen=300.0, tipo_producto='malteada')
    exposion_emo = Producto(nombre="Explosion de Emociones",precio_publico= 7500, tipo_vaso="Vaso de plástico", tipo_producto='copa', volumen=None)

    # Creando los ingredientes
    helado_fresa = Ingrediente(nombre="Helado de Fresa", precio=2000, calorias=150, contador_inventario=5.0, es_vegetariano=False, sabor="Fresa", tipo_ingrediente='base')
    helado_vainilla = Ingrediente(nombre="Helado de Vainilla", precio=2200, calorias=180, contador_inventario=10.0, es_vegetariano=False, sabor="Mandarina", tipo_ingrediente='base')
    helado_yogurt = Ingrediente(nombre="Helado de Yogurt", precio=1000, calorias=70, contador_inventario=3.0, es_vegetariano=False, sabor="Chocolate", tipo_ingrediente='base')
    mms = Ingrediente(nombre="Chocolates M&M´S", precio=1500, calorias=250, contador_inventario=15.0, es_vegetariano=True, tipo_ingrediente='complemento')
    mani = Ingrediente(nombre="Crema de Mani", precio=1200, calorias=50, contador_inventario=1.0, es_vegetariano=False, tipo_ingrediente='complemento')
    trozos = Ingrediente(nombre="Trozos de frutos rojos", precio=800, calorias=30, contador_inventario=5.0, es_vegetariano=False, tipo_ingrediente='complemento')

    # Asociando ingredientes a los productos
    fresa_explosion .ingredientes.append(helado_fresa)
    fresa_explosion .ingredientes.append(helado_yogurt)
    fresa_explosion .ingredientes.append(mms)

    delicia_mandarina.ingredientes.append(helado_vainilla)
    delicia_mandarina.ingredientes.append(helado_yogurt)
    delicia_mandarina.ingredientes.append(mms)

    galaxia_chocolate.ingredientes.append(helado_fresa)
    galaxia_chocolate.ingredientes.append(mani)
    galaxia_chocolate.ingredientes.append(helado_yogurt)

    exposion_emo.ingredientes.append(helado_vainilla)
    exposion_emo.ingredientes.append(helado_yogurt)
    exposion_emo.ingredientes.append(trozos)

    # Asociando ingredientes a la heladería
    heladeria.ingredientes.append(helado_fresa)
    heladeria.ingredientes.append(helado_vainilla)
    heladeria.ingredientes.append(helado_yogurt)
    heladeria.ingredientes.append(mms)
    heladeria.ingredientes.append(mani)

    # Asociando productos a la heladería
    heladeria.productos.append(fresa_explosion )
    heladeria.productos.append(delicia_mandarina)
    heladeria.productos.append(galaxia_chocolate)
    heladeria.productos.append(exposion_emo)

    # Commit
    db.session.add(heladeria)
    db.session.add_all([fresa_explosion , delicia_mandarina, galaxia_chocolate, exposion_emo]) 
    db.session.add_all([helado_fresa, helado_vainilla, helado_yogurt, mms, mani, trozos])
    db.session.commit()

@app.route('/')
def index():

    init_db(app)
    cargar_datos()

    heladeria = Heladeria.query.get(1)

    return render_template('index.html', heladeria=heladeria)

app.register_blueprint(producto_bp)
app.register_blueprint(heladeria_bp)
app.register_blueprint(ingrediente_bp)

if __name__ == '__main__':
    app.run(debug=True)

# los ingredientes deben compartirse entre todos los productos de la heladería
