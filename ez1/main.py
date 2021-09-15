from flask import Flask, app, render_template, json
from Include.Modelo.UsuariosDAO import UsuariosDAO

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bienvenidos todos</h1>"

if __name__ == "__main__":
    app.run()