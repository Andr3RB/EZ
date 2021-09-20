class UsuariosVO:

    def __init__(self, id, nombre, tienda, correo, contrasena, idCoV):
        self.__id = id
        self.__nombre = nombre
        self.__tienda = tienda
        self.__correo = correo
        self.__contrasena = contrasena
        self.__idCoV = idCoV

    def setId(self, n):
        self.__id = n   
    
    def getId(self):
        return self.__id

    def setNombre(self, n):
        self.__nombre = n   
    
    def getNombre(self):
        return self.__nombre

    def setTienda(self, n):
        self.__tienda = n   
    
    def getTienda(self):
        return self.__tienda

    def setCorreo(self, n):
        self.__correo = n   
    
    def getCorreo(self):
        return self.__correo

    def setContrasena(self, n):
        self.__contrasena = n   
    
    def getContrasena(self):
        return self.__contrasena

    def setIdCoV(self, n):
        self.__idCoV = n   
    
    def getIdCoV(self):
        return self.__idCoV
    