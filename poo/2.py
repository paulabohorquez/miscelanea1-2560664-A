
class producto:
    counter = 0
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.__precio=precio
        producto.counter += 1

    def getnombre(self):
        return self.nombre
    
    def getprecio(self):
        return self.__precio
    
    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setprecio(self,precio):
        self.precio=precio

class calcular (producto):
    def __init__(self, nombre,precio):
        self.nombre=nombre
        self.precio=precio*0.19
        print(self.precio)

    def getcalcular (self):
        return self.precio
    
    def setcalcular(self, precio):
        self.precio=precio

prod1=calcular("televisor",int(1500000))
prod2=calcular("celular",850000)

print(prod2)
print(prod2.getcalcular)
print(producto.counter)

