a = int(input("ingrese un numero entre 0 y 9999: "))
b = a
if b<0 and b>9999:
    print("el numero es invalido")
elif b>=0 and b<=9:
    print("el numero tiene una cifra")
elif b>=10 and b<=99:
    print("el numero tiene dos cifras")
elif b>=100 and b<=999:
    print("el numero tiene tres cifras")
elif b>=1000 and b<=9999:
    print("el numero tiene cuatro cifras")
elif b>=10000:
    print("el numero infresado es invalido")
    
