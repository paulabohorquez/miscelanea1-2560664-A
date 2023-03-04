class Aprendiz: #se crea la clase aprendiz
    def __init__(self,nombre): #creamos el constructor con su parametro 
        self.__nombre=nombre #definimos el atributo
        self.__cursos=[] #creamps la lista
    def agregarCurso(self,nombreCurso): #creamos el metodo con sus parametros
        self.__cursos.append(nombreCurso) #le agregamos a la lista 
    def verCursos(self): #creamos el metodo con su parametro
        return self.__cursos #retornamos

class Curso: #se crea la clase curso
    def __init__(self,nombreCurso): #creamos el constructor con su parametro 
        self.__nombreCurso=nombreCurso #definimos el atributo

    def getNombreCurso(self): #creamos el metodo
        return self.__nombreCurso #retornamos

ob=Aprendiz('Miguel') #se crea un objeto de la clase aprendiz
c1=Curso('Python Basico') #se crea un objeto de la clase curso
c2=Curso('Python Intermedio') #se crea un objeto de la clase curso
c3=Curso('Java Basico') #se crea un objeto de la clase curso

ob.agregarCurso(c1) #utilizamos el metodo de la clase aprendiz
ob.agregarCurso(c2) #utilizamos el metodo de la clase aprendiz
ob.agregarCurso(c3) #utilizamos el metodo de la clase aprendiz

for curso in ob.verCursos(): #recorreremos todos los elementos de la lista 
    print(curso.getNombreCurso()) #se imprimen

del ob #eliminamos a la clase aprendiz
#print(ob)
print('.....',c1.getNombreCurso())