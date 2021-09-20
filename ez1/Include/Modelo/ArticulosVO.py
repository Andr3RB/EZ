class ArticulosVO:
 
    def __init__(self, idarticulo, tienda, cantidad, precio, marca):
        self.__idarticulo = idarticulo
        self.__tienda = tienda
        self.__cantidad = cantidad
        self.__precio = precio
        self.__marca = marca
 
    def setIdarticulo(self,n):
        self.__idarticulo = n

    def getIdarticulo(self,n):
        return self.__idarticulo
 
    def setTienda(self,n):
        self.__tienda = n

    def getTienda(self,n):
        return self.__tienda

    def setCantidad(self,n):
        self.__cantidad = n

    def getCantidad(self,n):
        return self.__cantidad
 
    def setPrecio(self,n):
        self.__precio = n

    def getPrecio(self,n):
        return self.__precio    
 
    def setMarca(self,n):
        self.__Marca = n

    def getMarca(self,n):
        return self.__marca

