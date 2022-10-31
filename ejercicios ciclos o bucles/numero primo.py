num = int(input("ingrese numero para determinar si es primo o no: "))
i=1
a = 0
while(num > i):
    if num%i ==0:
       a+=1
    i+=1
    if a > 2 or num <=1:
            print("el numero no es primo")
    else:
         print("el numero es primo")
                
