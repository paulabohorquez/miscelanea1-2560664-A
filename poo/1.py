class Persona: #se crea una clase llamada persona 
    def __init__(self,nombre): # se crea una funcion con el constructor y su parametro self, tambien se pone otro parametrro nombre
        self.__nombre=nombre #se inicializa el parametro
        #print('Constructor Activado')        

    def getNombre(self): #se crea una funcion con el argumento self
        return self.__nombre #se retorna el nombre de maria

    def setNombre(self,nombre): #se crea a funcion con argumentos self y nombre
        self.__nombre=nombre  #se inicializa el parametro
        
class Aprendiz(Persona): #se crea a clase aprendiz herendando de la clase persona 
    def __init__(self,nombre,ficha): #se crea una funcion con los parametros
        Persona.__init__(self,nombre) # se hereda de persona
        self.__ficha=ficha #se inicializa el parametro
        

    def getFicha(self): #se crea la funcion get
        return self.__ficha #se retorna la ficha
    
class documento(Persona): #se crea la clase documento heredando de persona 
    def __init__(self,nombre,documento): #se crea la funcion con los parametros 
        self.__documento=documento #se inicializa el parametro
    def getdocumento(self): #se crea la funcion 
        return self.__documento #se retorna el documento

    def setdocumento(self,documento): #se crea la funcion 
        self.__documento=documento #se inicializa el parametro

class todo(Persona):
    def __init__(self,nombre,documento,ficha):
        self.__nombre=nombre
        self.__documento=documento
        self.__ficha=ficha
    def gettodo(self):
        print  (self.__nombre, self.__documento, self.__ficha)




app=todo("pedro" ,12345, 256)
print(app.gettodo())    


                 

