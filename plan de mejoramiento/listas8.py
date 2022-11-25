'''Diseñemos un programa que, dados un elemento y una lista, nos diga
si el elemento pertenece o no a la lista mostrando en pantalla el mensaje 
Pertenece o No pertenece en funcion del resultado.'''
elemento = 5
lista = [1, 4, 5, 1, 3, 8]
pertenece = False
for i in lista:
    if elemento == i:
        pertenece = True
        break

if pertenece:
    print("si pertenece")
else:
    print("No pertenece")