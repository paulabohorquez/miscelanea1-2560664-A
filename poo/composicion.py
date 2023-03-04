class Curso:  #se crea la clase curso
    def __init__(self,titulo): #se crea al constructor con sus parametros
        self.__titulo=titulo #definimos el atributo titulo

    def getTitulo(self): #se crea el metodo 
        return self.__titulo #se retorna el titulo

class Aprendiz: #se crea la clase aprendiz

    def __init__(self,nombre): ##se crea al constructor con sus parametros
        self.__nombre=nombre #definimos el atributo
        self.__cursos=[]#creamps la lista

    def agregarCurso(self,nombreCursito):#creamos el metodo con sus parametros
        cursito=Curso(nombreCursito)# le asignamos a cursito la clase curso
        self.__cursos.append(cursito) #le agregamos a la lista cursito

    def getCursos(self): #creamos el metodo con su parametro 
        return self.__cursos #retornamos la lista 

ap=Aprendiz('Sofia') #se crea un objeto de la clase aprendiz
ap.agregarCurso('Python Basico') #utilizamos el metodo de la clase curso
ap.agregarCurso('Python Intermedio') #utilizamos el metodo de la clase curso

for c in ap.getCursos(): #recorreremos todos los elementos de la lista 
    print(c.getTitulo()) #se imprimen

del ap #eliminamos a la clase aprendiz
