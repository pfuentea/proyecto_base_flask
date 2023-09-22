from app_base import app
from flask import render_template
from app_base.models.ciudades import Ciudad

@app.route('/')
def index():
    print("entre")
    v_ciudades=Ciudad.get_all()
    return render_template("index.html", ciudades=v_ciudades, saludo="Patricio")
