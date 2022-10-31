num = int(input("ingrese un numero y se determinara sus divisores: "))
i = 1
print("los divisores son: ")
while(num >= i):
    if num%i == 0:
        print(i)
        i+=1