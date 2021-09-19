from flask import Flask, app, render_template, json
from Include.modelo.UsuariosDAO import UsuariosDAO

app = Flask(_name_)

@app.route("/")
def index():
    return "<h1>Bienvenidos todos</h1>"

if _name_ == "_main_":
    app.run()