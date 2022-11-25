'''Ingresar 5 caracteres e indicar cuantas veces se repite el
carácter ‘a’.'''
ca = 0
numCar = 5
print("Ingrese", numCar, "caracteres: ")
for i in range(0, numCar):
    m = input("Ingrese Caracter: ")
    if m == "a" :
        ca = ca + 1
print ("En", numCar, "caracteres hay", ca, "caracteres 'a'")