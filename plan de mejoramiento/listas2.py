'''ordenado de enteros y con posibles
repeticiones de valores, obtenga como salida una lista de
los números ordenados, pero sin repeticiones.'''
VEC =[]
N = int( input("Ingrese número de elementos del vector"))
if 1 <= N and N <= 200:
    for i in range(1,N+1):
        elemento = int(input("Ingrese Entero: "))
    VEC.append(elemento)
i = 0
lista_nueva = [] 
for elemento in VEC:
    if elemento not in lista_nueva:
        lista_nueva.append(elemento) 
lista_nueva.sort()
print(lista_nueva)