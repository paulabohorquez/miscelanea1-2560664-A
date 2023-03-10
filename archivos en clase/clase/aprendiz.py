from Persona import * #importamos la clase persona 
#from Curso import * ...en caso de composición
class Aprendiz(Persona):#creamos la clase aprendiz heredando de padre
    def __init__(self,ficha,nombre,documento):#iniciamos el constructor con todos los argumentos
        Persona.__init__(self,nombre,documento)#son los atributos que se heredan de la clase padre
        self.__ficha=ficha #asignamos los parametros
        self.__cursos=[]#iniciamos la lista 
    def getFicha(self):#creamos el metodo get
        return self.__ficha#retornamos la ficha 
    def setNombre(self,ficha):#creamos el metodo set
        self.__ficha=ficha#asignamos los parametros
    def agregarCurso(self,curso):#creamos el metodo agregar curso
        #c=Curso('python',120) 
        self.__cursos.append(curso)#agregamos a la lista el numero de curso
    def getCursos(self): #creamos el metodo get
        return self.__cursos #retornamos la lista