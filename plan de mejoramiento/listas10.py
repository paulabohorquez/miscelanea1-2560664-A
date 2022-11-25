#Un programa que necesita determinar si un elemento pertenece o no 
#a una lista y actuar en consecuencia puede hacerlo asi
conjunto = [1, 2, 3]
elemento = int(input("Dame un numero: "))
if elemento not in conjunto:
    conjunto.append(elemento)
print(conjunto)