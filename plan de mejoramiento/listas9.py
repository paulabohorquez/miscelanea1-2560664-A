'''Recapitulemos: para ordenar una lista de n elementos hemos de hacer n-1 pasadas. En
cada pasada conseguimos poner al menos un elemento en su posicion: el mayor. (Hacen falta
n−1 y no n porque la ultima pasada nos pone dos elementos en su sitio: el mayor va a la
segunda posicion y el menor se queda en el unico sitio que queda: la primera celda de la lista.)
Intentemos codificar esa idea en Python:'''



lista = [2, 26, 4, 3, 1]
for i in range(1, len(lista)):
    for j in range(0, len(lista)-i):
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
print (lista)