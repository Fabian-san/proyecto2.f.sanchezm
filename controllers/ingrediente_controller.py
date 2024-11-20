from models.ingrediente import Ingrediente
from flask import Blueprint, render_template, flash, redirect, url_for
from db import db

ingrediente_bp = Blueprint('ingrediente_bp', __name__, url_prefix='/ingrediente')

@ingrediente_bp.route('/ver_ingrediente/<int:id>')
def ver_ingredientes(id):
    ingrediente = Ingrediente.query.get(id)
    return render_template('ver_ingrediente.html', ingrediente=ingrediente)

@ingrediente_bp.route('renovar/<int:id>')
def rotacion(id):
    ingrediente = Ingrediente.query.get(id)
    ingrediente.rotacion_ingrediente()
    db.session.commit()
    flash('Rotacion exitosa!')
    return redirect(url_for('producto_bp.lista_productos'))

@ingrediente_bp.route('abastecer/<int:id>')
def abastecer(id):
    ingrediente = Ingrediente.query.get(id)
    ingrediente.abastecer()
    db.session.commit()
    flash('Abastecida exitosamente!')
    return redirect(url_for('producto_bp.lista_productos'))
    