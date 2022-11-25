'''Crear un algoritmo, que dado N números enteros ingresados 
por teclado determine cuál de ellos es el menor y mayor respectivamente.'''
lim = int(input("Ingrese la cantidad de números a comparar:"))
n = int(input("Ingrese los números: "))
men = n
may = n
for i in range(1, lim):
    n = int( input("Ingrese número: "))
    if n < men :
        men = n
    else:
        if n > may :
            may = n
print ("El número menor es :" ,men)
print ("El número mayor es :", may)