n=1
contador=0
while True:
    n=int(input("ingrese un numero: "))
    contrario=n*-1
    if n==0:
        print("la cantidad de numeros ingresados fue: ", contador)
        break
    elif n>0:
        print("el numero es ",n," y su contrario es: ", contrario)
    else:
        print("el numero es ",n," y su contrario es: ", contrario)
    contador+=1