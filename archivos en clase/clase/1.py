from Aprendiz import * #importamos la clase aprendiz
from Curso import * #importamos la clase curso

# nombre=input('ingrese nombre del aprendiz')
# documento=int(input('ingrese documento del aprendiz'))
# ficha=input('ingrese ficha del aprendiz')

# ap=Aprendiz(ficha,nombre,documento)

# nombreCurso=input('ingrese nombre del curso')
# horas=int(input('ingrese intensidad horaria del curso'))
# c1=Curso(nombreCurso,horas)
# ap.agregarCurso(c1)

# with open('herencia/aprendices.txt','a') as flujo:    
#     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

with open('herencia/aprendices.txt','r') as flujo: #le asignamos a flujo la ruta relativa de la ubicacion del archivo
    datos=flujo.read() #le asignamos a datos el archivo para leer su contenido   
    print(datos)#imprimimos la variable
    #flujo.write('2560664,maria,123')
aprendices=[] #creamos una lista
with open('herencia/aprendices.txt','r') as flujo: #le asignamos a flujo la ruta relativa de la ubicacion del archivo
    for linea in flujo: #recorremos cada linea del archivo
        #print(linea)
        aprendices.append(linea.rsplit())#le agregamos a la lista aprendices y le ponemos este metodo para quitzr el salto de linea

datosxlinea=[] #creamos una nueva lista
for aprendiz in aprendices:#recorremos la lista aprendices 
    datosxlinea.append(aprendiz[0].split(','))#agregamos a la nueva lista el primer dato que halla antes de la primera coma

#print(ob.getNombre())

print(datosxlinea) #imprimimos la lista

listaDeObjetos=[] #se crea una nueva lista 
for apr in datosxlinea: #recorremos la lista
     f=apr[0]# le asignamos a la variable el dato que este en la posicion 0 de la lista
     n=apr[1]# le asignamos a la variable el dato que este en la posicion 1 de la lista
     d=apr[2]# le asignamos a la variable el dato que este en la posicion 2 de la lista
     ob=Aprendiz(f,n,d) #instanciamos el objeto de a clase aaprendiz, teniendo como argumentos las variables 
     print(ob)#imprimimos 
     listaDeObjetos.append(ob) #agregamos a una nueva lista las variables

for xx in listaDeObjetos: #recorremos la lista 
    print(xx.getNombre()) #imprimimos cada elemento aparte 
    print(xx.getDocumento()) #imprimimos cada elemento aparte
    print(xx.getFicha()) #imprimimos cada elemento aparte