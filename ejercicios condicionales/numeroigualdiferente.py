a = int(input("ingrese el numero: "))
b = int(input("ingrese el numero: "))
c = int(input("ingrese el numero: "))
if a == b and b == c:
    print("los tres numeros son iguales")
elif a == b and b != c:
    print("solo hay dos numeros iguales")
elif a != b and b == c:
    print("solo hay dos numeros iguales")
elif a != c and b == c:
    print("solo hay dos numeros iguales")
else:
    print("los tres numeros son diferentes")

