from flask import Blueprint, render_template
from . import db
bp = Blueprint('artista', __name__, '/artistas')


@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM artists
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("artistas.html",artistas=lista_de_resultado)