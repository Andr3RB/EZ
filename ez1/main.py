from Include.Modelo.ArticulosDAO import ArticulosDAO
from flask import Flask, app, render_template, json, request
#from Include.Modelo.UsuariosDAO import UsuariosDAO
from flaskext.mysql import MySQL
import Include.conexion as cnx 


app = Flask(__name__,static_url_path='',static_folder='static/')

@app.route("/") ##Ruta
def main():
    return render_template('Home.html')


# #@app.route("/LoginC", methods = ['POST'])
#     def LoginC():
#    db = MySQL
#     cursor = db.cursor()
#     sql = "INSERT INTO Usuarios(correo, contrasena) VALUES ("+request.args.get('correo')+", "+request.args.get('contrasena')+")"
#     try:
# #       if request.method == 'POST': 
# #            adao = ArticulosDAO()
# #            lvo = adao.selectALL()
#             cursor.execute(sql)
#             db.commit()
#             return render_template('LoginComprador.html')##eventos=lvo)
# #        else:
# #            return render_template('interfazC.html')
#     except Exception as e:
#         return json.dumps({'error':str(e)})

@app.route("/LoginC", methods = ['POST'])
def LoginC():
            return render_template('LoginComprador.html')


@app.route("/LoginV", methods = ['POST'])
def LoginV():
    try:
        if request.method == 'POST': 
#            adao = ArticulosDAO()
#            lvo = adao.selectALL()
            return render_template('LoginComprador.html')##,eventos=lvo)
        else:
            return render_template('interfazV.html')
    except Exception as e:
        return json.dumps({'error':str(e)})

# @app.route("/LoginC/interfazC", methods = ['POST'])
# def InterfazC():
#     try:
#         if request.method == 'POST': 
# #            adao = ArticulosDAO()
# #            lvo = adao.selectALL()
#             return render_template('interfazC.html')##eventos=lvo)
#         else:
#             return render_template('interfazC.html')
#     except Exception as e:
#         return json.dumps({'error':str(e)})

@app.route("/registuser", methods = ['POST'])
def registuser():
        try:
             correo=request.form['correo']
             print(correo)
             contrasena=request.form['contrasena']
             conn=cnx.mysql.connect()
             cursor=conn.cursor()
             cursor.execute("INSERT INTO Usuarios(correo, contrasena) VALUES (%s, %s)",(correo, contrasena,)) #Este insert debe ir en el DAO 
             return render_template('LoginComprador.html')
        except Exception as e:
         return json.dumps({'error':str(e)})

@app.route("/interfazV", methods = ['POST']) ##con esta ruta enviaremos después del login a interfaz vendedor
def InterfazV():
    try:
        if request.method == 'POST': 
#            adao = ArticulosDAO()
#            lvo = adao.selectALL()
            return render_template('interfazV.html')##,eventos=lvo)
        else:
            return render_template('interfazV.html')
    except Exception as e:
        return json.dumps({'error':str(e)})


if __name__ == "__main__":
    app.run()

