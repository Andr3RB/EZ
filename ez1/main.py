from Include.Modelo.ArticulosDAO import ArticulosDAO
from flask import Flask, app, render_template, json, request
from Include.Modelo.UsuariosDAO import UsuariosDAO


app = Flask(__name__static_url_path='',static_folder='static/')

@app.route("/arreglo")
def arreglo():
    try:
        if request.method == 'POST': 
            dao = UsuariosDAO()
            lvo = dao.selectALL()
            return render_template('LoginComprador.html',eventos=lvo)
        else:
            return render_template('arreglo')
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run()

@app.route("/interfazC")
def interfazC():
    try:
        if request.method == 'POST': 
            adao = ArticulosDAO()
            lvo = adao.selectALL()
            return render_template('interfazC.html',eventos=lvo)
        else:
            return render_template('interfazC')
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run()

