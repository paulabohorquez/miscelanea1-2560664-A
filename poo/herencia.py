
class Vehiculo: #le asigna a la clase el nombre vehiculo
    def __init__(self,tipo): # ponemos de parametro tipo y el constructor con  su parametro 
        self.tipo=tipo #aqui accedemos al parametro
    def descripcion(self): #definimos el metodo llamado descripcion 
        print('Soy generico no tengo descripcion',self.tipo) #imprimimos 
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):#creamos el metodo gettipo para poder acceder a el 
        return self.tipo #lo retornamos 
        #return Vehiculo.tipo
    def __str__(self): #ponemos el metodo str para retornarlo  informando de que clase es el objeto segun en el orden que este 
        return 'Soy objeto de la clase Vehiculo' #retornara este mensaje 

class Herramienta: #creaamos una clase llamada herramienta
    def __init__(self,proposito):# ponemos e parametro proposito en este metodo
        self.__proposito=proposito #aqui accedemos al parametro
    def getProposito(self): #creamos el metodo gettipo para poder acceder a el 
        return self.__proposito #lo retornamos
    def __str__(self): #ponemos el metodo str para retornarlo  informando de que clase es el objeto segun en el orden que este 
        return 'Soy objeto de la clase Herramienta' #retornara este mensaje 
class Terrestre(Vehiculo,Herramienta): #creamos una clase que se hereda de las superclases vehiculo y herramienta
    def __init__(self,tipo,proposito):
        Herramienta.__init__(self,proposito)
        Vehiculo.__init__(self,tipo)        
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())
 