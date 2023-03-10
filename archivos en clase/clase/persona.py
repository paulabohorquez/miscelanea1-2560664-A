class Persona: #cramos la clase persona
    def __init__(self,nombre,documento): #se inicia el constructor con los parametros
        self.__nombre=nombre 
        self.__documento=documento
    def getNombre(self): #iniciamos el metodo get
        return self.__nombre #retornamos el nombre
    def getDocumento(self):#iniciamos el metodo get
        return self.__documento #retornamos el documento
    def setNombre(self,nombre):#iniciamos el metodo set con sus parametros
        self.__nombre=nombre 
    def setDocumento(self,documento):#iniciamos el metodo set con sus parametros
        self.__documento=documento