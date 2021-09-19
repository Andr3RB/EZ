from flask import Flask, app, render_template, json
from Include.Modelo.UsuariosDAO import UsuariosDAO

app = Flask(__name__)

@app.route("/arreglo")
def arreglo():
    try:
        dao = UsuariosDAO()
        lvo = dao.selectALL()
        print(lvo[3].getCorreo())
        return render_template('LoginComprador.html',eventos=lvo)
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run()