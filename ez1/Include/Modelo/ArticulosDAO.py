from flask import json
import Include.conexion as cnx 
from Include.Modelo.ArticulosVO import ArticulosVO

class ArticulosDAO:
    def __init__(self):
        self.__tabla = "Articulos"

    def selectALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM ' +self.__tabla +' ORDER BY Id DESC')
            data=cursor.fetchall()
            arreglo=[]
            for fila in data:
                uvo = ArticulosVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                arreglo.append(uvo)
            return arreglo
        except Exception as d:
            return json.dumps({'error':str(d)})
        finally:
            cursor.close()
            conn.close()