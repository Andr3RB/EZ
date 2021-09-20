class ArticulosVO:
 
    def __init__(self, idarticulo, tienda, cantidad, precio, marca, tipo_art):
        self.__idarticulo = idarticulo
        self.__tienda = tienda
        self.__cantidad = cantidad
        self.__precio = precio
        self.__marca = marca
        self.__tipo_art = tipo_art

    def setIdarticulo(self,n):
        self.__idarticulo = n

    def getIdarticulo(self):
        return self.__idarticulo
 
    def setTienda(self,n):
        self.__tienda = n

    def getTienda(self):
        return self.__tienda

    def setCantidad(self,n):
        self.__cantidad = n

    def getCantidad(self):
        return self.__cantidad
 
    def setPrecio(self,n):
        self.__precio = n

    def getPrecio(self):
        return self.__precio    
 
    def setMarca(self,n):
        self.__marca = n

    def getMarca(self):
        return self.__marca

    def setTipo_art(self,n):
        self.__tipo_art = n

    def getTipo_art(self):
        return self.__tipo_art

