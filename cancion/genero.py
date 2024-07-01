from flask import Blueprint, render_template
from . import db
bp = Blueprint('genero', __name__, url_prefix='/generos')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("generos.html",generos=lista_de_resultado)
	
