class producto:
    counter=0
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio*0.19
        print(self.precio)
        producto.counter+=1


    def getproducto (self):
        return self.precio
    
    def setproducto(self, precio):
        self.precio=precio

prod1=producto("televisor",int(1500000))
prod2=producto("celular",850000)

print(prod2)
print(prod1)
print(producto.counter)
