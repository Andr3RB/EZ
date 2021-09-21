from flask import json
import Include.Conexion as cnx 
from Include.modelo.UsuariosVO import UsuariosVO

class UsuariosDAO:
    def _init_(self):
        self.__tabla = "Usuarios"

    def selectALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM'+self.__tabla +' ORDER BY Id DESC')
            data=cursor.fetchall()
            arreglo=[]
            for fila in data:
                uvo = UsuariosVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                arreglo.append(uvo)
            return arreglo
        except Exception as d:
            return json.dumps({'error':str(d)})
        finally:
            cursor.close()
            conn.close()