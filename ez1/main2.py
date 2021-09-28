from Include.Modelo.ArticulosDAO import ArticulosDAO
from flask import Flask, app, render_template, json, request

app = Flask(__name__,static_url_path='',static_folder='static/')

@app.route("/") ##Ruta
def index():
    return render_template('index.html', perfil=str('Daniel'))

@app.route("/shop") ##Ruta
def shop():
    return render_template('shop.html')


if __name__ == "__main__":
    app.run()