from flask import json
import Include.conexion as cnx 
from Include.Modelo.UsuariosVO import UsuariosVO

class UsuariosDAO:
    def __init__(self):
        self.__tabla = "Usuarios"