class Curso: #creamos la clase curso
    def __init__(self,nombre,horas):#iniciamos el constructor con sus parametros
        self.__nombre=nombre #asignamos los parametros
        self.__horas=horas #asignamos los parametros
    def getNombre(self): #creamos un metodo get
        return self.__nombre #retornamos el nombre