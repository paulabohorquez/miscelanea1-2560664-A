'''El código del ejercicio 1 de Vectores en Python usando
mientras (while) es el siguiente'''
i = 1
F = [] 
numElementos = int( input("Ingrese Número de elementos a Ingresar: "))
while i <= numElementos:
    elemento = int( input("Ingrese Elemento: "))
    F.append(elemento) #Agregamos el elemento a la lista
    i = i + 1
print(F) 