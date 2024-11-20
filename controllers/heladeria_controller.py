from models.heladeria import Heladeria
from models.producto import Producto
from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import db

heladeria_bp = Blueprint('heladeria_bp',__name__, url_prefix='/vender')

@heladeria_bp.route('/', methods=["GET", "POST"])
def vender():
    if request.method == 'GET':
        return render_template('vender.html')
    else:
        response = request.form['producto']
        # producto_vender = Producto.query.filter_by(nombre=response).first()
        heladeria = Heladeria.query.filter_by(id=1).first()
        resultado = heladeria.vender(response)
        flash(resultado)
        
        if resultado:
            db.session.commit()
            #return 'vendido'
            return redirect(url_for('heladeria_bp.vender'))
        else:
            return redirect(url_for('heladeria_bp.vender'))
    