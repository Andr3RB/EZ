from Include.Modelo.UsuariosVO import UsuariosVO
from flask import Flask, app, render_template, json, request 
from flaskext.mysql import MySQL
import Include.conexion as cnx 

#class UsuariosDAO:
#    def __init__(self):
#        self.__tabla = "Usuarios"


#@app.route("/LoginC", methods = ['POST'])
#def LoginC():
 #           return render_template('LoginComprador.html')
# @app.route("/LoginC/registuser", methods = ['POST'])
# def registuser():
#         #try:
#             conn=cnx.mysql.connect()
#             cursor=conn.cursor()
#             cursor.execute('SELECT * FROM  Usuarios ORDER BY Id DESC')
#             prueba = cursor.fetchall()
#             print(prueba)
#             #return prueba
#             return render_template('LoginComprador.html')
        #except Exception as d:
         #   return json.dumps({'error':str(d)})
        #finally:
         #   cursor.close()
          #  conn.close()