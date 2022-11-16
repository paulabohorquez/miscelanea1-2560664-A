import random
vector=[]
d=True
a=0
b=1
c=1
while d:
    num=int(input("elija la cantidad de elementos a ejecutar de a serie de fibonacci: "))
    if num>=5 and num<=20:
        d=False
    else:
        print("minimo 5 elementos y maximo 20")
for i in range(num):
    c=a+b
    a=b
    b=c
    vector.append(c)
print("los numeros de la serie de fibonacci son: ", vector)