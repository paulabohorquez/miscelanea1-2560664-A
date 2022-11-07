import random

r=(round(random.random()*100))
cont=0
while True:
    n = int(input('Ingrese un numero: '))
    cont+=1
    if n>r:
        print ('El numero es menor, intentelo de nuevo')
    elif n<r:
        print ('El numero es mayor, intentelo de nuevo')
    else:
        print ('Felicidades, encontró el numero, las veces q lo intento fueron:',cont)
        break